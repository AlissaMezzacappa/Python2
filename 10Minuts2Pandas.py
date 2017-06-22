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
dates=pd.date_range('20130101', periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)
df2 = pd.DataFrame({ 'A' : 1.,'B' : pd.Timestamp('20130102'),
'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
'D' : np.array([3] * 4,dtype='int32'),
'E' : pd.Categorical(["test","train","test","train"]),
'F' : 'foo' })
df.dtypes #gives column types
df.head() #gives first 5 rows
df.tail(3) #gives last 3 rows
df.index #gives indices
df.columns #gives column labels
df.values #gives values
df.describe
df.T #TRAnspose
df.sort_index(axis=1, ascending=False)
df.sort_values(by='B')
#Selection Skipped to
#Getting Data In/Out
