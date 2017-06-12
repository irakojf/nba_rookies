# visualize.py

# Visualizes trends in .csv data

from getStat import *
from dataClean import sleeper

import os 
import pandas as pd
import numpy as np 


dir_path = os.path.dirname(os.path.realpath(__file__))
exports_path = dir_path + '/bbref_exports/'

def allPlayers():
    for i in sleeper():
        print( i )

def columns(name):
    columns = pd.read_csv(exports_path + name + '.csv').columns
    return (columns)

def read(name): 
    df = pd.read_csv(exports_path + name + '.csv', 
                     usecols = ['Season', 'Tm', 'Pos', 'AST', 'ORB']
                     )
    print ('\n' + name + '\n')
    print (df) 
    print ('\n')
    return df

def findData(): 
# Identifies which variables in the PER formula are 
# unavailable in our data set 
    
    formula = ["MP", "3P", "AST", "STL", "BLK", "PF", 
               "FG", "FGA", "FT", "FTA",
               "team_FG", "team_FG", "team_AST",
               "VOP", "TOV", "DRB%", "factor", "TRB",
               "ORB", "lg_FT", "lg_PF", "lg_FTA", "lg_PF"]
    
    havedata = []
    for column in columns('James Harden'): 
        havedata.append(column)
        
    match = (set(havedata) & set(formula))
    missingdata = set(formula) - match 
    
    print(missingdata)
    return(missingdata)


def VOP(season): 
    a = LeagueStat(season)    
    lg_PTS = a.get('PTS') 
    lg_FGA = a.get('FGA')
    lg_ORB = a.get('ORB%')
    lg_TO = a.get('TOV%')
    lg_FTA = a.get('FTA')
    
    VOP = lg_PTS / (lg_FGA - lg_ORB + lg_TO + 0.44 * lg_FTA)
    return VOP 

class LeagueStat(object): 
    
    def __init__(self, season): 
        self.season = season
        
    def get(self, stat): 
        df = pd.read_csv(dir_path + '/data/' + 'leagueAvgs.csv', 
                         usecols = [ 'Season' , stat ]
                         )
        out = df.loc[df['Season'] == self.season, stat].iloc[0].astype(float)
        return out

print(VOP('2016-17'))

    
    
    
    
    
    
    
    
    
    
    
    
    

