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
       
       

 