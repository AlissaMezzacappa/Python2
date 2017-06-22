# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:24:20 2017

@author: Alissa
"""
import re
import urllib
sites='google yahoo cnn msn'.split()
pat=re.compile(r'<title>+.*</title>+',re.I|re.M) 
#makes compiled version of pattern rather than recreate it everytime
for s in sites:
    print('Searching: ' + s)
    try:
        u=urllib.urlopen('http://' + s + '.com')
#    except: #this is for python 3
#        u=urllib.request.urlopen('http://' + s + '.com')
    te=url.read()
    title = re.findall(pat, str(te))
    print(title[0])