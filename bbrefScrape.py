# bbrefScrape.py

# Returns individual 'sleepers' from the sleeper() function in dataClean.py
# Queries sleepers from basketball-reference.com; opens individual tabs in Chrome
# Scrapes statistical data on individual players (e.g. James Harden)
# Saves each player's stats into "/bbref_exports/[name].csv"
# Allows for data manipulation using pandas

# Uses Selenium, BeautifulSoup, and pandas
# HTML Parser adapted from:
# http://srome.github.io/Parsing-HTML-Tables-in-Python-with-BeautifulSoup-and-pandas/

from dataClean import sleeper

# for Selenium
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# for BeautifulSoup
import pandas as pd
from bs4 import BeautifulSoup
import requests


### Sets up the HTMLTableParser for BeautifulSoup

class HTMLTableParser():

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
            
            print (df)
            return df


def scrape():

### Uses Selenium to open each player's profile page on
### basketball-reference.com on an individual tab

    executable_path = "/Users/irako/Desktop/nba_rookies/chromedriver"
    os.environ["webdriver.chrome.driver"] = executable_path

    chrome_options = Options()
    chrome_options.add_extension("/Users/irako/Desktop/nba_rookies/adb.crx")
    chrome_options.add_extension("/Users/irako/Desktop/nba_rookies/vim.crx")

    driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)

    for i in sleeper():
        driver.get('http://www.basketball-reference.com/');
        search_box = driver.find_element_by_name('search')
        search_box.send_keys(i + Keys.ARROW_DOWN + Keys.RETURN)


        url = driver.current_url
        print( "Player name: " + i + "\nURL: " + url ) # prints the current URL


        # creates the folder 'bbref_exports'; creates a path for
        # scraped data from basketball-reference (.csv) to be exported
        newfolder = r'bbref_exports'
        if not os.path.exists(newfolder):
            os.makedirs(newfolder)
        global path
        path = newfolder + '/' + i + ".csv"

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

scrape()
