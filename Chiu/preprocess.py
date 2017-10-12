# -*- coding: utf-8 -*-
"""
@author: jason
"""

import pandas as pd
import modict as mo

data = pd.read_csv("../raw_data/Census_Microdata.csv")
data.drop(['Person ID', 'Health'], inplace=True, axis=1)

feature_dummy_dict = mo.get_dummy_dict()
feature_value_dict = mo.get_value_dict()

for key, value in feature_dummy_dict.items():
    new_dummy = pd.get_dummies(data[key])
    new_dummy = new_dummy.rename(columns=value)
    data.drop([key], inplace=True, axis=1)
    data = pd.concat([data, new_dummy], axis=1)

data.drop(['NotRequired'], inplace=True, axis=1)

for key, value in feature_value_dict.items():
    data[key] = data[key].map(value)

Occupation = pd.get_dummies(data['Occupation']).rename(columns = lambda col: 'Occupation_%s'%col)
Industry = pd.get_dummies(data['Industry']).rename(columns = lambda col: 'Industry_%s'%col)

data = pd.concat([data, Occupation, Industry], axis=1)

data.drop(['Occupation', 'Industry', 'Occupation_-9', 'Industry_-9'], inplace=True, axis=1)

data.to_csv('../data/dummy_data.csv', index=False)
