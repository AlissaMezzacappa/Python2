# -*- coding: utf-8 -*-
"""
Created on Wed May 31 16:45:26 2017
Matplotlib tuttorial
@author: Alissa
"""
#%matplotlib inline
#Import symbols from module like this:
#or import the module and name it
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 10) #from 0 generate 10 indexes incrimenting up to 5
#print(x)
#y = x ** 2
#plt.figure()
#plt.plot(x, y, 'r')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('title')
#plt.show()
#plt.subplot(1,2,1)
#plt.plot(x, y, 'r--')
#plt.subplot(1,2,2)
#plt.plot(y, x, 'g*-');
import matplotlib.pyplot as plt
import numpy as np
#fig = plt.figure(figsize=(8,4), dpi=100)
#fig = plt.figure()
x = np.linspace(0, 5, 10)
y = x ** 2
#axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)
#
#axes.plot(x, y, 'r')
#
#axes.set_title('title');
#axes.set_xlabel('x')
#axes.set_ylabel('y')
##Make inset figure inside figure
#fig = plt.figure()
#
#axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
#axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # inset axes
#
## main figure
#axes1.plot(x, y, 'r')
#axes1.set_xlabel('x')
#axes1.set_ylabel('y')
#axes1.set_title('title')
#
## insert
#axes2.plot(y, x, 'g')
#axes2.set_xlabel('y')
#axes2.set_ylabel('x')
#axes2.set_title('insert title');

#subplots
fig = plt.figure()
ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
ax3 = plt.subplot2grid((3,3), (1,2), rowspan=2)
ax4 = plt.subplot2grid((3,3), (2,0))
ax5 = plt.subplot2grid((3,3), (2,1))
fig.tight_layout()
#or the regular way
#fig, axes = plt.subplots()
#fig, axes = plt.subplots(figsize=(12,3))
#axes.plot(x, y, 'r')
#axes.set_xlabel('x')
#axes.set_ylabel('y')
#axes.set_title('title');
#
#fig, axes = plt.subplots(nrows=1, ncols=2)
#
#for ax in axes:
#    ax.plot(x, y, 'r')
#    ax.set_xlabel('x')
#    ax.set_ylabel('y')
#    ax.set_title('title')              
#    
#fig.tight_layout()
#
##Saving figures
#fig.savefig("filename.png", dpi=200)

##making legends
#fig = plt.figure()
#
#ax= fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
#ax.plot(x, x**2, label="curve1")
#ax.plot(x, x**3, label="curve2")
##ax.legend();
#ax.legend(loc=0) # let matplotlib decide the optimal location
#ax.legend(loc=1) # upper right corner
#ax.legend(loc=2) # upper left corner
#ax.legend(loc=3) # lower left corner
#ax.legend(loc=4) # lower right corner
# .. many more options are available

#fig, ax = plt.subplots()
#
#ax.plot(x, x**2, label="y = x**2")
#ax.plot(x, x**3, label="y = x**3")
#ax.legend(loc=2); # upper left corner
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_title('title');

             
#Formatting labels:
    #change the global font size and font family, which applies to all text elements in a figure (tick labels, axis labels and titles, legends, etc.)
#matplotlib.rcParams.update({'font.size': 18, 'font.family': 'serif'}) #for example
#matplotlib.rcParams.update({'font.size': 18, 'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix'}) #or stix
#matplotlib.rcParams.update({'font.size': 18, 'text.usetex': True}) #of LaTex #DNW
## restore
#matplotlib.rcParams.update({'font.size': 12, 'font.family': 'sans', 'text.usetex': False})
#fig, ax = plt.subplots()
#
#ax.plot(x, x**2, label=r"$y = \alpha^2$") #LaTex label
#ax.plot(x, x**3, label=r"$y = \alpha^3$") #use $ to encapsulate LaTex text $
#ax.legend(loc=2) # upper left corner
#ax.set_xlabel(r'$\alpha$', fontsize=18)#LaTex label
#ax.set_ylabel(r'$y$', fontsize=18)
#ax.set_title('title');
#            
## MATLAB style line color and style 
#ax.plot(x, x**2, 'b.-') # blue line with dots
#ax.plot(x, x**3, 'g--') # green dashed line
#fig, ax = plt.subplots()
#
#ax.plot(x, x+1, color="red", alpha=0.5) # half-transparant red
#ax.plot(x, x+2, color="#1155dd")        # RGB hex code for a bluish color
#ax.plot(x, x+3, color="#15cc55")        # RGB hex code for a greenish color

