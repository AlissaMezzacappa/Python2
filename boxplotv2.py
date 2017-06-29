# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 19:56:14 2017

@author: Alissa
"""
df = pd.DataFrame({'Group':['A','A','A','B','C','B','B','C','A','C'],\
                  'Apple':np.random.rand(10),'Orange':np.random.rand(10)})
df = df[['Group','Apple','Orange']]


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dd=pd.melt(df,id_vars=['Group'],value_vars=['Apple','Orange'],var_name='fruits')
sns.boxplot(y='Group',x='value',data=dd,hue='fruits')
