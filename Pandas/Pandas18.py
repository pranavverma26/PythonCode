import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("\n value_counts :- series and dataframe")

# Series :- value_count is more useful in series
a = pd.Series([1,1,1,2,2,3])
print(a.value_counts())
# DataFrame
marks = pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14]
])
print(marks.value_counts())


ipl_match = pd.read_csv("D:\Coding Language\Python\DataSet\datasets-session-17\ipl-matches.csv")
print(ipl_match.columns)
print("\n Find which player has won most potm -> in finals and qualifiers")
print(ipl_match[~ipl_match['MatchNumber'].str.isdigit()][['Player_of_Match']].value_counts())

print("\n Toss decision plot")
ipl_match['TossDecision'].value_counts().plot(kind='pie')
# plt.show()

print("\n How many matches each team has played")
print((ipl_match['Team1'].value_counts() + ipl_match['Team2'].value_counts()).sort_values(ascending=True))

print("\n sort_values(series and dataframe) -> ascending -> na_position -> inplace -> multiple cols")
movies = pd.read_csv("D:\Coding Language\Python\DataSet\datasets-session-17\movies.csv")
print(movies.sort_values('title_x',ascending=True),end="\n\n")

print("By default sort values put missing values at the end")
students = pd.DataFrame(
    {
        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],
        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]

    }
)
# print(students)
print(students.sort_values('name',na_position='first',ascending=False))

print("\n sort two columns one by one")
print(movies.sort_values(['year_of_release','title_x'],ascending=[True,False]))


print("\n Rank is only applicable on series")
batsman = pd.read_csv(r"D:\Coding Language\Python\DataSet\datasets-session-17\batsman_runs_ipl.csv")
print(batsman)
batsman['batting_rank']=batsman['batsman_run'].rank(ascending=False)
print(batsman.sort_values('batting_rank'))

print("\n sort_index(series and dataframe)")
marks = {
    'maths':67,  
    'english':57,  
    'science':89,   
    'hindi':100
}
marks_series = pd.Series(marks)
print(marks_series.sort_index(ascending=False))
print(movies.sort_index(ascending=False))

print("\n set_index(dataframe)") 
batsman.set_index('batter',inplace=True) 
print(batsman)

print("\n reset_index(Series + dataframe) -> drop -> To make it like previous")
batsman.reset_index(inplace= True)
print(batsman)
 
print("\n How to replace existing index without loosing")
print(batsman.reset_index().set_index('batting_rank'))

print("\n series to dataframe using reset_index")
print("Type of mark_series is ",type(marks_series))
print("Type of mark_series is ",type(marks_series.reset_index()))

print("\n rename(dataframe) -> index")
movies.set_index('title_x',inplace=True)
movies.rename(columns={'imdb_id':'imdb','poster_path':'link'},inplace=True)
print("\n We can also change the name of index.")
movies.rename(index={'Uri: The Surgical Strike':'Uri','Battalion 609':'Battalion'},inplace=True)
print(movies)

print("\n unique(series)")
temp = pd.Series([1,1,2,2,3,3,4,4,5,5,np.nan,np.nan])
print(temp)
print(temp.unique())
print(ipl_match['Season'].unique())
print("Number of unique values = ",len(ipl_match['Season'].unique())) # or we can use ipl_match['Season].nunique() :- nunique does not count nan values

print("\n isnull(series + dataframe) -> It tells each value is missing value or not if missing value then return true")




