#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 22:21:47 2017

@author: irako
"""
from NBA import sleeper

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
from selenium import webdriver
for i in sleeper(): 
    driver = webdriver.Chrome('/Users/irako/Desktop/nba_rookies/chromedriver')  # Optional argument, if not specified will search path.
    driver.get('http://www.basketball-reference.com/');
    search_box = driver.find_element_by_name('search')
    search_box.send_keys(i + Keys.ARROW_DOWN + Keys.RETURN)
    driver.quit()




    
