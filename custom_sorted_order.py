# -*- coding: utf-8 -*-
"""
Created on Wed May 31 08:42:20 2017

@author: Alissa
"""

colors = [ 'green', 'yellow', 'blue','red']
#
#def compare_length(c1, c2):
#    if len(c1) < len(c2): return -1
#    if len(c1) > len(c2): return 1
#    return 0
#
#print sorted(colors, cmp=compare_length)

print sorted(colors, key=len)