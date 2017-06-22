# -*- coding: utf-8 -*-
"""
Created on Wed May 31 18:49:27 2017
Exploratory Data Analysis
@author: Alissa
Goals: Investigate Categorical vs. Numerical
Classification of Regression
Decision Trees or Random Forests
"""
import os
os.chdir('C:\Users\Alissa\Documents\Python2') #change directory
cwd=os.getcwd()
print(cwd)
print(os.listdir('.')) #List all files and directories in current directory
#import pandas as pd
#df=pd.read_csv('drug_consumption.txt')#load csv
df=open('drug_consumption.txt','r')
#sklearn? numpy?
