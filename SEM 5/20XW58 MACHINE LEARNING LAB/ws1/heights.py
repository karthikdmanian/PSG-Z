# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:16:01 2022

@author: 20pw16
"""
import numpy as np
import pandas as pd

file = pd.read_csv(r"Z:/SEM 5/20XW58 MACHINE LEARNING LAB/ws1/datasets/20pw.csv")
print(file)

boxplot = file.boxplot(figsize=(6,6))

q1=np.percentile(file,25)
q3=np.percentile(file,75)

IQR=q3-q1

lower=q1-1.5*IQR
upper=q3+1.5*IQR

print(lower,upper)