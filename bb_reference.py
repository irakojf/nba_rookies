#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 22:21:47 2017

@author: irako
"""
from NBA import sleeper

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

    body = driver.find_element_by_tag_name('body')
    body.send_keys('t' + 'K')
    driver.switch_to_window(driver.window_handles[-1])

    print(i)
    print(url)
