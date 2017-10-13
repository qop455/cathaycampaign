# -*- coding: utf-8 -*-
"""
@author: jason
"""
import pandas as pd
import mord
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
import split

def main():
    data = pd.read_csv('./final_data.csv')
    X_train, X_test, y_train, y_test = split.split(data)
    
    clf = mord.LogisticIT()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    
    print('accuracy_score:%06f'%accuracy_score(y_test, y_pred))
    print('precision_score:%06f'%precision_score(y_test, y_pred, average='macro'))
    print('recall_score:%06f'%recall_score(y_test, y_pred, average='macro'))
    
    target_names = ['VeryGood', 'Good', 'Fair', 'Bad', 'VeryBad']
    print('classification_report:', classification_report(y_test, y_pred, target_names=target_names))

if __name__ == '__main__':
    main()