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
plt.hist(titanic.Age.dropna(),bins=25,color=sns.desaturate("indianred",1)) #2nd argument 0-1
#boxplot
fig2=plt.figure()
#sns.boxplot(titanic.Age.dropna(),vert=True)
#two sku boxplot
sns.boxplot(x=titanic.Age.dropna(),y=titanic.Sex) #generates error
#testing other method:
    #redo variables for plot
    df = pd.DataFrame({'Group':['A','A','A','B','C','B','B','C','A','C'],\
                  'Apple':np.random.rand(10),'Orange':np.random.rand(10)})
df = df[['Group','Apple','Orange']]
#
dd=pd.melt(df,id_vars=['Group'],value_vars=['Apple','Orange'],var_name='fruits')
sns.boxplot(y='Group',x='value',data=dd,hue='fruits')
(y=titanic.Sex, x=titanic.Age, )
##Ref:https://stackoverflow.com/questions/16592222/matplotlib-group-boxplots
##Kernel Density Estimate Plot
#fig3=plt.figure()
#sns.kdeplot(titanic.Age.dropna(),shade=True)
#fig4=plt.figure()
#sns.distplot(titanic.Age.dropna())
##Violin Plot
#sns.violinplot(titanic.Age.dropna(),vert=True)
#fig5=plt.figure()
#sns.violinplot(titanic.Age.dropna(),titanic.Sex)
##Cumulative Distribution Function
#fig6=plt.figure()
#sns.kdeplot(titanic.Age.dropna(),cumulative=True)
##test test test
