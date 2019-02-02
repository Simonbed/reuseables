##### These are some templates that I use when writing a new code
##### Some of these are very helpful depending on what we need
#####
##### I don't take ownership of these codes as some have been taken and modified from other sources while some are mine



### To find the current repository -- If I don't know
import os
direct = os.getcwd()
print(direct)


### This code prints a pd dataframe full without the "..." when it's too long
import pandas as pd
def print_full(x):
    pd.set_option('display.max_rows', len(x))
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', -1)
    print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.float_format')
    pd.reset_option('display.max_colwidth')

### Converting DICTIONARY to PANDAS SERIES
dictionary1 = dict() ##Could have made the dictionary an easier way : dictionary1 = dict({"a":400, "b":200, "c":300})
dictionary1.update({"a":100})
dictionary1.update({'b':200})
dictionary1.update({'c':300})
dictionary1.update({'d':400})
dictionary1.update({'e':800}) ### THIS MADE THE DICTIONARY
dictSerie = pd.Series(dictionary1) ### THIS IS THE ONLY CONVERTION lline

### Converting PANDAS DATAFRAME into List of lists
dataLines = list()
for i in range(0, 7501):
    dataLines.append([str(pandas_Dataframe.values[i,j]) for j in range(0,20)])

### Cleaning data using regular expressions
import re

states = ["        Amsterdam   ", "Aladin!!!", " !Mulan", "Tristana                 ", "ObJeCtif!", "****Gros Balou   ", "=========West Germany??  ", "____Slovenia!!", "West Virginia!", "Bikini Bottom"]
def remove_functions(strp):
    return re.sub("[!#?_=*]", '', strp) ### This doesnt work for if there is "-"

ooops = [str.strip, remove_functions, str.title]

def clean_data(oops, funky):
    result = list()
    for data in oops:
        for fun in funky:
            data = fun(data) #applies every function in OOOPS to the oops list
        result.append(data)
    return(result)

cleaned_data = clean_data(states, ooops)
print(cleaned_data) ## The data becomes clean

#### Cleaning data (lists) by removing certain item from the list
### Removing the "BadItem" strings (couls be other values) that are in the data
cleanData = list()
for line in linesOfData:  ##We will use the first data to create cleaned data
    templine = list()
    for item in line:
        if item != 'BadItem':
            templine.append(item)
        else:continue
    cleanData.append(templine)


#### For printing a certain value based on a key in a key,Value item (dict)
for key, value in dictionary.items() :
    if key == "02-2015" :
        print("For the KEY you requested ( %s ), the requested VALUE IS %f" %(key, value))
    else :
       continue
