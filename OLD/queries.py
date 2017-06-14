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



    
    

    

