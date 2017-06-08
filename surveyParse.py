#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 12:25:50 2017
@author: irako

surveyParse.py 
Reads text files and parses for player names. 

"""
import re

def main(): 
    return
    
def read_all(): 
    survey_files = ['s0809.txt', 
             's0910.txt',
             's1011.txt',
             's1112.txt',
             's1213.txt',
             's1314.txt',
             's1415.txt',
             's1516.txt',
             's1617.txt']
    for survey_file in survey_files: 
        global file_name
        file_name = survey_file
        file = open( survey_file, "r" )
        global lines 
        lines = file.readlines()
        file.close() 
        format()

def format(file_name):
    # reads the file 

    file = open( file_name, "r" )
    global lines 
    lines = file.readlines()
    file.close() 
    
    
    
    # places the survey questions into an array called players
    headers = []
    results = []
    for line in lines:
        line = line.rstrip( '\n' )
        phrase = "Which rookie "
        if line.find( phrase )!= -1: 
            headers.append( line )
            results.append( line ) 
            
        responses = line.splitlines()
        for response in responses: 
            if response.find( "%" )!= -1: 
                results.append( response )
    
    # checks each line for the player pattern using Regex 
    # if the line contains "Last", skip the line
    players = []
    for result in results: 
        pattern = '[a-zA-Z]* [a-zA-Z]* [\, [a-zA-Z]*' 
        match = re.search(pattern, result)
        re.match(pattern, result) 
        if match and ( result.find( "Last" )== -1 ): 
            new_line = match.group()
            players.append(new_line)  
    survey = { file_name : players }
    return survey
                
                

    
    

    
        
        
    


             
                

    
main()