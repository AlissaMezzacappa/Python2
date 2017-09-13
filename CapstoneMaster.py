"""re-write exploring DC
"""
import os
import pandas as pd
import numpy as np
import urllib
u=urllib.urlopen('http://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29')
text=u.read()
import re
matches=re.findall(r"\d+\.\s\w+", text)
del(matches[0:3])
del(matches[12])
for i in range(0, len(matches)):
    matches[i]=re.sub(r"\d+\.\s","",matches[i])
"""#local import
os.chdir('C:\Users\Alissa\Documents\Springboard\Capstone1\data\DrugConsumption') #cd and import data
data=pd.read_csv('drug_consumption.txt',header=None,names=matches) #also header=None"""
#web import
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00373/drug_consumption.data"
data = pd.read_csv(url,names=matches)
#print(data.head())
#make drug use binary instead  #code_dict={CL0:"Never Used", CL1:"Used over a Decade Ago",CL2:"Used in Last Decade",CL3:"Used in Last Year",CL4:"Used in Last Month", CL5:"Used in Last Week",CL6:"Used in Last Day"}
#month based binary variable
data=data.replace(['CL0','CL1','CL2','CL3'],0)
data=data.replace(['CL4','CL5','CL6'],1)
#1-13 are attributes 14-32 are drugs
attribute=data.iloc[:,:13]
#attribute.columns=[0,1,2,3,4,5,6,7,8,9,10,11,12]
drugs=data.iloc[:,13:] #CL4, CL5, CL6 are use in last month, week, day respectively
#drugs.columns=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
print(attribute.head())
print(drugs.head())

coormat=data.corr()


#To try: XG Boost or boosting - tree tech.
#"""
# Compare Algorithms
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
# prepare configuration for cross validation test harness
seed = 7
# prepare models
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
#rename data
X=attribute
Y=drugs.iloc[:,:17]
# evaluate each model in turn
results = []
names = []
scoring = 'accuracy'
count=0      
#n=0     
#val=[]
#best2=[]
for name in Y.columns:
   y = Y[name]
   print(name)
   for name, model in models:
    	kfold = model_selection.KFold(n_splits=10, random_state=seed)
    	cv_results = model_selection.cross_val_score(model, X, y, cv=kfold, scoring=scoring) #ValueError: bad input shape (1696, 19)
    	results.append(cv_results)
    	names.append(name)
    	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    	print(msg)
#   for i in xrange(0,5):
#       val[i]=results[6*n].mean()+ results[6*n].std()
#   best2=val.sort_values().head(2)
#   # boxplot algorithm comparison
#   fig = plt.figure()
#   fig.suptitle('Algorithm Comparison')
#   ax = fig.add_subplot(111)
#   plt.boxplot(results[count]) #list call by row - not working
#   ax.set_xticklabels(names)
#   plt.show()
#   count=count+1
#"""