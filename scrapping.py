# -*- coding: utf-8 -*-
"""
Created on Wed May 31 19:29:39 2017

@author: Alissa
"""

import urllib
u=urllib.urlopen('http://www.msn.com/')
te=u.read()
import re
pat='title'
title = re.findall(pat, str(te))
print(title)

