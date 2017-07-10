# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 23:05:38 2017

@author: Alissa
"""
import os
import pandas as pd
import numpy as np
import urllib #have to get headers from source
u=urllib.urlopen('http://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29')
text=u.read()
import re
matches=re.findall(r"\d+\.\s\w+", text)
#print(matches)
del(matches[0:3])
del(matches[12])
print(matches) #these are the headers, but how do I add them?
os.chdir('C:\Users\Alissa\Documents\Springboard\Capstone1\data\DrugConsumption') #cd and import data
data=pd.read_csv('drug_consumption.txt',header=None) #also header=None
#delimeter flag
print(data.head())
##finish this part 
#remove 1. from matches
#data=pd.DataFrame(data, coulmns=)
#1-13 are attributes 14-32 are drugs
attribute=data.iloc[:,:13]
drugs=data.iloc[:,13:] #CL4, CL5, CL6 are use in last month, week, day respectively

import scipy.stats as st #check correlation between attributes and drugs
coef=np.matlib.zeros((len(attribute),len(drugs))  #PROBLEM HERE

for x in drugs 
    count=0 #error - invalid sytax
    counter=0
    for y in attribute
        coef[count,counter]=st.pearsonr(x, y)
        count=count+1
    counter=counter+1