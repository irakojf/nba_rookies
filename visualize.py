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

"""

years = []
for i in range(0, 19):
    year = str(1999 + i)
    years.append(year)

timPER = [] 

for year in years: 
    df = team_query('SAS', year, 'advanced')
    try: 
        a = (df.loc[df['Player'] == 'Tim Duncan', 'PER']).values
        timPER.append( a )
    except KeyError: 
        pass

""" 

scrape(['Tim Duncan', 'Carmelo Anthony'], 'advanced')






