# tablePuller.py
# Scrapes, reads, and visualizes advanced data from the Spurs (or any team)
# Can intake any year or team and return tables into .csv format

# HTML Parser adapted and adjusted from: 
# http://srome.github.io/Parsing-HTML-Tables-in-Python-with-BeautifulSoup-and-pandas/


# Available functions: 
    # query(url)
    # batch(team)

### 


import os
import csv
import re
import pandas as pd
import requests
import matplotlib.pyplot as plt
plt.style.use('ggplot')

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup



def main(): 
    scrape(['Lebron James'], 'advanced')


### Set up the current directory as the home path ###

global dir_path, path
dir_path = os.path.dirname(os.path.realpath(__file__))

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
                    df.iloc[(row_marker),(column_marker)] = column.get_text()
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
            # df = df.iloc[1:]

            # creates a .csv file out of Dataframe
            df.iloc[1:].to_csv(path)
            
            # print(df.iloc[1:])
            
            return df

### Query ### 
# Sets the URL and scrapes table data


def team_query( team='SAS', year='1990', div_name = 'advanced' ): 
        
    url = 'http://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fteams%2F' + team + '%2F' + year + '.html&div=div_' + div_name
    
    # Calls the given url with BeautifulSoup
    response = requests.get(url)
    response.text[:100] 
    
    # Calls the HTMLTableParser with the given url
    hp = HTMLTableParser()
    table = hp.parse_url(url)[0][1] 
    table.head()
    
    return table

def scrape(players, div):
### Takes an array of players
### Uses Selenium to open each player's profile page on
### basketball-reference.com on an individual tab

    executable_path = dir_path + "/chromedriver"
    os.environ["webdriver.chrome.driver"] = executable_path

    chrome_options = Options()
    chrome_options.add_extension(dir_path + "/adb.crx")
    chrome_options.add_extension(dir_path + "/vim.crx")

    driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)

    for player in players: 
        print(player)
        driver.get('http://www.basketball-reference.com/');
        search_box = driver.find_element_by_name('search')
        search_box.send_keys(player + Keys.ARROW_DOWN + Keys.RETURN)

        b_url = driver.current_url
        
        # pulls the player id from the current url 
        # e.g. Carmelo Anthony : anthoca01
        # then changes the url from in browser url to the user-specified url
        pattern = "[a-zA-Z0-9_.-]*.html"
        m = re.search(pattern, str(b_url)).group(0)
        player_id = m[:-5]
        first_letter = m[:1]
        # print(player_id)
        
        url = 'http://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fplayers%2F' + first_letter + '%2F' + player_id + '.html&div=div_' + div
        # print(url)
        
        # creates the folder 'bbref_exports'; creates a path for
        # scraped data from basketball-reference (.csv) to be exported
        
        newfolder = str(div + '_exports')
        if not os.path.exists(newfolder):
            os.makedirs(newfolder)
        global path
        path = newfolder + '/' + player + ".csv"

        # BeautifulSoup
        response = requests.get(url)
        response.text[:100] # Access the HTML with the text property

        hp = HTMLTableParser()
        table = hp.parse_url(url)[0][1] # Grabbing the table from the tuple
        table.head()


        # Creates and switches to new tab using vimium,
        # Selenium switches the driver to the newly created tab
        body = driver.find_element_by_tag_name('body')
        body.send_keys('t' + 'K')
        driver.switch_to_window(driver.window_handles[-1])
    
        print(table.iloc[1:])
        
    driver.quit()
    
    return table.iloc[1:]
    
def draft(players, div): 
    # Takes an array of players and returns a player's draft position
    
    executable_path = dir_path + "/chromedriver"
    os.environ["webdriver.chrome.driver"] = executable_path

    chrome_options = Options()
    chrome_options.add_extension(dir_path + "/adb.crx")
    chrome_options.add_extension(dir_path + "/vim.crx")

    driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)

    for player in players: 
        print(player)
        driver.get('http://www.basketball-reference.com/');
        search_box = driver.find_element_by_name('search')
        search_box.send_keys(player + Keys.ARROW_DOWN + Keys.RETURN)

        b_url = driver.current_url
        
        # pulls the player id from the current url 
        # e.g. Carmelo Anthony : anthoca01
        # then changes the url from in browser url to the user-specified url
        pattern = "[a-zA-Z0-9_.-]*.html"
        m = re.search(pattern, str(b_url)).group(0)
        player_id = m[:-5]
        first_letter = m[:1]
        # print(player_id)
        
        url = 'http://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fplayers%2F' + first_letter + '%2F' + player_id + '.html&div=div_' + div
        # print(url)

        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml').get_text()
        start = soup.find("Draft:")
        end = soup.find("overall)")
        draft = (soup[start:end] + "overall)")[7:]
        
    if "overall" not in draft: 
        print ('Undrafted')
    else: 
        print (draft)
    
    return draft        

if __name__ == '__main__':
    main()
