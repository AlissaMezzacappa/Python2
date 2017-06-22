# -*- coding: utf-8 -*-
"""
Created on Wed May 10 18:45:28 2017

@author: Alissa
"""

import re
#print(re.split(r'(s*)','here are some words'))
#print(re.split(r'[a-f][a-f]','hAjsvbodwhiwhpwlS',re.I|re.M))
print(re.findall(r'\d{1,5}\s\w+\s\w+\.','oinwe324 main st.asdvse'))
print(re.findall('r\d{1-9}','9g8ggd9'))
#te='ab2k9221hf'
#pat=r'[a-z]'
#m11=re.search(r'[a-z]',str(te))
#print(m11.group())
#print(m11.span())
print(re.findall('r[1-9]','34kjjj2j1'))
