# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 20:01:30 2017

@author: Alissa
"""

import re
text = "He was carefully disguised but captured quickly by police."
for m in re.finditer(r"\w+ly", text): 
    print '%02d-%02d: %s' % (m.start(), m.end(), m.group(0))
print(re.findall(r"\w+ly", text))
    