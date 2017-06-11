# visualize.py

# Visualizes trends in .csv data


import os 
from dataClean import sleeper
import pandas as pd
import numpy as np 


global path
dir_path = os.path.dirname(os.path.realpath(__file__))
exports_path = dir_path + '/bbref_exports/'

def printAll():
    for i in sleeper():
        print( i )

def read(name): 
    df = pd.read_csv(exports_path + name + '.csv', 
                     usecols = ['Tm', 'Pos', 'AST', 'ORB']
                     )
    # Note: if all values in the row == NaN, 
    # the row may be the 'Career' row
    print (name + '\n')
    print (df) 

printAll()
read('Nerlens Noel' )