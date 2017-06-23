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





'''
#Scrape advanced data for each team from 2013 to 2017.
yrs = ['2013', '2014', '2015', '2016', '2017']
for year in yrs: 
    league_misc(year)

#Join scraped data with older data (advanced plus basic stats combined)
#Export into a new folder for the past five seasons. 
yrs = ['2013', '2014', '2015', '2016', '2017']
for year in yrs: 
    df1 =  df.from_csv(dir_path + '/league misc/' + year + '.csv')
    df2 = df.from_csv(dir_path + '/League Totals Wins/' + year + 'a.csv')
    result = pd.concat([df1, df2], axis=1)
    
    newfolder = str( 'league all stats')
    if not os.path.exists(newfolder):
        os.makedirs(newfolder)
    
    global path
    path = newfolder + '/' + year + ".csv"
    
    result.to_csv(path)
    
    
### Merge all tables from every year into one csv file.
a = df.from_csv(dir_path + '/league all stats/2013.csv')
b = df.from_csv(dir_path + '/league all stats/2014.csv')
c = df.from_csv(dir_path + '/league all stats/2015.csv')
d = df.from_csv(dir_path + '/league all stats/2016.csv')
e = df.from_csv(dir_path + '/league all stats/2017.csv')
result = a.append([b, c, d, e])
result.to_csv(dir_path + '/league all stats/total.csv')

'''
    
    
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


### Set everything up and convert everything into a number
year = 'total'
print('\n' + year)
df = makeframe(str(dir_path + '/league all stats/' + year + '.csv'))
df1 = df.drop('Team', axis=1)
df1 = df1.convert_objects(convert_numeric=True)
y = df[['W']] 

xvar = [
        '3PA', 
        '2PA', 
        'ORB', 
        'DRB', 
        'AST',
        'ORtg',
        'DRtg',
        ]
x1 = df1[xvar]

# Run the Regression
result = sm.OLS(y, x1).fit()
print(result.summary())


#Calculate the VIF
#vif = [variance_inflation_factor(x.values, i) for i in range(x.shape[1])]
#print(vif)


df1['Beta*3PA'] = 35.9594  * df1[['3PA']]
df1['Beta*2PA'] = -20.0278 * df1[['2PA']]
df1['Beta*ORB'] = 35.9594  * df1[['ORB']]
df1['Beta*DRB'] = -20.0278 * df1[['DRB']]
df1['Beta*AST'] = -20.0278 * df1[['AST']]
df1['Beta*ORtg'] = 2.4991 * df1[['ORtg']]
df1['Beta*DRtg'] = -2.1900 * df1[['DRtg']] 

df1['Y-Hat'] = (
        df1['3PA'] + 
        df1['2PA'] + 
        df1['ORB'] + 
        df1['DRB'] + 
        df1['AST'] +
        df1['ORtg'] + 
        df1['DRtg'] 
        )

# Run correlation between y-hat and prediction variables
for x in xvar: 
    a = df1[['Y-Hat', x]].corr()    
    print(a)

b = [    
#    0.0,
#    0.0,
#    0.0,
    0.0,
    0.0,
    0.0,
    0.734628,
    0.599427,
    0.556944,
    0.504105
    ]

c = []
for b1 in b: 
    c.append(b1 * b1)

corr = pd.DataFrame(
    {'x-var': xvar,
     'strcoef': b,
     'strcoef^2': c
    })

print('\n')
print(corr)

#k = df.loc[y['TEAM'] == 'New York Knicks']
#print(k)
