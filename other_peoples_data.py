# -*- coding: utf-8 -*-
"""
Created on Thu Jul 06 14:20:30 2017
Data cleaning with Pandas
Other People's Messy Data
THIS FILE IS A REFERNCE 
IT IS NOT MEANT TO BE RUN
@author: Alissa
"""
#Pandas take tabular data and do transformations and processing with it
import pandas as pd #unicode sandwich complient #stings coming in are decoded # unicode through out the code #come out encoded again
import numpy as np
pd.read_<tab>
pd.read_stata("state_names.dta",encoding="utf-8") # special char enabled
import chardet
chardet.detect(rawdata) # tells you what the encoding is
file boston_python_is_awesome.tsv #tells you encoding
from unidecode import unidecode
unidecode(stuff)
df=pd.read_excel("filename.xlsx")
df.columns # all the shit in the file
df.describe() #desciptive stats
df.info() # columns number type
#types are important
#merging issues...
#CONVERTING TYPES #dtype from numpy
pd.read_csv(..,dtype={"column_1":int,"column_2":object})
#or
df.column=df.column.astype(int)
#semantics of types - Kinds of nothing :
    #- No data available: None -
    #-Nully values: '', 0
    #identifiers - not numbers - load as strings
    #Categoricals - not strings
    #Ordinals - low, medium, high or *, **, ***, **** - not strings
#DEALING WITH MISSING DATA
#converting custom N/A values
pd.read_csv(..., na_values=['N/A','Unknown'])
#or
df.replace('N/A',None)
#Dropping nulls
df.dropna(axis=1, how='all') #how='any'
df.dropna(method='bfill') 
df.interpolate() #takes average around gap and fills
#examples of indexing
df[["state','county']]
expensive_stuff=df['Aquisition Cost']>100000
df[expensive_stuff].count()
df.sort('Aquisition Cost', ascending=False)\[['Item Name','Acquisition Cost']]
df.UI.value_counts() # count of how many times each value is used
#replace some things
df=df.replace({'UI':['EA','EACH',...]},{'UI':['Each','Each']}) # turn objects in UI column corresponding to 1st set into 2nd set
df.df.replace({'UI':'Unknnown'},{'UI':np.NaN})
df.UI.value_counts()[20:]
#so if the above values you don't want in you df do this:
    dontcare=df.UI.value_counts()[20:]
    df=df[~df.UI.isin(dontcare.index)]
#Reg Expres 
df.column[df.column.str.contains('(\d{4}-\{2})')]
#string functions
df['Item Name'].str.lower()
#PIVOTING
df.pivot(index='date',columns='variable',...)
#Groupby
df.groupby('State')[['Acuisition Cost']].sum()
#Transforming data with functions
df4['one'].map(f)
#MERGING DATAFRAME- types match, size the same after, how=inner and how=outer
pd.merge(ages,weights,left_on='cats',right_on='other column',how='outer') #fill empties with NaN
#Other libraries fuzzywuzzy jellyfish
from fuzzywuzzy import fuzz
fuzz.ratio('this is a test', 'this is a test!") #% match
#Graphs - ggplot=R, bokeh=interactive, seaborn=statistical, matplotlib=everything, glue
#PDFs - tabula table from pdf to csv
#Repeatability maters
#build tools: Make, tup
#Data pipelines: OKFN Bubbles, Storm, Spark
#UNIVERSAL DATA WRANGLING CODE
#Be conscious about what I load into memory
pr.read_csv(...,usecols=['blah'], iterator=True,chunksize=100000)
    #even further - Blaze - pandas like interface for querying large datasets - does everything auto