##linestyles
#fig, ax = plt.subplots(figsize=(12,6))
#
#ax.plot(x, x+1, color="blue", linewidth=0.25)
#ax.plot(x, x+2, color="blue", linewidth=0.50)
#ax.plot(x, x+3, color="blue", linewidth=1.00)
#ax.plot(x, x+4, color="blue", linewidth=2.00)
#
## possible linestype options ‘-‘, ‘--’, ‘-.’, ‘:’, ‘steps’
#ax.plot(x, x+5, color="red", lw=2, linestyle='-')
#ax.plot(x, x+6, color="red", lw=2, ls='-.')
#ax.plot(x, x+7, color="red", lw=2, ls=':')
#
## custom dash
#line, = ax.plot(x, x+8, color="black", lw=1.50)
#line.set_dashes([5, 10, 15, 10]) # format: line length, space length, ...
#
## possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
#ax.plot(x, x+ 9, color="green", lw=2, ls='--', marker='+')
#ax.plot(x, x+10, color="green", lw=2, ls='--', marker='o')
#ax.plot(x, x+11, color="green", lw=2, ls='--', marker='s')
#ax.plot(x, x+12, color="green", lw=2, ls='--', marker='1')
#
## marker size and color
#ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
#ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
#ax.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
#ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8, 
#        markerfacecolor="yellow", markeredgewidth=2, markeredgecolor="blue");
        
##PLOT RANGE
#fig, axes = plt.subplots(1, 3, figsize=(12, 4))
#
#axes[0].plot(x, x**2, x, x**3)
#axes[0].set_title("default axes ranges")
#
#axes[1].plot(x, x**2, x, x**3)
#axes[1].axis('tight')
#axes[1].set_title("tight axes")
#
#axes[2].plot(x, x**2, x, x**3)
#axes[2].set_ylim([0, 60])
#axes[2].set_xlim([2, 5])
#axes[2].set_title("custom axes range");
#    
##Logrythmic Scale
#fig, axes = plt.subplots(1, 2, figsize=(10,4))
#      
#axes[0].plot(x, x**2, x, np.exp(x))
#axes[0].set_title("Normal scale")
#
#axes[1].plot(x, x**2, x, np.exp(x))
#axes[1].set_yscale("log")
#axes[1].set_title("Logarithmic scale (y)");

##ticks
#fig, ax = plt.subplots(figsize=(10, 4))
#
#ax.plot(x, x**2, x, x**3, lw=2)
#
#ax.set_xticks([1, 2, 3, 4, 5])
#ax.set_xticklabels([r'$\alpha$', r'$\beta$', r'$\gamma$', r'$\delta$', r'$\epsilon$'], fontsize=18)
#
#yticks = [0, 50, 100, 150]
#ax.set_yticks(yticks)
#ax.set_yticklabels(["$%.1f$" % y for y in yticks], fontsize=18); # use LaTeX formatted labels
#
#                  #Scientific Notation
#fig, ax = plt.subplots(1, 1)
#      
#ax.plot(x, x**2, x, np.exp(x))
#ax.set_title("scientific notation")
#
#ax.set_yticks([0, 50, 100, 150])
#
#from matplotlib import ticker
#formatter = ticker.ScalarFormatter(useMathText=True)
#formatter.set_scientific(True) 
#formatter.set_powerlimits((-1,1)) 
#ax.yaxis.set_major_formatter(formatter) 
#
###AXIS NUMBER AND LABEL SPACING
## distance between x and y axis and the numbers on the axes
#matplotlib.rcParams['xtick.major.pad'] = 5
#matplotlib.rcParams['ytick.major.pad'] = 5
#
#fig, ax = plt.subplots(1, 1)
#      
#ax.plot(x, x**2, x, np.exp(x))
#ax.set_yticks([0, 50, 100, 150])
#
#ax.set_title("label and axis spacing")
#
## padding between axis label and axis numbers
#ax.xaxis.labelpad = 5
#ax.yaxis.labelpad = 5
#
#ax.set_xlabel("x")
#ax.set_ylabel("y");
## restore defaults
#matplotlib.rcParams['xtick.major.pad'] = 3
#matplotlib.rcParams['ytick.major.pad'] = 3
#                   
###Axis position adjustment
#fig, ax = plt.subplots(1, 1)
#      
#ax.plot(x, x**2, x, np.exp(x))
#ax.set_yticks([0, 50, 100, 150])
#
#ax.set_title("title")
#ax.set_xlabel("x")
#ax.set_ylabel("y")
#
#fig.subplots_adjust(left=0.15, right=.9, bottom=0.1, top=0.7);
                   
