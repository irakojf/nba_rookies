# getStat.py

# Finds multiple statistics for individual players: 
    # PER 
    # Win Share
    # Draft position
    
# Also supports team and league stats

# Usage: 
# function(playdict['player name'])
# current_per(playdict['James Harden'])

from dataClean import sleeper
from lxml import html
from bs4 import BeautifulSoup

import requests
import csv
import os 
import pandas as pd
import numpy as np 
import requests


### Set up ###

dir_path = os.path.dirname(os.path.realpath(__file__))
exports_path = dir_path + '/bbref_exports/'

urls = []
with open('url.csv', newline='') as f:
    reader = csv.reader(f)
    for i in reader:
        for j in i: 
            urls.append(j)
    
players = []
for k in sleeper(): 
    players.append(k)

global playdict
playdict = dict(zip(players, urls))

### Functions ###

def current_per(url): 
    page = requests.get(url)
    tree = html.fromstring(page.content)
    current_per = tree.xpath("/html/body/div/div/div[@class='stats_pullout']/div[@class='p3']/div[1]/p[2]/text()")   
    print (current_per)
    return current_per


def winShare(url): 
    page = requests.get(url)
    tree = html.fromstring(page.content)
    winShare = tree.xpath("/html/body/div/div/div[@class='stats_pullout']/div[@class='p3']/div[2]/p[2]/text()")   
    print (winShare)
    return winShare

def draft(url): 
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml').get_text()
    start = soup.find("Draft:")
    end = soup.find("overall)")
    draft = (soup[start:end] + "overall)")[7:]
    print (draft)
    return draft

    # pattern = 'Draft+[\w\s\:(),]+overall'
    # did not end up using regex 
    
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

def factor(season): 
    a = LeagueStat(season)    
    lg_AST = a.get('AST')
    lg_FG = a.get('FG%')
    lg_FT = a.get('FT%')

    factor = 2/3 - ((0.5 * lg_AST / lg_FG) / (2 * lg_FG / lg_FT))
    return factor

def team_stat(season, team, stat): 
    acronyms = ['ATL', 'BKN', 'BOS', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 
                'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 
                'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHX', 
                'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']

    if team not in acronyms:
        raise Exception("Invalid team name")
    
    acronym = team 
    
    url = 'http://www.basketball-reference.com/teams/' + acronym
    response = requests.get(url)
    response.text[:100] # Access the HTML with the text property

    a = TeamParser()
    team_data = a.parse_url(url)[0][1]
    team_data.head() 

    team_stat = (team_data.loc[team_data['Season'] == season, stat].iloc[0])
    return team_stat

class LeagueStat(object): 
    
    def __init__(self, season): 
        self.season = season
        
    def get(self, stat): 
        df = pd.read_csv(dir_path + '/data/' + 'leagueAvgs.csv', 
                         usecols = [ 'Season' , stat ]
                         )
        out = df.loc[df['Season'] == self.season, stat].iloc[0].astype(float)
        return out


class TeamParser():

        def parse_url(self, url):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            return [(table['id'],self.parse_html_table(table))\
                    for table in soup.find_all('table')]

        def parse_html_table(self, table):
            n_columns = 0
            n_rows=0
            column_names = []

            # Find number of rows and columns
            # we also find the column titles if we can
            for row in table.find_all('tr'):

                # Determine the number of rows in the table
                td_tags = row.find_all('td') + row.find_all('th')
                if len(td_tags) > 0:
                    n_rows+=1
                    if n_columns == 0:
                        # Set the number of columns for our table
                        n_columns = len(td_tags)

                # Handle column names if we find them
                th_tags = row.find_all('th')
                if len(th_tags) > 0 and len(column_names) == 0:
                    for th in th_tags:
#                        if th.get_text() != 'Season':
                            column_names.append(th.get_text())

            # Safeguard on Column Titles
            if len(column_names) > 0 and len(column_names) != n_columns:
                #raise Exception("Column titles do not match the number of columns")
                print( 'Exception raised!')

            columns = column_names if len(column_names) > 0 else range(0,n_columns)
            df = pd.DataFrame(columns = columns,
                              index= range(0,n_rows))
            row_marker = 0
            for row in table.find_all('tr'):
                column_marker = 0
                columns = row.find_all(['td', 'th']) 
                for column in columns:
                    df.iat[(row_marker),(column_marker)] = column.get_text()
                    column_marker += 1
                if len(columns) > 0:
                    row_marker += 1

            # Convert to float if possible
            for col in df:
                try:
                    df[col] = df[col].astype(float)
                except ValueError:
                    pass

            # remove the first row from df 
            # the header is duplicated because we included 'th' in row 74
            df = df.iloc[1:]

            # creates a .csv file out of Dataframe
            # df.to_csv(path)
            return df
