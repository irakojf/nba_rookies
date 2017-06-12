# visualize.py

# Visualizes trends in .csv data

from getStat import *
from dataClean import sleeper

import os 
import pandas as pd
import numpy as np 
import requests


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



print(team_stat('1950-51', 'NYK', 'Pace'))
print(VOP('2016-17'))
print(factor('2016-17'))    

    
    
    
    
    
    
    

    

