# visualize.py

# Visualizes trends in .csv data

from getStat import *
from dataClean import sleeper
#%matplotlib inline


dir_path = os.path.dirname(os.path.realpath(__file__))
exports_path = dir_path + '/bbref_exports/'

def allPlayers():
    players = []
    for i in sleeper():
        print( i )
        players.append(i)
    return players

def columns(name):
    columns = pd.read_csv(exports_path + name + '.csv').columns
    return (columns)

def read(name): 
    df = pd.read_csv(exports_path + name + '.csv', 
                     usecols = ['Season', 'Tm', 'PTS']
                     )
    print ('\n' + name + '\n')
    print (df) 
    print ('\n')
    return df





# allPlayers()

#allPlayers()
#read('DeJuan Blair')
#read('Austin Daye')
#read('Jodie Meeks')
#read('Terrence Williams')
#read('Norris Cole')

###

player = 'DeJuan Blair'
read(player)

blair_PER = []    


#2009-10	SAS
#2010-11	SAS
#2011-12	SAS
#2012-13	SAS
#2013-14	DAL
#2014-15	WAS
#2015-16	WAS

SAS  = ['2009-10', '2010-11', '2011-12', '2012-13'] 
DAL = ['2013-14']
WAS = ['2014-15', '2015-16']

for i in SAS: 
    PER(player, i, 'SAS')
    
for i in DAL: 
    PER(player, i, 'DAL')
    
for i in WAS: 
    PER(player, i, 'WAS')
    


###

"""

read('James Harden')
# print(columns('James Harden'))

harden_PER = []    
hardenOKC  = ['2009-10', '2010-11', '2011-12'] 
hardenHOU = ['2012-13', '2013-14', '2014-15', '2015-16', '2016-17']

for years in hardenOKC: 
    a = PER('James Harden', years, 'OKC')
    harden_PER.append(a)
    
for years in hardenHOU: 
    a = PER('James Harden', years, 'OKC')
    harden_PER.append(a)
    
print(harden_PER)

"""

### 

"""
player = 'Brandon Jennings'
read(player)

jennings_PER = []    

jenningsMIL  = ['2009-10', '2010-11', '2011-12', '2012-13'] 
jenningsDET = ['2013-14', '2014-15', '2015-16']
jenningsORL = ['2015-16']
jenningsNYK = ['2016-17']
jenningsWAS = ['2016-17']

for i in jenningsMIL: 
    PER(player, i, 'MIL')
    
for i in jenningsDET: 
    PER(player, i, 'DET')
    
for i in jenningsORL: 
    PER(player, i, 'NYK')
    
for i in jenningsNYK: 
    PER(player, i, 'NYK')

for i in jenningsWAS: 
    PER(player, i, 'WAS')

    
"""



    
    

    

