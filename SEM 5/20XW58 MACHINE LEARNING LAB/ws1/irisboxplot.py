# -*- coding: utf-8 -*-
"""Created on Tue Jul 19 14:51:48 2022@author: 20pw16"""

import pandas as pd
import numpy as np
import seaborn as sns
file = pd.read_csv(r"Z:/SEM 5/20XW58 MACHINE LEARNING LAB/ws1/datasets/iris.csv")

# sepalLength box plot for classes
sns.catplot(x="Species",y="SepalLengthCm",data=file,kind="box",col="Species")
sns.catplot(x="Species",y="SepalWidthCm",data=file,kind="box",col="Species")
sns.catplot(x="Species",y="PetalLengthCm",data=file,kind="box",col="Species")
sns.catplot(x="Species",y="PetalWidthCm",data=file,kind="box",col="Species")

q1 = np.percentile(file["SepalLengthCm"][:51],25,axis=0)