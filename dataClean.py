# dataClean.py

# Takes [survey].txt files from surveyParse.py;
# Cleans and returns .csv files for each 'sleeper' individual player
# Can also produce .csv files for each 'best' individual player

import pandas as pd
import csv
import sys

from surveyParse import parse
from surveyParse import headers

def main():
    global file_list
    global a_list
    global b_list

    file_list = ['s0809.txt',
             's0910.txt',
             's1112.txt',
             's1213.txt',
             's1314.txt',
             's1415.txt',
             's1516.txt',
             's1617.txt']

    a_list = ['s0809.txt',
             's0910.txt',
             's1112.txt',
             's1213.txt'
             ]

    b_list = ['s1314.txt',
             's1415.txt',
             's1516.txt',
             's1617.txt']

def create( survey_file ):
    key = headers( survey_file )
    data = parse( survey_file )

    output = survey_file[:-4] + ".csv"
    with open(output, 'w') as csv_file:
        csv_app = csv.writer( csv_file )
        csv_app.writerow( key )
        csv_app.writerow( data )

def csv_create():
    # creates a CVS for the following text files
    for file in file_list:
        create(file)

def best_player():
    # creates a new .csv for each year's "best players in 5 years"

    best_player = []
    year = []
    for file in file_list:
        csv_file = file[:-4] + ".csv"
        df=pd.read_csv(csv_file, sep=',',header=None)
        df.values
        year.append( file )
        best_player.append( df.values[1][1] )

    with open('bestplayer.csv', 'w') as csv_file:
        csv_app = csv.writer( csv_file )
        csv_app.writerow( year )
        csv_app.writerow( best_player )

def sleeper():
    # creates a new .csv for each year's "sleeper successes"

    sleeper = []
    year = []
    for file in a_list:
        a = "/Users/irako/Desktop/nba_rookies/csvfiles/"
        csv_file = a + file[:-4] + ".csv"
        df=pd.read_csv(csv_file, sep=',',header=None)
        df.values
        year.append( file )
        sleeper.append( df.values[1][3] )

    for file in b_list:
        a = "/Users/irako/Desktop/nba_rookies/csvfiles/"
        csv_file = a + file[:-4] + ".csv"
        df=pd.read_csv(csv_file, sep=',',header=None)
        df.values
        year.append( file )
        sleeper.append( df.values[1][2] )


    g = []
    h = []
    m = []
    junk = []
    cities = ['Oklahoma City', 'Denver', 'Dallas',
              'San Antonio', 'Detroit', 'Milwaukee',
              'Miami', 'New York', 'Memphis', 'Charlotte',
              'New Jersey', 'Charlotte', 'Boston',
              'Orlando', 'Portland', 'Houston',
              'Indiana', 'Minnesota', 'L.A. Clippers',
              'Philadelphia', 'Chicago', 'Cleveland']

    for i in sleeper:
        j = (i.replace("'","").replace("[", "").replace("]", "")).split(",")
        for k in j:
          l = k.lstrip().rstrip()
          if l in cities:
              junk.append(l)
          else:
              h.append(l)
    return h

    for i in range(0, (len(h))):
        with open('sleeper1.csv', 'w') as csv_file:
            csv_app = csv.writer( csv_file )
            csv_app.writerow( h )

main()
