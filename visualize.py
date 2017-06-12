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

def read(name): 
    df = pd.read_csv(exports_path + name + '.csv', 
                     usecols = ['Season', 'Tm', 'Pos', 'AST', 'ORB']
                     )
    print ('\n' + name + '\n')
    print (df) 
    print ('\n')

#read('Nerlens Noel' )
#read('DeJuan Blair')


for i in sleeper(): 
    print(draft(playdict[i]))