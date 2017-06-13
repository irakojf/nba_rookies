# visualize.py

###

from tablePuller import *
import pandas as pd


dir_path = os.path.dirname(os.path.realpath(__file__))

def get_df(name, statgroup, groupby=''): 
    # groupby: ['Big Men', 'Guards', 'PG', 'SG' ... 'C']
    # statgroup: advanced or per_game
    path = dir_path + '/' + statgroup + '_exports/' + groupby + '/' + name + '.csv'
    df = pd.read_csv(path)
    df = df.fillna(0.0) # replaces all NaN with 0.0
    return df


def plot(name, statgroup, stat, perchange, groupby=''):
# Plots a time series of a particular stat's change over time where
# Also returns the time series 
    if perchange == True: 
        title = ( stat + ' % change over time for ' + name )
        print(title)
        df = get_df(name, statgroup, groupby) 
        # only output the 'Season' , 'Tm' and 'PER' columns
        df2 = df[['Season', 'Tm', stat]] 
        
        # find the index of the 'Career' value
        # since the index outputs as numpy [4], convert into a list
        # loop through the list and set b equal to index value
        a = list(df2.loc[df2['Season'] == 'Career'].index)
        for i in a: 
            b = i
        df2 = df2[:b]
        df3 = df2[stat]  
        
        
        # Y-Axis
        yaxis = []
        for i in df3[1:]: 
            yaxis.append(float(i))
        yaxis.append(0.0)
        yaxis = (yaxis - df3)[:-1] # remove the last object in the list
        yaxis = pd.Series(yaxis, name='%change')
        #print(yaxis)
        
        
        # X-Axis
        xaxis = []
        for i in df2['Season'][1:]: 
            xaxis.append(i)
        xaxis = pd.Series(xaxis, name='Year to year')
        #print(xaxis)
        
        table = pd.concat([xaxis, yaxis], axis=1)
        out = df2.join([xaxis, yaxis])
        table.plot(x=xaxis)
        plt.legend([name], title=title)
        print(out)
        return out
    
    else:
        title = ( stat + ' over time for ' + name )
        print(title)
        df = get_df(name, statgroup, groupby) 
        df2 = df[['Season', 'Tm', stat]] # only output the 'Season' and 'PER' columns
        
        # find the index of the 'Career' value
        # since the index outputs as numpy [4], convert into a list
        # loop through the list and set b equal to index value
        a = list(df2.loc[df2['Season'] == 'Career'].index)
        for i in a: 
            b = i
        df2 = df2[:b]
        df3 = df2[stat]  
        
        # Y-Axis
        yaxis = pd.Series(df3)
        
        # X-Axis
        xaxis = []
        for i in df2['Season']: 
            xaxis.append(i)
        xaxis = pd.Series(xaxis, name='Season')
        #print(xaxis)
        
        table = pd.concat([xaxis, yaxis], axis=1)
        print(df2)
        table.plot(x=xaxis)
        plt.legend([name], title=title)
        return df2

def c_overtime_avgline(name, statgroup, stat, perchange, groupby=''): 
    title = ( stat + ' % change over time for ' + name )
    print(title)
    df = get_df(name, statgroup, groupby) 
    # only output the 'Season' , 'Tm' and 'PER' columns
    df2 = df[['Season', 'Tm', stat]] 
    
    # find the index of the 'Career' value
    # since the index outputs as numpy [4], convert into a list
    # loop through the list and set b equal to index value
    a = list(df2.loc[df2['Season'] == 'Career'].index)
    for i in a: 
        b = i
    df2 = df2[:b]
    df3 = df2[stat]  
        
        
    # Y-Axis
    yaxis = []
    for i in df3[1:]: 
        yaxis.append(float(i))
    yaxis.append(0.0)
    yaxis = (yaxis - df3)[:-1] # remove the last object in the list
    yaxis = pd.Series(yaxis, name='%change')
    
    avg = float((sum(yaxis)/len(yaxis)))
    average = []
    for i in yaxis: 
        average.append(avg)
    average = pd.Series(average, name=('Average' + stat))
    print(yaxis)
        
        
    # X-Axis
    xaxis = []
    for i in df2['Season'][1:]: 
        xaxis.append(i)
    xaxis = pd.Series(xaxis, name='Year to year')
    #print(xaxis)
    
    table = pd.concat([xaxis, yaxis, average], axis=1)
    out = df2.join([xaxis, yaxis])
    table.plot(x=xaxis)
    plt.legend([name], title=title)
    






