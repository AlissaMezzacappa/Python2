# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:47:14 2017
#Exploring Seaborn
@author: Alissa
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#seaborn settings
sns.set_palette("deep",desat=.6)
sns.set_context(rc={"figure.figsize":(8,4)})
#load data set
titanic=pd.read_csv('train.csv')
print(titanic.head())
#histogram
fig1=plt.figure()
plt.hist(titanic.Age.dropna(),bins=25) #color=sns.desaturate("indianred",a))
#boxplot
fig2=plt.figure()
sns.boxplot(titanic.Age.dropna(),vert=True)
#two sku boxplot
sns.boxplot(titanic.Age.dropna(),titanic.Sex) #generates error
#Kernel Density Estimate Plot
fig3=plt.figure()
sns.kdeplot(titanic.Age.dropna(),shade=True)
fig4=plt.figure()
sns.distplot(titanic.Age.dropna())
#Violin Plot
sns.violinplot(titanic.Age.dropna(),vert=True)
fig5=plt.figure()
sns.violinplot(titanic.Age.dropna(),titanic.Sex)
#Cumulative Distribution Function
fig6=plt.figure()
sns.kdeplot(titanic.Age.dropna(),cumulative=True)
#test test test
