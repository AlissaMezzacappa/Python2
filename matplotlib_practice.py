# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 16:18:24 2017
Matplotlib Practice
@author: Alissa
"""
import numpy as np
import matplotlib.pyplot as plt
#histogram
x = np.random.normal(size=1000)

fig, ax = plt.subplots()

H = ax.hist(x, bins=50, alpha=0.5, histtype='stepfilled') 

#pie plots
fracs = [30, 15, 45, 10]
colors = ['b', 'g', 'r', 'w']

fig, ax = plt.subplots(figsize=(6, 6))  # make the plot square
pie = ax.pie(fracs, colors=colors, explode=(0, 0, 0.05, 0), shadow=True,
             labels=['A', 'B', 'C', 'D'])

#error bars
x = np.linspace(0, 10, 30)
dy = 0.1
y = np.random.normal(np.sin(x), dy)

fig, ax = plt.subplots()
plt.errorbar(x, y, dy, fmt='.k')

#filled plots
x = np.linspace(0, 10, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots()
ax.fill_between(x, y1, y2, where=(y1 < y2), color='red')
ax.fill_between(x, y1, y2, where=(y1 > y2), color='blue')

#scatter plot
x = np.random.random(50)
y = np.random.random(50)
c = np.random.random(50)  # color of points
s = 500 * np.random.random(50)  # size of points

fig, ax = plt.subplots()
im = ax.scatter(x, y, c=c, s=s, cmap=plt.cm.jet)

# Add a colorbar
fig.colorbar(im, ax=ax)

# set the color limits - not necessary here, but good to know how.
im.set_clim(0.0, 1.0)


#contour plots
x = np.linspace(0, 10, 50)
y = np.linspace(0, 20, 60)

z = np.cos(y[:, np.newaxis]) * np.sin(x)

fig, ax = plt.subplots()

# filled contours
im = ax.contourf(x, y, z, 100)

# contour lines
im2 = ax.contour(x, y, z, colors='k')

fig.colorbar(im, ax=ax)

##show image
I = np.random.random((100, 100))

I += np.sin(np.linspace(0, np.pi, 100))

fig, ax = plt.subplots()

im = ax.imshow(I, cmap=plt.cm.jet)

fig.colorbar(im, ax=ax)

##2d histogram and hexbin
x, y = np.random.normal(size=(2, 10000))

fig, ax = plt.subplots()
im = ax.hexbin(x, y, gridsize=20)
fig.colorbar(im, ax=ax)

fig, ax = plt.subplots()
H = ax.hist2d(x, y, bins=20)
fig.colorbar(H[3], ax=ax)

##polar plots
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='polar')
                    
theta = np.linspace(0, 10 * np.pi, 1000)
r = np.linspace(0, 10, 1000)

ax.plot(theta, r)
