# Day 25: pandas   (pip install pandas). Run from the repo root.
import pandas as pd

small = pd.DataFrame({'name': ['Ana', 'Ben'], 'age': [17, 16]})   # build one by hand
print(small)

df = pd.read_csv('data/hacker_news.csv')       # Ex 1: CSV -> DataFrame (a table)
print(df.head())                               # Ex 2: first 5 rows (df.tail() = last 5)
print(df.shape)                                # Ex 5: (rows, columns)
print(df.columns.tolist())

titles = df['title']                           # Ex 4: one column = a Series
mask = titles.str.contains('Python', case=False, na=False)   # True/False for every row
print(mask.sum())                              # True counts as 1
print(df[mask]['title'].head(3).tolist())      # Ex 5: keep only the True rows

df['title_len'] = titles.str.len()             # add a column
print(df['num_points'].describe())             # count, mean, std, min, max in one call
