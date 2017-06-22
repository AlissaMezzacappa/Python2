# -*- coding: utf-8 -*-
"""
Created on Wed May 31 20:59:25 2017
Reading and Writing
@author: Alissa
"""
import os
os.chdir('C:\Users\Alissa\Documents\Spingboard') #change directory
cwd=os.getcwd()
print(cwd)
#foo=os.listdir('.')
#print(foo)
f=open('testfile.txt','w')
#print(f.mode)
#print(f.name)
print(f)
f.write('Hello World\n')
f.write('This is our new text file\n')
f.write('and this is another line.\n')
f.close()
f=open('testfile.txt','r')
#print(f.read()) #one or the other for some reason
#print(f.read(5)) #DNW
#print( f.readline(11)) #not reading line 11 reading first 11 char
#foofoo=f.readlines() #DNW
#print(foofoo) #DN seperate lines
#f=open('testfile.txt','r')
#for line in f:
#    print line, #DN seperate lines
file=open('testfile.txt','a')
file.write('This is a test\n')
file.write('To add more lines.\n')
file.close()    #Best practice
f=open('testfile.txt','r')
#for line in f:
#    print line, #Output in iPython Console
#with open('testfile.txt') as file:  
#    data = file.read() 
##for line in file:
##    print(line), #DNW
#    #examples
##    with open('hello.txt', 'w') as f: 
##        f.write('Hello World') 
#with open('testfile.txt') as f: 
#    data = f.readlines() 
##splitting lines
with open('testfile.txt', 'r') as f:
    data=f.readlines()
    print( data)
##for line in data:
##    words = line.split()
##print words