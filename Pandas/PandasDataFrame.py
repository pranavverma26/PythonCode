import numpy as np
import pandas as pd

# If we have tabular form then this is know as dataframe. And one single column is series. Every single row
# is also a series.

# Creating DataFrame

# using lists
student_data = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
student1 = pd.DataFrame(student_data,columns=['iq','marks','package'])
print(student1)

# uxing dicts
student_dict = {
    'name':['nitish','aknkit','rupesh','rishabh','amit','ankita'],
    'iq': [100,90,120,80,0,0],
    'marks':[80,70,100,50,0,0],
    'package':[10,7,14,2,0,0]
}

student2 = pd.DataFrame(student_dict)
student2.set_index('name',inplace=True)
print(student2)


movies = pd.read_csv("D:\Coding Language\Python\DataSet\datasets-session-17\movies.csv")
print(movies)
print()

ipl_match = pd.read_csv("D:\Coding Language\Python\DataSet\datasets-session-17\ipl-matches.csv")
print(ipl_match)

# shape = to know how many rows and columns have
print("Movies shape =",movies.shape)
print("ipl shape =",ipl_match.shape)

# dtype
print("DataType of movies =",movies.dtypes)

# index
print("Index of movies =",movies.index)

# column = Fetch all the columns of data frame
print(" Column of dataframes movies = ")
print(movies.columns)

# values = fetch all the values of datatframe
print("Values of movie dataframe")
print(movies.values,end="\n\n")
print("Values of ipl dataframe")
print(ipl_match.values)

print("head and tail : head = give first 5 matches and tail give last 5 matches")
print(movies.head())
print(movies.tail())

print("\n sample = randomly gives samples")
print(ipl_match.sample())

print("\n info =  Gives high level information about your dataframe")
print(movies.info())

print("\n describe gives mean,std,min..etc on numerical values only")
print(movies.describe())

print("\n isnull value present in function")
print(movies.isnull())
print("Columns total number of missing value =",movies.isnull().sum())

print("\n duplicated values =")
print(student2.duplicated().sum())

print("\n rename = rename column name,temproaily for permanent inplace = True")
student2.rename(columns={'marks':'percent','package':'lpa'},inplace=True)
print(student2)


# Math Methods

print("\n sum -> it apply sum on all column")
print(student1.sum())
print("To apply on rows")
print(student1.sum(axis=1))

print("\n We can also apply mean,median,mode,std on both row and column axis =0 column wise (default) ans axis =1 row-wise")

print("\n selecting cols from a DataFrame")
print(movies['title_x']) # Its type is series

print("\nFetching multiple columns")
print(movies[['title_x','year_of_release','actors']])

print("\n Selecting rows from a DataFrame")
print("iloc = searches using index positions")
print("loc = searches using index labels")
print(movies.iloc[0]) # gives 1st row
# fetching multiple rows
print("\n")
print(movies.iloc[0:5])
print("\n")
print(movies[0:5:2])

# we can also use fancy indexing
# The differnce between iloc and loc is that in iloc in range last one is excluded but in loc
# last one is included.
print(movies.iloc[[0,4,5]])
print("\n")
print(student2.loc['nitish':'rishabh'])
# we can apply iloc in student2 apart from we provide student2 a index but it also have default index


print("\n Selecting both rows and column")
print(movies.iloc[0:3,0:3])
print("\nUsing Loc")
print(movies.loc[0:2,'title_x':'poster_path'])

print("\n Filtering DataFrame")

print("\n Find all the winners")
print(ipl_match.columns)
finalMatch= ipl_match['MatchNumber']=='Final'
print(ipl_match[finalMatch])
Teams = ipl_match[finalMatch]
# print(Teams[['Season','Team1','Team2','WinningTeam']])

# Above one in one line
print(ipl_match[ipl_match['MatchNumber']=='Final'][['Season','Team1','Team2','WinningTeam']])

print("\n How many super over finishes have occured =",end=" ")
print((ipl_match['SuperOver']=='Y').sum())
print(ipl_match[ipl_match['SuperOver']=='Y'].shape[0])

print("\n How many matches has csk won in kolkata =",end=" ")
print(ipl_match[(ipl_match['WinningTeam']=='Chennai Super Kings') & (ipl_match['City']=='Kolkata')].shape[0])

toss_win = (ipl_match['TossWinner'] == ipl_match['WinningTeam']).sum()
Tota_Toss = ipl_match.shape[0]
print("\n Toss winner is match winner in percentage =",end=" ")
print((toss_win/Tota_Toss)*100,end="\n\n")

print(movies.columns)
print("\n movies with rating higher than 8 and votes>10000")

print(movies[(movies['imdb_rating']>8) & (movies['imdb_votes']>10000)][['title_x','release_date',]])

print("\n Action movies with rating higher than 7.5")
