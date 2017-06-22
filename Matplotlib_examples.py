# -*- coding: utf-8 -*-
"""
Created on Thu May 25 13:30:51 2017

@author: Alissa
"""
#Matplotlib
#import subpackage
import matplotlib.pyplot as plt
year=[2000,2005,2010,2015]
pop=[10,20,30,40]
plt.plot(year,pop) #plot with line between points
plt.show() #to show plot 
#or scatter plot
plt.scatter(year,pop)
plt.xscale('log')
plt.show()
#histogram
import numpy as np
values=np.randint(0,100,50)
plt.hist(values, bins=3)
plt.clf() #cleans up 
#population append historical data
year=[1800,1850,1900]+ year
pop=[1.0, 1.262, 1.650] + pop
#label axes
plt.xlabel('Year')
plt.ylabel('Population')
#put a title
plt.title('World Population Projections')
#change y axis values
plt.yticks([0,2,4,6,8,10],['0','2B','4B','6B','8B','10B'])
