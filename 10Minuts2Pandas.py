# -*- coding: utf-8 -*-
"""
Created on Wed May 31 17:31:03 2017
10 minutes to pandas
@author: Alissa
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Object Creation - Creating a Series by passing list values
s=pd.Series([1,3,5,np.nan,6,8])
#DataFrame with datetime index
dates=pd.date_range('20130101', periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)
#Creating a DataFrame by passing a dict of objects that an be converted to series-like
df2 = pd.DataFrame({ 'A' : 1.,'B' : pd.Timestamp('20130102'),
'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
'D' : np.array([3] * 4,dtype='int32'),
'E' : pd.Categorical(["test","train","test","train"]),
'F' : 'foo' })
df2.dtypes #gives column types
df.head() #gives first 5 rows
df.tail(3) #gives last 3 rows
df.index #gives indices
df.columns #gives column labels
df.values #gives values
df.describe
df.T #TRAnspose
df.sort_index(axis=1, ascending=False)
df.sort_values(by='B')
#Selection - 
df['A'] #equivalent to df.A
df[0:3] #slicing rows
#selection by label
df.loc[dates[0]]
df.loc[:,['A','B']] #selecting multi-axis by label
df.at[dates[0],'A']
#select position via passed integer: this select 4th row
df.iloc[3]
df.iloc[3:5,0:2]
df.iloc[[1,2,4],[0,2]]
df.iloc[1:3,:]
 #Boolean indexing
 #use single column's values to select data
df[df.A > 0]
 #selecting values from DataFrame where boolean condition is met
df[df > 0]
 #filtering with isin()
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
df2[df2['E'].isin(['two','four'])]
#Setting a new column automatically aligns indexes
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
df['F'] = s1
#setting values by label
df.at[dates[0],'A'] = 0
#setting values by position
df.iat[0,1] = 0
#Missing Data
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1],'E'] = 1
print(df1)
df1.dropna() #df1.dropna(how='any')
#filling missing data
df1.fillna(value=5)
#get booklean mask where values are nan
pd.isnull(df1)

##Operations - operations will in general exclude missing data
print(df)
print(df.mean())
print(df.mean(1))
s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2) #shift 2 rows down
df.sub(s, axis='index') #unclear what this is doing...
#apply functions to data
df.apply(np.cumsum)
#Histogramming
s = pd.Series(np.random.randint(0, 7, size=10))
s.value_counts() #gives hist 1-d values
#String Methods
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s.str.lower() #makes strings lower case
s.str.upper()
s.str.len()
#Merge - Concat
df = pd.DataFrame(np.random.randn(10, 4))
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)
#join
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
pd.merge(left, right, on='key')
#alt join ex
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
pd.merge(left, right, on='key')
#Append
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
s = df.iloc[3]
df.append(s, ignore_index=True)
#Groupping
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'], 'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],  'C' : np.random.randn(8),'D' : np.random.randn(8)})
df.groupby('A').sum()
df.groupby(['A','B']).sum()

#Reshaping
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df2 = df[:4]
stacked = df2.stack()
stacked.unstack()
stacked.unstack(1)
stacked.unstack(0)
#Pivot Tables
df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,\
                   'B' : ['A', 'B', 'C'] * 4,\
                            'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,\
                                  'D' : np.random.randn(12),\
                       'E' : np.random.randn(12)})
pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
#Time Series
#resampling durring frequency conversion
rng = pd.date_range('1/1/2012', periods=100, freq='S')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts.resample('5Min').sum()
#time zone rep
rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)
ts_utc = ts.tz_localize('UTC')
#convert to another time zone
ts_utc.tz_convert('US/Eastern')
#Convert between time span representations
rng = pd.date_range('1/1/2012', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ps = ts.to_period()
ps.to_timestamp()
#convert a quarterly frequency with year ending in November 
#to 9am of the end of the month following the quarter end
prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
ts = pd.Series(np.random.randn(len(prng)), prng)
ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9

           #Categoricals
df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']}) 
#Convert the raw grades to a categorical data type.
df["grade"] = df["raw_grade"].astype("category")
#rename categories
df["grade"].cat.categories = ["very good", "good", "very bad"]
 #reorder and add missing categories
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
df.sort_values(by="grade") #sort
df.groupby("grade").size() #group  by categorical column

          ##Plotting
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum() #cumulative sum
ts.plot()
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
plt.figure(); df.plot(); plt.legend(loc='best')

#Getting Data In/Out
#Writing to csv
df.to_csv('foo.csv')
#reading from csv
pd.read_csv('foo.csv')
#HDF5
df.to_hdf('foo.h5','df')
pd.read_hdf('foo.h5','df')
#Excel
df.to_excel('foo.xlsx', sheet_name='Sheet1')
pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])

