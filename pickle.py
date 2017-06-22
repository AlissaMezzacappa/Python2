# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 15:03:22 2017
pickle
@author: Alissa
"""
#
import pickle
a=['test value','test value 2','test value 3']
file_Name='testfile'
fileObject=open(file_Name,'wb') #open for writing
pickle.dump(a,fileObject) #write to file
fileObject.close()
fileObject=open(file_Name,'r')
b=pickle.load(fileObject)
print(a==b)