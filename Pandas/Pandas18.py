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
], columns=["iq","marks","package"])
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
marks1 = {
    'maths':67,  
    'english':57,  
    'science':89,   
    'hindi':100
}
marks_series = pd.Series(marks1)
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
print(students['name'][students['name'].isnull()])   # applied on series

print("\n hasnans(series)")
print(students['name'].hasnans) # applied on series

print("Applied on dataframe")
print(students.isnull())

print("\n dropna(series + dataframe) -> how parameter -> works like or")
print(students['name'].dropna())

print("\nApplying on dataframe")
print(students.dropna(how='all'))

students.dropna(subset=['name']) # removing na on the basis of name . To make permanenrt changes "inplace = True"
students.dropna(subset=['name','college']) # removing na on the basis of name,college 

print("\n fillna(series + dataframe)")
print(students['name'].fillna('unknown')) # applied on series
# we can also apply on whole dataframe but it is not good method because one number can't satisfy each na


# Best way
print(students['package'].fillna(students['package'].mean(),inplace=True))
print(students)

# forward fill ("ffill")- isha ya hoga ki "na" sa previous wala value joa hai "na" koa mill jeyga.
print(students['name'].fillna(method='ffill'))

# backward fill ("bfill")- isha ya hoga ki "na" k baad wala value joa hai na koa mill jeyga.
print(students['name'].fillna(method='bfill'))

print("\n drop_duplicates(series + dataframe) -> works like and -> duplicated()")
print(marks)
print(marks.duplicated()) # tells which one are duplicate and return True
print("Number of duplicate value are =",marks.duplicated().sum()) # tells how much duplicated value are.


print(marks.drop_duplicates(keep='last')) # here by default keep = 'first'. Means remove first duplicate elements.

print("\n Q). Find the last match played by virat kohli in Delhi")
print(ipl_match)
ipl_match['all_players'] = ipl_match['Team1Players'] + ipl_match['Team2Players']
print(ipl_match.head(5))

def did_kohli_play(player_list):
    return 'V Kohli' in player_list
ipl_match['did_kohli_play'] = ipl_match['all_players'].apply(did_kohli_play)
ans = ipl_match[(ipl_match['City']=='Delhi') & (ipl_match['did_kohli_play']==True)].drop_duplicates(subset=['City'],keep='first')
print(ans)


print("\n # drop(series + dataframe) -> remove row or column")
temp = pd.Series([10,2,3,16,45,78,10])
print(temp)
print(temp.drop(index=[0,6]))


students.drop(columns=['branch','cgpa'],inplace=True) # drop column
students.drop(index=[0,8],inplace=True)
print(students)
print("\n")
students.set_index('name',inplace=True) # make name as index and then drop index
students.drop(index=['ankit','rishabh'],inplace=True)
print(students)

print("\n apply(series + dataframe)")
temp2 = pd.Series([10,20,30,40,50])
print(temp2)
def sigmoid(value):
  return 1/1+np.exp(-value)

print(temp.apply(sigmoid))

print("\n")
points_df = pd.DataFrame(
    {
        '1st point':[(3,4),(-6,5),(0,0),(-10,1),(4,5)],
        '2nd point':[(-3,4),(0,0),(2,2),(10,10),(1,1)]
    }
)
print(points_df)
def euclidean(row):
  pt_A = row['1st point']
  pt_B = row['2nd point']

  return ((pt_A[0] - pt_B[0])**2 + (pt_A[1] - pt_B[1])**2)**0.5
points_df['distance'] = points_df.apply(euclidean,axis=1) # In dataframe we go row-wise.
print(points_df)



