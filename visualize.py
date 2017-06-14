# visualize.py

###

from tablePuller import *
import pandas as pd

### Helper Functions ### 
sleepers = ['Hassan Whiteside', 'Jeremy Lin', 'Draymond Green', 'Jae Crowder', 
        'Jimmy Butler', 'Kyle Lowry', 'Isaiah thomas', 'Kyle Korver', 'Lance Stephenson', 
        'Matthew Dellavedova', 'Marcin Gortat', 'Wesley Matthews', 'Seth Curry', 'Patrick Beverly', 
        'Trevor Ariza', 'Marc Gasol', 'Kenneth Faried', 'Will Barton', 'Rudy Gobert', 
        'DeAndre Jordan', 'Ryan Anderson', 'Tyler Johnson', 'Jusuf Nurkic', 'Nikola Mirotic', 
        'Steven Adams', 'Clint Capela' ]

dir_path = os.path.dirname(os.path.realpath(__file__))

def get_df(name, statgroup, groupby=''): 
    # groupby: ['Big Men', 'Guards', 'PG', 'SG' ... 'C']
    # statgroup: advanced or per_game
    path = dir_path + '/' + statgroup + '_exports/' + groupby + '/' + name + '.csv'
    df = pd.read_csv(path)
    df = df.fillna(0.0) # replaces all NaN with 0.0
    return df


def plot(name, statgroup, stat, groupby='', perchange=False):
# Plots a time series of a particular stat's change over time where
    if perchange == True: 
        title = ( stat + ' % change over time for ' + name )
        print(title)
        df = get_df(name, statgroup, groupby) 
        df2 = df[['Season', stat]] # only output the 'Season' and 'PER' columns
        
        # find the index of the 'Career' value
        # since the index outputs as numpy [4], convert into a list
        # loop through the list and set b equal to index value
        a = list(df2.loc[df2['Season'] == 'Career'].index)
        for i in a: 
            b = i
        df2 = df2[:b]
        df3 = df2[stat]  
        
        
        # Y-Axis
        yaxis = []
        for i in df3[1:]: 
            yaxis.append(float(i))
        yaxis.append(0.0)
        yaxis = (yaxis - df3)[:-1] # remove the last object in the list
        yaxis = pd.Series(yaxis)
        #print(yaxis)
        
        
        # X-Axis
        xaxis = []
        for i in df2['Season'][1:]: 
            xaxis.append(i)
        xaxis = pd.Series(xaxis, name='Season')
        #print(xaxis)
        
        table = pd.concat([xaxis, yaxis], axis=1)
        print(table)
        table.plot(x=xaxis)
        plt.legend([name])
    
    else:
        title = ( stat + ' over time for ' + name )
        print(title)
        df = get_df(name, statgroup, groupby='') 
        df2 = df[['Season', stat]] # only output the 'Season' and 'PER' columns
        
        # find the index of the 'Career' value
        # since the index outputs as numpy [4], convert into a list
        # loop through the list and set b equal to index value
        a = list(df2.loc[df2['Season'] == 'Career'].index)
        for i in a: 
            b = i
        df2 = df2[:b]
        df3 = df2[stat]  
        
        # Y-Axis
        yaxis = pd.Series(df3)
        
        # X-Axis
        xaxis = []
        for i in df2['Season']: 
            xaxis.append(i)
        xaxis = pd.Series(xaxis, name='Season')
        #print(xaxis)
        
        table = pd.concat([xaxis, yaxis], axis=1)
        print(table)
        table.plot(x=xaxis)
        plt.legend([name])


#### Queries #### 
plot('Klay Thompson', 'advanced', 'PER', True)


##########################

### Old Queries ###  
''' 
##########################


scrape(['Javale McGee'], 'advanced')
scrape(['Michael Jordan', 'Klay Thompson'], 'advanced')
scrape(['Michael Jordan', 'Klay Thompson'], 'per_game')


##########################


scrape(['Lebron James', 'Stephen Curry'], 'per_game')
setB = ['Lebron James', 'Stephen Curry']
for player in setB: 
    plot(player, 'per_game', 'AST')
    plt.legend(setB)

##########################

setA = ['Lebron James', 'Stephen Curry']
for player in setA: 
    plot_perchange(player, 'PER')
    plt.legend(setA)
    
##########################


# print(get_df('Jeremy Lin', 'Guards', 'advanced'))

'''


