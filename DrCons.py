"""re-write exploring DC
"""
import os
import pandas as pd
import numpy as np
import urllib
u=urllib.urlopen('http://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29')
text=u.read()
import re
matches=re.findall(r"\d+\.\s\w+", text)
del(matches[0:3])
del(matches[12])
print(matches)
os.chdir('C:\Users\Alissa\Documents\Springboard\Capstone1\data\DrugConsumption') #cd and import data
data=pd.read_csv('drug_consumption.txt',header=None) #also header=None
print(data.head())
#1-13 are attributes 14-32 are drugs
attribute=data.iloc[:,:13]
drugs=data.iloc[:,13:] #CL4, CL5, CL6 are use in last month, week, day respectively
import scipy.stats as st
coef=np.random.rand(13,19)
for x in drugs: 
    count=0 #error - invalid sytax
    counter=0
    for y in attribute:
        coef[count,counter]=st.pearsonr(x, y) #x is an unsized object
        count=count+1
    counter=counter+1