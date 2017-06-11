# surveyParse.py

# Reads survey.txt files and parses data into lists


import re
import itertools

def main():
    return

def read_all():
    # executes all possible survey files into the parse(function)

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
        parse(file_name)

def headers(file_name):
    # accepts a survey file and returns an array containing the
    # survey questions

    file = open( file_name, "r" )
    global lines
    lines = file.readlines()
    file.close()

    headers = []
    for line in lines:
        line = line.rstrip( '\n' )
        phrase = "Which rookie "
        if line.find( phrase )!= -1:
            headers.append( line )
    return headers


def parse(file_name):
    # accepts a survey file and returns an array of arrays
    # containing just the player responses only

    file = open( file_name, "r" )
    global lines
    lines = file.readlines()
    file.close()

    responses = []
    for line in lines:
        line = line.rstrip( '\n' )
        phrase = "Which rookie "
        if line.find( phrase )!= -1:
            responses.append( "SPLIT" )

        ans = line.splitlines()
        for an in ans:
            if an.find( "%" )!= -1 or an.find( "percent" )!=-1 :
                responses.append( an )

    players = []
    for response in responses:
        if response.find("SPLIT")!= -1:
            players.append( response )
        pattern = '[a-zA-Z"\']* [. [\, [a-zA-Z]*'
        match = re.search(pattern, response)
        re.match(pattern, response)

        # checks each line for the player pattern using Regex
        # if the line contains "Last", skip the line
        if match and ( response.find( "Last " )== -1 ):
            new_line = match.group()
            players.append(new_line)

    # uses itertools and splits the responses to question into its own array
    keyword = "SPLIT"
    spl = [list(y) for x, y in itertools.groupby(players, lambda z: z == keyword) if not x]

    return spl


main()
