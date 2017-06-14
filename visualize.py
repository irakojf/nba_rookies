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

def get_df(name, groupby, stat): 
    # groupby: ['Big Men', 'Guards', 'PG', 'SG' ... 'C']
    # stat: advanced or per_game
    path = dir_path + '/' + stat + '_exports/' + groupby + '/' + name + '.csv'
    df = pd.read_csv(path)
    df = df.fillna(0.0) # replaces all NaN with 0.0
    return df

#### Sample Queries ####

# Select the player column (multiple queries)
    # print( df.iloc[1:]['Player'] )
    # print( df.loc[:, 'Player'] )
    
# Select the first row 
    # print( df.iloc[2] )
    # Prints the header as well as the first row 

# Select the value
    # print( df.iloc[1][8] )
    # [index_row][index_column]

# Select multiple columns
    # print ( df[['Player', 'PER']] )
    

### Queries ###
# query() returns df
# scrape(sleepers, 'per_game')
 

def plotCenters(name):
    df = get_df(name, 'C', 'advanced') 
    df2 = df[['Season', 'PER']] # only output the 'Season' and 'PER' columns
    
    # find the index of the 'Career' value
    # since the index outputs as numpy [4], convert into a list
    # loop through the list and set b equal to index value
    a = list(df2.loc[df2['Season'] == 'Career'].index)
    for i in a: 
        b = i
    df2 = df2[:b]
    df3 = df2['PER']  
    df3.plot()

### Queries ###
"""

setB = ['DeAndre Jordan', 'Steven Adams']
for center in setB: 
    plotCenters(center)
plt.legend(setB)

"""


def plotGuards(name):
    df = get_df(name, 'Guards', 'advanced') 
    df2 = df[['Season', 'OBPM']] # only output the 'Season' and 'PER' columns
    
    # find the index of the 'Career' value
    # since the index outputs as numpy [4], convert into a list
    # loop through the list and set b equal to index value
    a = list(df2.loc[df2['Season'] == 'Career'].index)
    for i in a: 
        b = i
    df2 = df2[:b]
    df3 = df2['OBPM']  
    df3.plot()


setA = ['Kyle Lowry', 'Isaiah Thomas', 'Kyle Korver', 'Lance Stephenson', 'Jeremy Lin']
for player in setA: 
    plotGuards(player)
plt.legend(setA)



print(get_df('Jeremy Lin', 'Guards', 'advanced'))




