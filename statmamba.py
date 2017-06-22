# statmamba.py

###

from tablePuller import *
from visualize import *
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor


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
    
for year in range(2010, 2017):
    team_query('NYK', str(year), 'totals')

'''

def makeframe(path): 
    df = pd.read_csv(path)
    df = df.fillna(0.0) # replaces all NaN with 0.0
    return df


years = ['2010-11', '2011-12', '2012-13', '2013-14', '2014-15', 
         '2015-16', '2016-17']

#for year in years: 
'''        
year = 'total'
print('\n' + year)
df = makeframe(str(dir_path + '/General Fours/' + year + '.csv'))
#x = df[['EFG%', 'OPP EFG%', 'TOV%', 'OREB%']]
#x = df[['FTA RATE', 'TOV%', 'EFG%','OREB%',  'OPP EFG%',  'OPP FTA RATE',  'OPP TOV%',  'OPP OREB%' ]]
y = df[['TEAM', 'WIN%']]
y['LOSE%'] = 1 - df[['WIN%']]
y1 = y[['LOSE%']]
print(df)

# Find and print the OLS Regression
result = sm.OLS(y1, x).fit()
print(result.summary())

vif = [variance_inflation_factor(x.values, i) for i in range(x.shape[1])]
print(vif)

'''
### Regression Formulas ###
"""
2010-11: 
    LOSE% = -0.0452 EFG% + 0.0383 TOV% + 0.0513 OPP EFG% - 0.0151 OREB% 

2011-12: 
    LOSE% = -0.0400 EFG% + 0.0599 OPP EFG% - 0.0175 OREB% 
    
2012-13: 
    LOSE% = -0.0413 EFG% + 0.0578 OPP EFG% - 0.0120 OREB% 
    
2013-14: 
    LOSE% = -0.00451 EFG% + 0.0551 OPP EFG%

2014-15: 
    LOSE% = -0.0484 EFG% + 0.0585 OPP EFG%
    
2015-16: 
    LOSE% = -0.0462 EFG% + 0.0656 TOV% + 0.0460 OPP EFG% - 0.0188 OREB%  
    
2016-17:
    LOSE% = -0.0452 EFG% + 0.0383 TOV% + 0.0513 OPP EFG% - 0.0151 OREB%
"""


year = '4years'
print('\n' + year)
df = makeframe(str(dir_path + '/League Totals Wins/' + year + '.csv'))
#print(df)
x = df[['FG', 'FGA', 'FG%','3P', '3PA', '3P%', '2P', '2PA', '2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']]
#x = df[['FGA', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'TOV', 'PTS']]
y = df[['Team', 'WIN%']]
y['LOSE%'] = 1 - df[['WIN%']]
y2 = df[['WIN%']]
y1 = y[['LOSE%']]
result = sm.OLS(y2, x).fit()
print(result.summary())

#k = df.loc[y['TEAM'] == 'New York Knicks']
#print(k)

print(x)

vif = [variance_inflation_factor(x.values, i) for i in range(x.shape[1])]
print(vif)


# Though these variables: 'FGA', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'TOV', 'PTS'
# were highly significant, with a |t| > prb ~ 0.000, 
# we found that these variables are highly colinear. VIF values are much higher than one. 
#[1513.2273856120787, inf, inf, inf, 224.31973181679464, 145.49554440420221, 184.10781155657105, 1078.1143533417589]






print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
