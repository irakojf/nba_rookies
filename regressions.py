# regressions.py

###

from tablePuller import *
from visualize import *
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor


dir_path = os.path.dirname(os.path.realpath(__file__))

def makeframe(path): 
    df = pd.read_csv(path)
    df = df.fillna(0.0) # replaces all NaN with 0.0
    return df



year = 'lal2017'
print('\n' + year)
df1 = makeframe(str(dir_path + '/gamelogs/' + year + '.csv'))
df1 = df1.convert_objects(convert_numeric=True)
df1['2PA'] = df1['FGA'] - df1['3PA']
df1['DRB'] = df1['TRB'] - df1['ORB']
df1['3P%'] = df1['3P'] / df1['3PA']
df1['2P%'] = (df1['FG'] - df1['3P']) / df1['2PA']

df1['Y-Hat'] = (-0.0231 * df1['3PA'] +
               -0.0295 * df1['2PA'] + 
               0.0334 * df1['ORB'] + 
               0.0485 * df1['DRB'] + 
               0.0401 * df1['AST'])

#df1['Y-Hat'] = abs(df1['Y-Hat'])

for cols in df1.columns.tolist()[1:]:
    df2 = df1.loc[df1['Y-Hat'] > 0.55] # If Y-Hat is greater than .55, then it should predict a win. 

df3 = df2[['Y-Hat', 'W/L']]
print(df3)

print('\nPredicted Wins')
yhat = ((df3['Y-Hat'] >= 0.55).sum())
print(yhat)


print('\nOverestimations')
overest = ((df3['W/L'] == 'L').sum())
print(overest)

for cols in df1.columns.tolist()[1:]:
    df2 = df1.loc[df1['Y-Hat'] < 0] # If Y-Hat is negative, then it should predict a loss. 

df3 = df2[['Y-Hat', 'W/L']]
print(df3)

print('\nUnderestimations')
underest = ((df3['W/L'] == 'W').sum())
print(underest)

print('\nTotal Errors')
print(overest + underest)





'''
#Scrape advanced data for each team from 2013 to 2017.
yrs = ['2013', '2014', '2015', '2016', '2017']
for year in yrs: 
    gamelogs('NYK', year)

#Join scraped data with older data (advanced plus basic stats combined)
#Export into a new folder for the past five seasons. 
yrs = ['2013', '2014', '2015', '2016', '2017']
for year in yrs: 
    df1 =  df.from_csv(dir_path + '/gamelogs/' + year + '.csv')
    result = pd.concat([df1], axis=1)
    
    newfolder = str( 'gamelogs' )
    if not os.path.exists(newfolder):
        os.makedirs(newfolder)
    
    global path
    path = newfolder + '/' + year + ".csv"
    
    result.to_csv(path)
    
    
### Merge all tables from every year into one csv file.
a = df.from_csv(dir_path + '/gamelogs/2013.csv')
b = df.from_csv(dir_path + '/gamelogs/2014.csv')
c = df.from_csv(dir_path + '/gamelogs/2015.csv')
d = df.from_csv(dir_path + '/gamelogs/2016.csv')
e = df.from_csv(dir_path + '/gamelogs/2017.csv')
result = a.append([b, c, d, e])
result.to_csv(dir_path + '/gamelogs/total.csv')
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

### Set everything up and convert everything into a number
year = '2017'
print('\n' + year)
df1 = makeframe(str(dir_path + '/gamelogs/' + year + '.csv'))
df1 = df1.convert_objects(convert_numeric=True)
df1['2PA'] = df1['FGA'] - df1['3PA']
df1['DRB'] = df1['TRB'] - df1['ORB']
df1['3P%'] = df1['3P'] / df1['3PA']
df1['2P%'] = (df1['FG'] - df1['3P']) / df1['2PA']

y = df1[['W=1']] 

# 3PA, 2PA, ORB, DRB, AST
# FG%, FGA, FG, AST, ORB, DRB
        
xvar = [ 
#        '2P%',
        '2PA',
#        '3P%',
#        '3PA',
        'AST', 
#        'ORB',
        'DRB',
#        'TOV'
        ]
x1 = df1[xvar]
        
# Run the Regression
result = sm.OLS(y, x1).fit()
print(result.summary())
        
        
#Calculate the VIF
#vif = [variance_inflation_factor(x.values, i) for i in range(x.shape[1])]
#print(vif)
        
       
#df1['Beta*2P%'] = 0.4185 * df1[['2P%']]
df1['Beta*2PA'] = -0.0193 * df1[['2PA']]
#df1['Beta*3P%'] = 0.3632 * df1[['3P%']]
df1['Beta*3PA'] = 0.0283 * df1[['3PA']]
#df1['Beta*AST'] = 0.0536 * df1[['AST']]
#df1['Beta*ORB'] = 0.0263 * df1[['ORB']]
df1['Beta*DRB'] = 0.0300 * df1[['DRB']]
#df1['Beta*TOV'] = -0.0332 * df1[['TOV']]
        
df1['Y-Hat'] = (
#        df1['Beta*2P%'] +
        df1['Beta*2PA'] + 
#        df1['Beta*3P%'] + 
        df1['Beta*3PA'] +
#        df1['Beta*AST'] +
#        df1['Beta*ORB'] +
        df1['Beta*DRB'] 
#        df1['Beta*TOV']
        )
     
# Run correlation between y-hat and prediction variables
for x in xvar: 
    a = df1[['Y-Hat', x]].corr()    
    print(a)

b = [
     -0.538999,
     0.204022,
     0.584208,
#     0.598783,
#     0.599934,
#     0.545723,
#     0.409126,
#     0.487451,
     ]

c = []
for b1 in b: 
    c.append(b1 * b1)
    
d = []
for c1 in c: 
    d.append(float(c1 * 0.595))
        
corr = pd.DataFrame(
        {'x-var': xvar,
         'strcoef': b,
         'strcoef^2': c,
         'explanation': d
         })
    
print('\n')
print(corr)
print('\n')


"""