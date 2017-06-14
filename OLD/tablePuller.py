# tablePuller.py
# Scrapes, reads, and visualizes advanced data from the Spurs (or any team)
# Can intake any year or team and return tables into .csv format

# HTML Parser adapted and adjusted from: 
# http://srome.github.io/Parsing-HTML-Tables-in-Python-with-BeautifulSoup-and-pandas/

### 


import os
import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests


### User input ### 
 
team = 'NYK' # Set San Antonio as the default team

batch = False # Allows batch functions to be turned on (if True) or off (if False)

if batch == False: 
    
    year = '1990'
    url = 'http://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fteams%2F' + team + '%2F' + year + '.html&div=div_per_game'

    query(url)



### Set up the current directory as the home path ###

global dir_path, path
dir_path = os.path.dirname(os.path.realpath(__file__))
path = dir_path + '/per_game/'

### Required class for parsing ### 

class HTMLTableParser():

        def parse_url(self, url):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            return [(table['id'],self.parse_html_table(table))\
                    for table in soup.find_all("table")] 

        def parse_html_table(self, table):
            n_columns = 0
            n_rows = 0
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
            # df.to_csv(path + yr + '.csv')
            
            print(df)
            
            return df

### Query ### 
# Sets the URL and scrapes table data


def query(url): 
    # Calls the given url with BeautifulSoup
    response = requests.get(url)
    response.text[:100] 
    
    # Calls the HTMLTableParser with the given url
    hp = HTMLTableParser()
    table = hp.parse_url(url)[0][1] 
    table.head()
    

### Batch functions only ### 
# Functions below can call aggregate data (e.g. stats per game for SAS from 1999 to 2017)
if batch == True: 
    
    years = []
    for i in range(0, 19):
        year = str(1999 + i)
        years.append(year)
        
    
    urls = []
    for year in years: 
        # isloated url address for team's regular stats
        url = 'http://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fteams%2F' + team + '%2F' + year + '.html&div=div_per_game'
        urls.append(url)
        
        
    i = 0 
    for url in urls: 
        yr = years[i] # yr is only used for CSV file naming
        i+=1
        
        query(url)

        
