#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 11:25:47 2017

@author: irako

makeCSV.py
Makes a CSV out of parsed survey data 

"""
import sys
import csv

from surveyParse import parse
from surveyParse import headers

def main(): 
    return 
    
    
def create( survey_file ):
    key = headers( survey_file )
    data = parse( survey_file )
    
    output = survey_file[:-4] + ".csv"
    with open(output, 'w') as csv_file: 
        csv_app = csv.writer( csv_file )
        csv_app.writerow( key )
        csv_app.writerow( data )
    
if __name__ == '__main__':
    create(sys.argv[1])