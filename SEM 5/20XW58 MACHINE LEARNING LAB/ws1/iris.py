# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 14:49:25 2022

@author: 20pw16
"""

import pandas as pd

file = pd.read_csv(r"Z:/SEM 5/20XW58 MACHINE LEARNING LAB/ws1/datasets/iris.csv")
print(file)

# mean
meanSepalLength = file['SepalLengthCm'].mean();
meanSepalWidth = file['SepalWidthCm'].mean();
meanPetalLength = file['PetalLengthCm'].mean();
meanPetalWidth = file['PetalWidthCm'].mean();

meanSepalLength = "{:.2f}".format(meanSepalLength)
meanSepalWidth = "{:.3f}".format(meanSepalWidth)
meanPetalLength = "{:.2f}".format(meanPetalWidth)
meanPetalWidth = "{:.3f}".format(meanPetalWidth)

print(f"Mean : {meanSepalLength} , {meanSepalWidth} , {meanPetalLength} , {meanPetalWidth}")

# median
medianSepalLength = file['SepalLengthCm'].median();
medianSepalWidth = file['SepalWidthCm'].median();
medianPetalLength = file['PetalLengthCm'].median();
medianPetalWidth = file['PetalWidthCm'].median();

medianSepalLength = "{:.2f}".format(medianSepalLength)
medianSepalWidth = "{:.3f}".format(medianSepalWidth)
medianPetalLength = "{:.2f}".format(medianPetalWidth)
medianPetalWidth = "{:.3f}".format(medianPetalWidth)

print(f"Median : {medianSepalLength} , {medianSepalWidth} , {medianPetalLength} , {medianPetalWidth}")

# mode
modeSepalLength = file['SepalLengthCm'].mode();
modeSepalWidth = file['SepalWidthCm'].mode();
modePetalLength = file['PetalLengthCm'].mode();
modePetalWidth = file['PetalWidthCm'].mode();

# modeSepalLength = "{:.2f}".format(modeSepalLength)
# modeSepalWidth = "{:.3f}".format(modeSepalWidth)
# modePetalLength = "{:.2f}".format(modePetalWidth)
# modePetalWidth = "{:.3f}".format(modePetalWidth)

print(f"Mode : {modeSepalLength} , {modeSepalWidth} , {modePetalLength} , {modePetalWidth}")

# std
stdSepalLength = file['SepalLengthCm'].std();
stdSepalWidth = file['SepalWidthCm'].std();
stdPetalLength = file['PetalLengthCm'].std();
stdPetalWidth = file['PetalWidthCm'].std();

stdSepalLength = "{:.2f}".format(stdSepalLength)
stdSepalWidth = "{:.3f}".format(stdSepalWidth)
stdPetalLength = "{:.2f}".format(stdPetalWidth)
stdPetalWidth = "{:.3f}".format(stdPetalWidth)

print(f"std : {stdSepalLength} , {stdSepalWidth} , {stdPetalLength} , {stdPetalWidth}")

# skewness