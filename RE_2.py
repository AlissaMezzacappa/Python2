# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 14:40:31 2017
Regular expressions span & group
@author: Alissa
"""
import re
p = re.compile('[a-z]+')
foo='hkl98h2221hk'
#print( p.match('::: message')
#m = p.search('::: message') ; print m
print(foo.findall())
##print(m.span())
#for match in str(foo):
#    print match.span()