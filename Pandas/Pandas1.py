# What is Pandas
# Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
# built on top of the Python programming language.

# Pandas Series
# A Pandas Series is like a column in a table. It is a 1-D array holding data of any type
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# string

# # series k andar doa cheeja hoti hai index and value
# country = ['India','Pakistan','USA','Nepal','Srilanka']
# s = pd.Series(country)
# print("First thing in panda")
# print(s)

# runs = [13,24,56,78,100]
# player = ["Padikal","Virat","Rajat","Iyer","Tim"]
# #print(pd.Series(runs,index=player,name="Players Run"))

# # # Series from dict

# run2 = {
#     'Padikal': 13,
#     'Virat': 24,
#     'Rajat': 56,
#     'Iyer':  78,
#     'Tim':100
# }
# series1= pd.Series(run2,name="RCB SCORECARD")
# print(series1)

# # # Series Attributes
# # # size = tells how much value does series have
# print("Series size =",series1.size)
# # #name = tells the name of series
# print("Name of series =",series1.name)
# # # is_unique = tells all items are unique or not 
# print(series1.is_unique)

# # # index = give index name
# print("Series index =",series1.index)
# # # values
# print("Values =",series1.values)

# # Series using real world data sets
subs = pd.read_csv("D:\Coding Language\DataSet\datasets-session-16\subs.csv").squeeze("columns")
print(subs)
kohli_iplRuns = pd.read_csv("D:\Coding Language\DataSet\datasets-session-16\kohli_ipl.csv",index_col='match_no').squeeze("columns")
print(kohli_iplRuns)

BollyWood_Movie = pd.read_csv(r"D:\Coding Language\DataSet\datasets-session-16\bollywood.csv",index_col='movie').squeeze("columns")
print(BollyWood_Movie)

# # Head = by default gives 5 series of top.
# # Tail = gives by default of last 5
print("Topic is Head : ")
print(subs.head())

# # sample = give randomly one row
print("Sample")
print(BollyWood_Movie.sample(10))

# # Value counts
print("Value : gives frequency")
# # Let we have nikalna hai ki har actor na kitni movie ki hai
# print(BollyWood_Movie.value_counts())
# #Sort value
print("Sort Values : It will do temproriy changes") # for permanent change kohli_iplRuns(inplace=True)
print(kohli_iplRuns.sort_values(ascending=False).head(1).values[0]) # we not use .values[0] o/p = 128 113

# # Sort_index
# Without inplace=True (returns a new sorted object) 
print("Sort_index")
print(BollyWood_Movie.sort_index(inplace=True))

# # count = gives total number of values present in the series and non missig values.
# print("Count")
# print(kohli_iplRuns.count())
# print(BollyWood_Movie.count())

# # Sum and Product
# print("Sum and Product")
# print(subs.sum())
# print(subs.prod())

# # Mean,Median,Mode, Std,Var
# print("Mean/Median/Mode/Std/Var")
# print(subs.mean())
# print(kohli_iplRuns.median())
# print(subs.std())
# print(kohli_iplRuns.var())

# # Min/Max
# print("Min/Max")
# print(subs.min())
# print(subs.max())

# # Describe = Gives count,mean,std.min..etc in one code
# print("Describe")
# print(kohli_iplRuns.describe())

# # Series Indexing
print("Integer Indexing")
# print(kohli_iplRuns[0]) It will give error because it have index label so we do :-
print(kohli_iplRuns.iloc[0])
x = pd.Series([12,13,14,35,46,57,58,79,9])
print(x[0])
print(x[3]) 
# # here negative indexing does not work if the indexes are string then it will work

# # Slicing :- It work like python
# print("slicing")
# print(kohli_iplRuns[5:16]) 

# # Fancy indexing
# print("Fancy indexing")
# print(kohli_iplRuns[[1,3,4,5]])
# print("Label Indexing")
# print(BollyWood_Movie["2 States (2014 film)"])

# print("Editing Series")
# # Using indexing or label
# series1['Virat'] =100
# print(series1)
# print("What if an index does not exist ?")
# # it will add that index in series.
# print("Use slicing")
# series1[2:4]=[68,69]
# print(series1)
# print("Using fancy indexing")
# series1[[0,3,4]]=[0,0,1]
# print(series1)

# # Series with python functionalities
# print("Series with python functionalities")
# # len/type/dir/sorted/max/min
# print(len(subs))
# print(type(subs)) # it's type is series
# print(dir(subs))
# print(sorted(subs)) # output is inside the list
# print(min(subs))
# print(max(subs))

# # Type Conversion
# print("Type Conversion")
# print(dict(series1))

# # Membership operators
# print("Membership operators")
# print('2 States (2014 film)' in BollyWood_Movie) # It works only on indexes

# # For values 
# print('Alia Bhatt' in BollyWood_Movie.values)

# # Looping 
# print("Looping") # It work on values
# for i in BollyWood_Movie:
#     print(i)

# # To work on Index
# # for i in BollyWood_Movie.index:
# #     print(i)

# # Arithmetic Operators
# print("Arithmetic Operators") # Its a good example of broadcasting
# print(100-series1)

# # Relational Operators
print("Relational Opeartors3")
print(kohli_iplRuns>=50)

# print("Boolean indexing on Series")
# # Find no of 50's and 100's scored by kohli
# print(kohli_iplRuns[kohli_iplRuns>=50].size)

# print("Find number of ducks")
# print(kohli_iplRuns[kohli_iplRuns==0].size)
# print("Find actors who have done more than 20 movies")
# num_movies = BollyWood_Movie.value_counts()
# print(num_movies[num_movies>20])

print("Plotting Graphs using series")
subs.plot()
plt.show()

# num_movies2 = BollyWood_Movie.value_counts().head(20)
# num_movies2.plot(kind='bar')
# plt.show()