# -*- coding: utf-8 -*-
"""
Created on Wed May 10 18:45:28 2017

@author: Alissa
"""

import re
#print(re.split(r'(s*)','here are some words'))
#print(re.split(r'[a-f][a-f]','hAjsvbodwhiwhpwlS',re.I|re.M))
print(re.findall(r'\d{1,5}\s\w+','oinwe324 main st.asdvse'))

import numpy as np
foo=np.random(100)