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
for i in range(0, len(matches)):
    matches=re.sub(r"\d+\.\s","",matches[i])
#remove /d/./s ###
#matches=re.sub(r'\d+\.\s','',matches, flags=0)
print(matches)
os.chdir('C:\Users\Alissa\Documents\Springboard\Capstone1\data\DrugConsumption') #cd and import data
data=pd.read_csv('drug_consumption.txt',header=None,names=matches) #also header=None
print(data.head())
#also need to make drug use binary instead of 'CL'/d #try 'converters' arguement
#1-13 are attributes 14-32 are drugs
attribute=data.iloc[:,:13]
attribute.columns=[0,1,2,3,4,5,6,7,8,9,10,11,12]
drugs=data.iloc[:,13:] #CL4, CL5, CL6 are use in last month, week, day respectively
drugs.columns=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
import scipy.stats as st
coef=np.random.rand(13,19)
for x in range(len(drugs)): 
    count=0 #error - invalid sytax
    counter=0
    for y in range(len(attribute)):
        coef[count,counter]=st.pearsonr(drugs[x], attribute[y]) #x is an unsized object
        count=count+1
    counter=counter+1
#To try: XG Boost or boosting - tree tech.
