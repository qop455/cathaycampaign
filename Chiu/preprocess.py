# -*- coding: utf-8 -*-
"""
@author: jason
"""

import pandas as pd
import numpy as np
import modict as mo


data = pd.read_csv("../raw_data/Census_Microdata.csv")

feature_dummy_dict = mo.get_dummy_dict()
feature_value_dict = mo.get_value_dict()

for key, value in feature_dummy_dict.items():
    new_dummy = pd.get_dummies(data[key])
    new_dummy = new_dummy.rename(columns=value)
    data = pd.concat([data, new_dummy], axis=1)

for key, value in feature_value_dict.items():
    for k, v in value.items():
        data[key][data[key] == k].set

