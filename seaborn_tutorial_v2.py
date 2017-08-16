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

#Bubble plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(df['Age'],df['Sales'], s=df['Income']) # Added third variable income as size of the bubble
plt.show()

#Color palate
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(rc={"figure.figsize": (6, 6)})
np.random.seed(sum(map(ord, "palettes")))
current_palette = sns.color_palette()
sns.palplot(current_palette)
#circular color
sns.palplot(sns.color_palette("hls", 8))
#control saturation
sns.palplot(sns.hls_palette(8, l=.3, s=.8))
#select evenly spaces hues
sns.palplot(sns.color_palette("husl", 8))
#Categorical color brewer
sns.palplot(sns.color_palette("Paired"))
sns.palplot(sns.color_palette("Set2", 10))
sns.palplot(sns.color_palette(flatui))


#xkcd colors
plt.plot([0, 1], [0, 1], sns.xkcd_rgb["pale red"], lw=3)
plt.plot([0, 1], [0, 2], sns.xkcd_rgb["medium green"], lw=3)
plt.plot([0, 1], [0, 3], sns.xkcd_rgb["denim blue"], lw=3);
        colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
sns.palplot(sns.xkcd_palette(colors))
#sequential color palettes
sns.palplot(sns.color_palette("Blues"))
sns.palplot(sns.color_palette("BuGn_r"))
sns.palplot(sns.color_palette("GnBu_d"))
#diverging color palettes
sns.palplot(sns.color_palette("BrBG", 7))
sns.palplot(sns.color_palette("RdBu_r", 7))
sns.palplot(sns.color_palette("coolwarm", 7))
#cutom
sns.palplot(sns.diverging_palette(220, 20, n=7))
