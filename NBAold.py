# -*- coding: utf-8 -*- 

""" 
    Sample basketball players 
    1. Top 5 rookies in each season 
    2. Optional: Narrow down to rookies that were picked after 
        the first 10 selections (sleeper picks)
    3. Sort by position, years played in college, team 
        performance of team (indicated by seeding at end of season), 
        position on depth chart, minutes played 
""" 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('max_columns', 50)
#%matplotlib inline

