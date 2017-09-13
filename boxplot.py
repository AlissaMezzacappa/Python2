# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 19:56:14 2017

@author: Alissa
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dd=pd.melt(df,id_vars=['Group'],value_vars=['Apple','Orange'],var_name='fruits')
sns.boxplot(y='Group',x='value',data=dd,hue='fruits')