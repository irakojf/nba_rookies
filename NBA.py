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

from makeCSV import create

def main(): 
    file_list = ['s0809.txt', 
             's0910.txt',
             's1011.txt',
             's1112.txt',
             's1213.txt',
             's1314.txt',
             's1415.txt',
             's1516.txt',
             's1617.txt']
    for file in file_list: 
        create(file)
        

main()