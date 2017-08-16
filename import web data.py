# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 14:54:56 2017

@author: Alissa
"""
#load column names
import pandas as pd
import urllib
u=urllib.urlopen('http://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29')
text=u.read()
import re
matches=re.findall(r"\d+\.\s\w+", text)
del(matches[0:3])
del(matches[12])
for i in range(0, len(matches)):
    matches[i]=re.sub(r"\d+\.\s","",matches[i])
print(matches)
# load dataset
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00373/drug_consumption.data"
df = pd.read_csv(url,names=matches)
print(df.head())