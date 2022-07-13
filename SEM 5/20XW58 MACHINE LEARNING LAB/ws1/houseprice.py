# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 09:18:38 2022

@author: 20pw16
"""

import pandas as pd

file = pd.read_csv(r"Z:/SEM 5/20XW58 MACHINE LEARNING LAB/ws1/datasets/houseprice.csv")
# print(file)

print(file.describe())

print("Skewness")
print(file.skew())

print("Kurtosis")
print(file.kurt())