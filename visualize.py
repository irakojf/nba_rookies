# visualize.py

###

from tablePuller import *



#### Sample Queries ####

# Select the player column (multiple queries)
    # print( query().iloc[1:]['Player'] )
    # print( query().loc[:, 'Player'] )
    
# Select the first row 
    # print( query().iloc[2] )
    # Prints the header as well as the first row 

# Select the value
    # print( query().iloc[1][8] )
    # [index_row][index_column]

# Select multiple columns
    # df = query()
    # print ( df[['Player', 'PER']] )
    


### Queries ###
# query() returns df
 
scrape(['Hassan Whiteside'], 'advanced')


"""
scrape(['Hassan Whiteside', 'Jeremy Lin', 'Draymond Green', 'Jae Crowder', 
        'Jimmy Butler', 'Kyle Lowry', 'Isiah Thomas', 'Kyle Corver', 'Lance Stephenson', 
        'Matthew Dellavadova', 'Marcin Gortat', 'Wesley Matthews', 'Seth Curry', 'Patrick Beverly', 
        'Trevor Ariza', 'Marc Gasol', 'Kenneth Farried', 'Will Barton', 'Rudy Gobert', 
        'DeAndre Jordan', 'Ryan Anderson', 'Tyler Johnson', 'Jusuf Nurkic', 'Nikola Mirotic', 
        'Steven Adams', 'Clint Capella' ], 'advanced')
"""





