# -*- coding: utf-8 -*-
"""
@author: jason
"""

import split
import pandas as pd
import xgboost as xgb
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
import time

def main():
    data = pd.read_csv('./final_data.csv')
    
    X_train, X_test, y_train, y_test = split.split(data)
    
    dtrain = xgb.DMatrix(X_train.values, y_train.values)
    dtest = xgb.DMatrix(X_test.values, y_test.values)

    # specify parameters via map, definition are same as c++ version
    param = {'max_depth':6, 'objective':'binary:logistic' }
    
    t = time.time()
    # specify validations set to watch performance
    watchlist  = [(dtest,'eval'), (dtrain,'train')]
    num_round = 6
    bst = xgb.train(param, dtrain, num_round, watchlist)
    
    # this is prediction
    preds = bst.predict(dtest)
    labels = dtest.get_label()
    y_preds = [1 if preds[i]>0.5 else 0 for i in range(len(preds))]
    
    print('-' * 20 + 'Result' + '-' * 20)
    print('accuracy_score:%06f %%'%(accuracy_score(y_test, y_preds) * 100))
    print('precision_score:%06f %%'%(precision_score(y_test, y_preds, average='macro') * 100))
    print('recall_score:%06f %%'%(recall_score(y_test, y_preds, average='macro') * 100))
    
    target_names = ['Bad', 'Good']
    print('\n')
    print('classification_report:', classification_report(y_test, y_preds, target_names=target_names))
    print("Time %d s"%(time.time()-t))
    return

    t = time.time()
    # sklearn method
    bst_sklearn = xgb.XGBClassifier()
    bst_sklearn.fit(X_train, y_train)
    preds_sklearn = bst_sklearn.predict(X_test)
    
    print('-' * 20 + 'Result' + '-' * 20)
    print('accuracy_score:%06f %%'%(accuracy_score(y_test, preds_sklearn) * 100))
    print('precision_score:%06f %%'%(precision_score(y_test, preds_sklearn, average='macro') * 100))
    print('recall_score:%06f %%'%(recall_score(y_test, preds_sklearn, average='macro') * 100))
    
    target_names = ['Bad', 'Good']
    print('\n')
    print('classification_report:', classification_report(y_test, preds_sklearn, target_names=target_names))
    print("Time %d s"%(time.time()-t))
    
if __name__ == '__main__':
    main()