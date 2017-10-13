# -*- coding: utf-8 -*-
"""
@author: jason
"""

from sklearn.model_selection import train_test_split
import pandas as pd

def split(data):
    
    data.drop(data[data['Wales'] == 1].index, inplace=True)
    data.drop(data[data['Health'] == -9].index, inplace=True)
    data.drop(['Wales'], inplace=True, axis=1)
    data['Health'] = data['Health'].map({1:1, 2:1, 3:0, 4:0, 5:0})
    
    feature, target = data[data.columns[:-1]], data['Health']
    X_train, X_test, y_train, y_test = train_test_split(feature, target, test_size=0.1, random_state=42)
    
    train = pd.concat([X_train, pd.DataFrame({'Health':y_train})], axis=1)
    
    good = train[train['Health'] == 1]
    bad = train[train['Health'] == 0]
    
    good_sample = good.sample(n=bad.Health.count(), replace=True)
    sample = pd.concat([good_sample, bad], axis=0, ignore_index=True)
    sample = sample.sample(frac=1).reset_index(drop=True)
    
    X_sample, y_sample = sample[sample.columns[:-1]], sample['Health']
    
    return  X_sample, X_test, y_sample, y_test
    
def concat_to_csv(X_train, X_test, y_train, y_test, train_path = './train.csv', test_path = './test.csv'):
    train = pd.concat([X_train, pd.DataFrame({'Health':y_train})], axis=1)
    test = pd.concat([X_test, pd.DataFrame({'Health':y_test})], axis=1)
    train.to_csv(train_path, index=False)
    test.to_csv(test_path, index=False)

if __name__ == '__main__':
    '''
    dataframe = pd.read_csv('./final_data.csv')
    X_train, X_test, y_train, y_test = split(dataframe)
    concat_to_csv(X_train, X_test, y_train, y_test)
    '''