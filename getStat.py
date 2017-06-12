# getStat.py

# Finds multiple statistics on a webpage: 
    # PER 
    # Win Share
    # Draft position

# Usage: 
# function(playdict['player name'])
# per(playdict['James Harden'])

from dataClean import sleeper
from lxml import html
from bs4 import BeautifulSoup
import requests
import csv


# Create a dictionary containing players and their urls

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

            
def per(url): 
    page = requests.get(url)
    tree = html.fromstring(page.content)
    per = tree.xpath("/html/body/div/div/div[@class='stats_pullout']/div[@class='p3']/div[1]/p[2]/text()")   
    return per


def winShare(url): 
    page = requests.get(url)
    tree = html.fromstring(page.content)
    winShare = tree.xpath("/html/body/div/div/div[@class='stats_pullout']/div[@class='p3']/div[2]/p[2]/text()")   
    return winShare

def draft(url): 
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml').get_text()
    start = soup.find("Draft:")
    end = soup.find("overall)")
    draft = (soup[start:end] + "overall)")[7:]
    return draft

    # pattern = 'Draft+[\w\s\:(),]+overall'
    # did not end up using regex 
    
    
