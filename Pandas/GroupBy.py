import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt

movies = pd.read_csv(r"D:\Coding Language\Python\DataSet\datasets-session-17\imdb-top-1000.csv")
print(movies.head(5))

# Group by - aap data k andar group form krta hai on the basis of some column. there are two types of column -: i) Numerical ii)Cateorogical
# Group by applied on catogorical column

genres = movies.groupby('Genre')
used_img1= cv2.imread(r"C:\Users\prana\OneDrive\Pictures\Screenshots\Screenshot 2026-07-12 095542.png")
plt.imshow(used_img1)
# plt.show()

# n fuctions Applying builtin aggregatioon groupby objects
mean1 = genres.mean(numeric_only=True) # like that we can apply sum,min,max and std etc
print(mean1)
print("\n")
print(genres.min()) # min is also applied on string so we do not need to do "numeric_value=True"




print("\n Q) find the genre with highest avg IMDB rating")

# find the genre with highest avg IMDB rating
movies.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False).head(1)

print("\n find director with most popularity ")
# find director with most popularity
movies.groupby('Director')['No_of_Votes'].sum().sort_values(ascending=False).head(1)

print("\nfind number of movies done by each actor")
# movies['Star1'].value_counts()
movies.groupby('Star1')['Series_Title'].count().sort_values(ascending=False)

# GroupBy Attributes and Methods
# find total number of groups -> len
# find items in each group -> size
# first()/last() -> nth item
# get_group -> vs filtering
# groups
# describe
# sample
# nunique

print("\n Total number of group = ")
print(len(movies.groupby('Genre'))) 
print(movies['Genre'].nunique())

print("\n Total number of rows in each group = ")
print(movies.groupby('Genre').size())
print(movies['Genre'].value_counts())


print("\n Nth movie or row in a group")
print(genres.first())
print(genres.last())
print(genres.nth(6))

print("\n Any specific genres of movie")
print(genres.get_group('Horror'))
print("\n")
print(movies[movies['Genre']=='Fantasy'])

print("\n Describe -> min,max,std..")
print(genres.describe())

print("\n sample -> Give random movies from each sample")
print(genres.sample(2,replace=True)) # give 2 random movies from each group. If they did not have two movie in group then "Make replace=True"

print("\n nunique() -> give unique values")
print(genres.nunique())

# agg method :-

# passing dict
print("\n agg method using dict -> apply different agg function on each column")
print(genres.agg(
    {
        'Runtime':'mean',
        'IMDB_Rating':'mean',
        'No_of_Votes':'sum',
        'Gross':'sum',
        'Metascore':'min'
    }
))

#passing list 
print("\n Apply agg func using list -> In this each column have min,max,mean,sum")
numeric_movies = movies.select_dtypes(include='number')
numeric = numeric_movies.groupby(movies['Genre'])
print(numeric.agg(['min','max','mean','sum']))


print("\n Adding both the syntax")
# Adding both the syntax
print(genres.agg(
    {
        'Runtime':['min','mean'],
        'IMDB_Rating':'mean',
        'No_of_Votes':['sum','max'],
        'Gross':'sum',
        'Metascore':'min'
    }
))

# looping on groups
# for group,data in genres:
#     print(type(group),end=" ") # here type of "group" = <class 'str'> and type of data is = <class 'pandas.core.frame.DataFrame'>
#     print(type(data))

print("\nfind the highest rated movie of each genre") # Here we use concat
df = pd.DataFrame(columns=movies.columns)
for group,data in genres:
  df = pd.concat([df,data[data['IMDB_Rating'] == data['IMDB_Rating'].max()]])
print(df)

# split (apply) combine
# apply -> builtin function
print(genres.apply(min)) # In apply we can provide our built in function but in agg we can't
# apply() combines all the returned groups into one final result before returning it.

print("\n find number of movies starting with A for each group")
def foo(group):
  return group['Series_Title'].str.startswith('A').sum()
print(genres.apply(foo))


print("\n find ranking of each movie in the group according to IMDB score")
def rank_movie(group):
  group['genre_rank'] = group['IMDB_Rating'].rank(ascending=False)
  return group
print(genres.apply(rank_movie))


print("\nfind normalized IMDB rating group wise")
def normal(group):
  group['norm_rating'] = (group['IMDB_Rating'] - group['IMDB_Rating'].min())/(group['IMDB_Rating'].max() - group['IMDB_Rating'].min())
  return group

genres.apply(normal)


print("\n groupby on multiple cols")
duo = movies.groupby(['Director','Star1'])

print("\nsize =",end=" ")
print(duo.size())
print("\nget_group") # It print the group with these combinations..
print(duo.get_group(('Aamir Khan','Amole Gupte')))


print("\nfind the most earning actor->director combo")
print(duo['Gross'].sum().sort_values(ascending=False).head(1))

print("\nfind the best(in-terms of metascore(avg)) actor->genre combo")
print(movies.groupby(['Star1','Genre'])['Metascore'].mean().reset_index().sort_values('Metascore',ascending=False).head(1)) # we do reset_index to convert multiIndex to one index


print("\n agg on multiple groupby")
numeric_multi=numeric_movies.groupby([movies['Director'],movies['Star1']])
print(numeric_multi.agg(['min','max','mean']))

# Using another dataset

ipl = pd.read_csv(r"D:\Coding Language\Python\DataSet\datasets-session-17\deliveries.csv")
print(ipl.head())
print("\n Shape of ipl =",ipl.shape)

print("\n Find the top 10 batsman in terms of runs")
print(ipl.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10))

print("\n Find the batsman with max no of sixes ")
print(ipl[ipl['batsman_runs']==6].groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1).index[0])