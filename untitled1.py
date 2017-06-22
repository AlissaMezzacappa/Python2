# -*- coding: utf-8 -*-
"""
Created on Sun May 14 14:01:17 2017
@author: Alissa
"""
#import os
#cd1=os.getcw()
#print cd1
#cd2=os.chdir('C:\Users\Alissa\Documents\Spingboard\Capstone 1\data')
##change directory to this one
#print cd2
#import pandas as pd
#import pickle
##open 'drug_consumption.data'
#open('drug_consumption.data','r')
import os
import pickle
mylist = ["This", "is", 4, 13327]
# Open the file C:\\binary.dat for writing. The letter r before the
# filename string is used to prevent backslash escaping.
os.chdir('C:\Users\Alissa\Documents\Spingboard\Capstone 1\data\Drug Consumption')
print(os.getcw())
myfile = open('test.txt', "w")
#pickle.dump(mylist, myfile)
#myfile.close()
#
#myfile = open(r"C:\\text.txt", "w")
#myfile.write("This is a sample string")
#myfile.close()
#
#myfile = open(r"C:\\text.txt")
# print(myfile.read())
#'This is a sample string'
#myfile.close()

## Open the file for reading.
#myfile = open(r"C:\\binary.dat")
#loadedlist = pickle.load(myfile)
#myfile.close()
# print(loadedlist)
#['This', 'is', 4, 13327]