# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 16:48:54 2017

@author: Alissa
"""
import urllib
u=urllib.urlopen('http://www.google.com/')
te=u.read()
import re
p = re.compile(te)
iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')

for match in iterator:
    print match.span()