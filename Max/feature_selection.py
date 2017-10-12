# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:18:02 2017

@author: user
"""

import pandas as pd

#df = pd.read_csv('C:\\Users\\user\\Downloads\\國泰\\01.2011_Census_Microdata.csv')



#Feature Importance
from sklearn.svm import LinearSVC
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel
from sklearn import linear_model
from sklearn.ensemble import ExtraTreesClassifier

iris = load_iris()
X, y = iris.data, iris.target
print(X.shape)

#clf = LinearSVC(C=0.01, penalty="l1", dual=False).fit(X, y)

clf = ExtraTreesClassifier().fit(X, y)
print(clf.feature_importances_ )

#clf = linear_model.Lasso(alpha=0.9).fit(X, y)
model = SelectFromModel(clf, prefit=True)
X_new = model.transform(X)
print(X_new.shape)