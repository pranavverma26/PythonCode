# What is Pandas
# Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
# built on top of the Python programming language.

# Pandas Series
# A Pandas Series is like a column in a table. It is a 1-D array holding data of any type
import numpy as np
import pandas as pd

# string

# series k andar doa cheeja hoti hai index and value
country = ['India','Pakistan','USA','Nepal','Srilanka']
s = pd.Series(country)
print(s)

runs = [13,24,56,78,100]
player = ["Padikal","Virat","Rajat","Iyer","Tim"]
print(pd.Series(runs,index=player,name="Players Run"))

# Series from dict

run2 = {
    'Padikal': 13,
    'Virat': 24,
    'Rajat': 56,
    'Iyer':  78,
    'Tim':100
}
series1= pd.Series(run2,name="RCB SCORECARD")


# Series Attributes
# sizes = tells how much value does series have
print("Series size =",series1.size)
#name = tells the name of series
print("Name of series =",series1.name)
# is_unique = tells all items are unique or not 
print(series1.is_unique)

# index = give index name
print("Series index =",series1.index)
# values
print("Values =",series1.values)

# Series us(ing real world data sets
subs = pd.read_csv("D:\Coding Language\DataSet\datasets-session-16\subs.csv").squeeze("columns")
print(subs)
kohli_iplRuns = pd.read_csv("D:\Coding Language\DataSet\datasets-session-16\kohli_ipl.csv",index_col='match_no').squeeze("columns")
print(kohli_iplRuns)

BollyWood_Movie = pd.read_csv(r"D:\Coding Language\DataSet\datasets-session-16\bollywood.csv",index_col='movie').squeeze("columns")
print(BollyWood_Movie)
