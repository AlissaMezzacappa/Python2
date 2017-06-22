# -*- coding: utf-8 -*-
"""
Created on Tue May 30 17:51:18 2017

@author: Alissa
"""
#Idiomatic Python
colors = ['red','green','blue','yellow']
for i in range(len(colors)-1,-1,-1):
    print colors[i]
#print('For looping over a range of numbers')
#for i in [0, 1, 2, 3, 4, 5]:
#    print i**2
#for i in range(6):
#    print i**2
#
##>>Better
#for i in xrange(6):
#    print i**2
#
#print('For Looping over a collection')
#colors = ['red', 'green', 'blue', 'yellow']
#
#for i in range(len(colors)):
#    print colors[i]
#    
###>>Better
#for color in colors:
#    print color
##How do i program clear?
#print('Looping Backwards')
#colors = ['red', 'green', 'blue', 'yellow']
#
#for i in range(len(colors)-1, -1, -1):
#    print colors[i]
    ##
#print('Looping over two collections')
##Basic Way
#names = ['raymond', 'rachel', 'matthew']
#colors = ['red', 'green', 'blue', 'yellow']
#n = min(len(names), len(colors))
#for i in range(n):
#    print names[i], '--->', colors[i]

#for name, color in zip(names, colors):
##Better way
#for name, color in izip(names, colors):
#    print name, '--->', color

#print('Looping in sorted order')
colors = ['red', 'green', 'blue', 'yellow']
## Forward sorted order
#for color in sorted(colors):
#    print colors

#print( 'Backwards sorted order)
#for color in sorted(colors, reverse=False):
#    print colors
#Cutom Sort Order
colors = ['red', 'green', 'blue', 'yellow']

def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0

print sorted(colors, cmp=compare_length)
#Better # Key function
print sorted(colors, key=len)