#                   #Axes Grid
#fig, axes = plt.subplots(1, 2, figsize=(10,3))
#
## default grid appearance
#axes[0].plot(x, x**2, x, x**3, lw=2)
#axes[0].grid(True)
#
## custom grid appearance
#axes[1].plot(x, x**2, x, x**3, lw=2)
#axes[1].grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.9)
#
##AXIS SPINES
#fig, ax = plt.subplots(figsize=(6,2))
#
#ax.spines['bottom'].set_color('blue')
#ax.spines['top'].set_color('blue')
#
#ax.spines['left'].set_color('red')
#ax.spines['left'].set_linewidth(2)
#
## turn off axis spine to the right
#ax.spines['right'].set_color("none")
#ax.yaxis.tick_left() # only ticks on the left side
#
##Dual Axes
#fig, ax1 = plt.subplots()
#
#ax1.plot(x, x**2, lw=2, color="blue")
#ax1.set_ylabel(r"area $(m^2)$", fontsize=18, color="blue")
#for label in ax1.get_yticklabels():
#    label.set_color("blue")
#    
#ax2 = ax1.twinx()       #make twin axis
#ax2.plot(x, x**3, lw=2, color="red")
#ax2.set_ylabel(r"volume $(m^3)$", fontsize=18, color="red")
#for label in ax2.get_yticklabels():
#    label.set_color("red")

##Axes where x and y is zero
#fig, ax = plt.subplots()
#
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
#
#ax.xaxis.set_ticks_position('bottom')
#ax.spines['bottom'].set_position(('data',0)) # set position of x spine to x=0
#
#ax.yaxis.set_ticks_position('left')
#ax.spines['left'].set_position(('data',0))   # set position of y spine to y=0
#
#xx = np.linspace(-0.75, 1., 100)
#ax.plot(xx, xx**3);
#       
##other plots
#n = np.array([0,1,2,3,4,5])
#fig, axes = plt.subplots(1, 4, figsize=(48,12))
#
#axes[0].scatter(x, x + 0.25*np.random.randn(len(x)))
#axes[0].set_title("scatter")
#
#axes[1].step(n, n**2, lw=2)
#axes[1].set_title("step")
#
#axes[2].bar(n, n**2, align="center", width=0.5, alpha=0.5)
#axes[2].set_title("bar")
#
#axes[3].fill_between(x, x**2, x**3, color="green", alpha=0.5);
#axes[3].set_title("fill_between");       
#    
## polar plot using add_axes and polar projection
#fig = plt.figure()
#ax = fig.add_axes([0.0, 0.0, .6, .6], polar=True)
#t = np.linspace(0, 2 * np.pi, 100)
#ax.plot(t, t, color='blue', lw=3);
#       
## A histogram
#n = np.random.randn(100000)
#fig, axes = plt.subplots(1, 2, figsize=(12,4))
#
#axes[0].hist(n)
#axes[0].set_title("Default histogram")
#axes[0].set_xlim((min(n), max(n)))
#
#axes[1].hist(n, cumulative=True, bins=50)
#axes[1].set_title("Cumulative detailed histogram")
#axes[1].set_xlim((min(n), max(n)));
#    
##Text Annotation
#fig, ax = plt.subplots()
#
#ax.plot(xx, xx**2, xx, xx**3)
#
#ax.text(0.15, 0.2, r"$y=x^2$", fontsize=20, color="blue")
#ax.text(0.65, 0.1, r"$y=x^3$", fontsize=20, color="green");
#       
#       #Color Map
#fig, ax = plt.subplots()
#
#p = ax.pcolor(X/(2*np.pi), Y/(2*np.pi), Z, cmap=matplotlib.cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max())
#cb = fig.colorbar(p, ax=ax)
##Contour map
#fig, ax = plt.subplots()
#
#cnt = ax.contour(Z, cmap=matplotlib.cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max(), extent=[0, 1, 0, 1])
#
##3D
#from mpl_toolkits.mplot3d.axes3d import Axes3D
##surface plot
#fig = plt.figure(figsize=(14,6))
#
## `ax` is a 3D-aware axis instance because of the projection='3d' keyword argument to add_subplot
#ax = fig.add_subplot(1, 2, 1, projection='3d')
#
#p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)
#
## surface_plot with color grading and color bar
#ax = fig.add_subplot(1, 2, 2, projection='3d')
#p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=False)
#cb = fig.colorbar(p, shrink=0.5)
##wire frame plot
#fig = plt.figure(figsize=(8,6))
#
#ax = fig.add_subplot(1, 1, 1, projection='3d')
#
#p = ax.plot_wireframe(X, Y, Z, rstride=4, cstride=4)
#
##Contour plot with projections
#fig = plt.figure(figsize=(8,6))
#
#ax = fig.add_subplot(1,1,1, projection='3d')
#
#ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
#cset = ax.contour(X, Y, Z, zdir='z', offset=-np.pi, cmap=matplotlib.cm.coolwarm)    #projection added here
#cset = ax.contour(X, Y, Z, zdir='x', offset=-np.pi, cmap=matplotlib.cm.coolwarm)    #projection added here
#cset = ax.contour(X, Y, Z, zdir='y', offset=3*np.pi, cmap=matplotlib.cm.coolwarm)   #projection added here
#
#ax.set_xlim3d(-np.pi, 2*np.pi);
#ax.set_ylim3d(0, 3*np.pi);
#ax.set_zlim3d(-np.pi, 2*np.pi);
#             
#             #Change Angle
#fig = plt.figure(figsize=(12,6))
#
#ax = fig.add_subplot(1,2,1, projection='3d')
#ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
#ax.view_init(30, 45)    #angle changed here
#
#ax = fig.add_subplot(1,2,2, projection='3d')
#ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
#ax.view_init(70, 30)    #angle changed here
#
#fig.tight_layout()

