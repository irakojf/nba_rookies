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


def plot(name, statgroup, stat, perchange, groupby=''):
# Plots a time series of a particular stat's change over time where
# Also returns the time series 
    if perchange == True: 
        title = ( stat + ' % change over time for ' + name )
        print(title)
        df = get_df(name, statgroup, groupby) 
        # only output the 'Season' , 'Tm' and 'PER' columns
        df2 = df[['Season', 'Tm', stat]] 
        
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
        yaxis = pd.Series(yaxis, name='%change')
        #print(yaxis)
        
        
        # X-Axis
        xaxis = []
        for i in df2['Season'][1:]: 
            xaxis.append(i)
        xaxis = pd.Series(xaxis, name='Year to year')
        #print(xaxis)
        
        table = pd.concat([xaxis, yaxis], axis=1)
        out = df2.join([xaxis, yaxis])
        table.plot(x=xaxis)
        plt.legend([name], title=title)
        print(out)
        return out
    
    else:
        title = ( stat + ' over time for ' + name )
        print(title)
        df = get_df(name, statgroup, groupby) 
        df2 = df[['Season', 'Tm', stat]] # only output the 'Season' and 'PER' columns
        
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
        print(df2)
        table.plot(x=xaxis)
        plt.legend([name], title=title)
        return df2

#### Queries #### 

## NOTE: Must include 'Guard' or 'Big Men' or 'SF' for players in sleeper list
# Sample queries below:
    
    #plot('Jeremy Lin', 'advanced', 'PER', True, 'Guards')
    #plot('Jeremy Lin', 'advanced', 'PER', False, 'Guards')
    #plot('Jeremy Lin', 'per_game', 'PTS', False, 'Guards')
    #plot('DeAndre Jordan', 'advanced', 'PER', True, 'Big Men')
    

# See what stats you can use 
#print(get_df('Jeremy Lin', 'advanced', 'Guards'))

#guards = ['Seth Curry', 'Kyle Lowry', 'Isaiah Thomas']
#for players in guards: 
    #plot(players, 'advanced', 'PER', True, 'Guards')
    #plot(players, 'advanced', 'PER', False, 'Guards')


# Returns all the Spurs players
spurs = [] 
spurs_unique = []
for year in range(1999, 2018):
    df = pd.read_csv(dir_path + '/spurs/per_game/' + str(year) + '.csv')
    df = df[['Player']].values
    for i in df: 
        for j in i: 
            spurs.append(j)
                
for i in spurs:
    if i not in spurs_unique:
        spurs_unique.append(i)

spurs = spurs_unique

def create_frame(player): 
# Creates a dataframe given a player (that has played on the spurs)

    df = get_df(player, 'advanced')
    df = df.loc[df['Tm'] == 'SAS'] # Checks if the team is San Antonio
    df = df.loc[df['Age'] != 0.0 ]
    df = df[['PER', 'Season']]
    df = df.reset_index()
    
    
    # For each year the player has played on the Spurs, 
    # add a row entry containing the player's name
    player_col = []
    for i in range(0, int(len(df.index))): 
        player_col.append(player)

    # Creates a player column containing player names
    players = pd.Series(player_col, name='Player')
    df = df.join(players) # Add it to the dataframe

    
    # Reorders the columns so that Player is the first column
    col = df.columns.tolist()
    col = col[-1:] + col[:-1]
    df = df[col]
    return df 


a = create_frame('Tim Duncan')[['Player', 'PER', 'Season']]
b = create_frame('Danny Green')[['Player', 'PER', 'Season']]
c = pd.concat(frames).reset_index()[['Player', 'PER', 'Season']]
d = c.groupby(['Player'])


for player in ['Danny Green', 'Tim Duncan', 'Tony Parker']: 
    a = create_frame(player)[['Player', 'PER', 'Season']]
    DFGPlot = a.plot(kind='line', x='Season', y='PER', label=player)
    

#DFGPlot = b.plot(kind='bar', x='Season', y='PER', label='Tim Duncan')








##########################

### Old Queries ###  

'''

players = ['Jimmy Butler', 'Jae Crowder', 'Trevor Ariza', 'Nikola Mirotic']
for player in players: 
    plot(player, 'advanced', 'PER', False, 'SF')
    plot(player, 'per_game', 'PTS', False, 'SF')
 
centers = ['DeAndre Jordan', 'Ryan Anderson', 'Kenneth Faried', 'Rudy Gobert',
           'Hassan Whiteside', 'Jusuf Nurkic', 'Steven Adams', 'Clint Capela', 
           'Draymond Green']
for players in centers: 
    plot(players, 'advanced', 'TRB%', False, 'Big Men')
    #plot(players, 'advanced', 'PER', False, 'Big Men')

##########################

plot('Javale McGee', 'advanced', 'PER', True)
plot('Javale McGee', 'advanced', 'PER', False)

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


