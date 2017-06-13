# statmamba.py

###

from tablePuller import *
from visualize import *
import pandas as pd


dir_path = os.path.dirname(os.path.realpath(__file__))



### Sample Queries ### 
'''

scrape(['Michael Jordan', 'Kobe Bryant'], 'advanced')
plot('Lebron James', 'advanced', 'ORB%', False)
team_query('NYK', '2013', 'per_game')

players = [ 'Michael Jordan', 'Kobe Bryant', 'Lebron James' ]
#scrape(players, 'advanced')

for player in players: 
    plot(player, 'advanced', 'ORB%', False)


'''

team_query('NYK', '2013', 'per_game')
team_query('NYK', '2014', 'per_game')
team_query('NYK', '2015', 'per_game')
team_query('NYK', '2016', 'per_game')