#Animation
from matplotlib import animation
# solve the ode problem of the double compound pendulum again

from scipy.integrate import odeint
from numpy import cos, sin

g = 9.82; L = 0.5; m = 0.1

def dx(x, t):
    x1, x2, x3, x4 = x[0], x[1], x[2], x[3]
    
    dx1 = 6.0/(m*L**2) * (2 * x3 - 3 * cos(x1-x2) * x4)/(16 - 9 * cos(x1-x2)**2)
    dx2 = 6.0/(m*L**2) * (8 * x4 - 3 * cos(x1-x2) * x3)/(16 - 9 * cos(x1-x2)**2)
    dx3 = -0.5 * m * L**2 * ( dx1 * dx2 * sin(x1-x2) + 3 * (g/L) * sin(x1))
    dx4 = -0.5 * m * L**2 * (-dx1 * dx2 * sin(x1-x2) + (g/L) * sin(x2))
    return [dx1, dx2, dx3, dx4]

x0 = [np.pi/2, np.pi/2, 0, 0]  # initial state
t = np.linspace(0, 10, 250) # time coordinates
x = odeint(dx, x0, t)    # solve the ODE problem
#Generate an animation that shows the positions of the pendulums as a function of time:
fig, ax = plt.subplots(figsize=(5,5))

ax.set_ylim([-1.5, 0.5])
ax.set_xlim([1, -1])

pendulum1, = ax.plot([], [], color="red", lw=2)
pendulum2, = ax.plot([], [], color="blue", lw=2)

def init():
    pendulum1.set_data([], [])
    pendulum2.set_data([], [])

def update(n): 
    # n = frame counter
    # calculate the positions of the pendulums
    x1 = + L * sin(x[n, 0])
    y1 = - L * cos(x[n, 0])
    x2 = x1 + L * sin(x[n, 1])
    y2 = y1 - L * cos(x[n, 1])
    
    # update the line data
    pendulum1.set_data([0 ,x1], [0 ,y1])
    pendulum2.set_data([x1,x2], [y1,y2])

anim = animation.FuncAnimation(fig, update, init_func=init, frames=len(t), blit=True)

# anim.save can be called in a few different ways, some which might or might not work
# on different platforms and with different versions of matplotlib and video encoders
#anim.save('animation.mp4', fps=20, extra_args=['-vcodec', 'libx264'], writer=animation.FFMpegWriter())
#anim.save('animation.mp4', fps=20, extra_args=['-vcodec', 'libx264'])
#anim.save('animation.mp4', fps=20, writer="ffmpeg", codec="libx264")
anim.save('animation.mp4', fps=20, writer="avconv", codec="libx264")

plt.close(fig)