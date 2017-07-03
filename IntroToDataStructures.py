# -*- coding: utf-8 -*-
"""
Created on Mon Jul 03 10:24:11 2017
Intro to Data Structures
@author: Alissa
"""
import numpy as np
import pandas as pd
#series is a 1-d labeled array that can hold any data type
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)
print(s[[4,3,1]])
'e' in s
s['e']
s+s
print(np.exp(s))
#print(s.index)
#print(pd.Series(np.random.randn(5)))
#Name
s = pd.Series(np.random.randn(5), name='something')
print(s.name)
s.rename('different')
#make dictionary
#d = {'a' : 0., 'b' : 1., 'c' : 2.}
#print(pd.Series(d,index=['b','c','d','a'])) #output NaN for missing number
##DataFrame
