# -*- coding: utf-8 -*-
"""
Created on Wed May 31 19:29:39 2017

@author: Alissa
"""

import urllib
u=urllib.urlopen('http://www.google.com/')
te=u.read()
import re
pat=r'[a-z]'
m11=re.search(pat,str(te))
for 
print(m11.group())
print(m11.span())

