# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 15:57:12 2017
Working with missing data
@author: Alissa
"""
#data goes missing commonly due to reindexing
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'],columns=['one', 'two', 'three']) 
df['four'] = 'bar'  
df['five'] = df['one'] > 0 
df2 = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']) 
 #finding NaN - None
 df2.isnull()
 df2.notnull()
 None==None #True
 np.nan==np.nan #False
 #Datetimes - NaT is a missing value
df2 = df.copy() 
df2['timestamp'] = pd.Timestamp('20120101')
df2.loc[['a','c','h'],['one','timestamp']] = np.nan #puts NaN in 'one' and NaT in 'timestamp'
df2.get_dtype_counts() 
s=pd.Series([1, 2, 3])          #float64
s.loc[0]=None #numeric container chooses NaN
 s = pd.Series(["a", "b", "c"]) #object
 s.loc[0] = None     #object container chooses None
  s.loc[1] = np.nan #but can still put NaN
#Calculations with missing data
df['one'].sum() #missing values treated as zero
df.mean()
df.cumsum()  
#NA values in GroupBy
df.groupby('one').mean() #automatically excludes NA
#filling missing values
#Replace NA with a scalar value
df2.fillna(0)       
df2['four'].fillna('missing')
#Fill gaps forward or backward
df=pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'],columns=['one', 'two', 'three']) 
df['four'] = 'bar'  
df['five'] = df['one'] > 0 
df2 = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']) 
df2.fillna(method='pad')      # 'pad'='ffill'  'bfill'='backfill' 
df2.fillna(method='pad',limit=1)     
#Fill with mean
dff = pd.DataFrame(np.random.randn(10,3), columns=list('ABC'))
dff.iloc[3:5,0] = np.nan   
dff.iloc[4:6,1] = np.nan 
dff.iloc[5:8,2] = np.nan
dff.fillna(dff.mean()) #or
dff.where(pd.notnull(dff), dff.mean(), axis='columns') 
dff.fillna(dff.mean()['B':'C'])
#Drop an axis
df.dropna(axis=0) #drop index
df.dropna(axis=1) #drop 1st column 
#Interpolate values
ts2.count()
ts2.interpolate().count()
ts2.interpolate() 
ts2.interpolate(method='time')
#floating point
ser.interpolate(method='values')  
#can interpolate a data frame
#method arguement gives type of interpolation for example:
    #method='quadratic' or method ='pchip' is cumulative
    #method='akima' - smooth
df.interpolate(method='barycentric')
df.interpolate(method='spline',order=2) 
df.interpolate(method='polynomial',order=2) #2nd order polynomial
#Compare
methods = ['linear', 'quadratic', 'cubic']
df = pd.DataFrame({m: ser.interpolate(method=m) for m in methods}) 
df.plot()
#mix reindex and interpolate to spread out middle of data
ser = pd.Series(np.sort(np.random.uniform(size=100))) 
new_index = ser.index | pd.Index([49.25, 49.5, 49.75, 50.25, 50.5, 50.75]) 
interp_s = ser.reindex(new_index).interpolate(method='pchip') 
interp_s[49:51] 
#Limit interpolation
ser = pd.Series([np.nan, np.nan, 5, np.nan, np.nan, np.nan, 13]) 
ser.interpolate(limit=2) #direction sensitive
ser.interpolate(limit=1)  # limit_direction == 'forward' 
ser.interpolate(limit=1, limit_direction='backward') 
ser.interpolate(limit=1, limit_direction='both')
#Replacing values
ser.replace(0, 5) #replace 0 with 5
ser.replace([0, 1, 2, 3, 4], [4, 3, 2, 1, 0]) #replace by list
#or specify mapping dictionary
ser.replace({0: 10, 1: 100})
#individual values by column
df = pd.DataFrame({'a': [0, 1, 2, 3, 4], 'b': [5, 6, 7, 8, 9]})
df.replace({'a': 0, 'b': 5}, 100)
#interpolate over
ser.replace([1, 2, 3], method='pad') 
#String / RegEx Replacement
d = {'a': list(range(4)), 'b': list('ab..'), 'c': ['a', 'b', np.nan, 'd']}
df = pd.DataFrame(d)
df.replace('.', np.nan)
#regex
df.replace(r'\s*\.\s*', np.nan, regex=True)
#list -> list
df.replace(['a', '.'], ['b', np.nan]) 
 #regex ->regex
df.replace([r'\.', r'(a)'], ['dot', '\1stuff'], regex=True) 
#dict -> dict
df.replace({'b': '.'}, {'b': np.nan}) #for column 'b' replace ...
df.replace({'b': r'\s*\.\s*'}, {'b': np.nan}, regex=True) #dict of regex->dict
df.replace({'b': {'b': r''}}, regex=True) #nested dictionaries
df.replace(regex={'b': {r'\s*\.\s*': np.nan}}) 
df.replace({'b': r'\s*(\.)\s*'}, {'b': r'\1ty'}, regex=True) 
df.replace([r'\s*\.\s*', r'a|b'], np.nan, regex=True) 
#alternatively
df.replace(regex=[r'\s*\.\s*', r'a|b'], value=np.nan) 
#numeric replacement
df = pd.DataFrame(np.random.randn(10, 2))    #create array
df[np.random.rand(df.shape[0]) > 0.5] = 1.5     #somehow rounding values close to 1.5 to 1.5
df.replace(1.5, np.nan) 
df00 = df.values[0, 0] 
df.replace([1.5, df00], [np.nan, 'a'])                
s = pd.Series([True, False, True])                
s.replace('a string', 'another string')
#Missing data casting rules and indexing
#data type->Cast to 
#integer -> float 
#boolean -> object 
#float -> no cast 
#object -> no cast
s = pd.Series(np.random.randn(5), index=[0, 2, 4, 6, 7]) #boolean type
crit = (s > 0).reindex(list(range(8))) #reindex booleen filled df _becomes object
crit.dtype
#floating point
reindexed = s.reindex(list(range(8))).fillna(0) 
 #fillna worksb
reindexed[crit.fillna(False)] #don't get what's happening here
reindexed[crit.fillna(True)]