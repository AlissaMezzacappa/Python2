# -*- coding: utf-8 -*-
"""
Created on Tue May 23 16:57:38 2017

@author: Alissa
"""
import os
#Retrieve current working directory
cwd=os.getcwd()
print(cwd)
#change directory
os.chdir('C:\Users\Alissa\Documents')
#List all files and directories in current directory
print(os.listdir('.'))

import pandas as pd
#load csv
df=pd.read_csv('Research.csv')
#Also read_table() to read general delimited files, default delimiter is tab but can change
#and read_fwf() to read tables of fixed-width formatted lines into DataFrames

file='Bird Log.xlsx'
#load spreadsheet
xl=pd.ExcelFile(file)
#print the sheet names
print(xl.sheet_names)
#load sheet into a DataFrame by name: df1
df1=xl.parse('Sheet1')
print(df.sheet_names)
#sf2=df.parse() <--Does not work for csv
#H