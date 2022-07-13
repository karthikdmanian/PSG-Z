# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 14:49:25 2022

@author: 20pw16
"""

import pandas as pd

file = pd.read_csv(r"Z:/SEM 5/20XW58 MACHINE LEARNING LAB/ws1/datasets/iris.csv")
print(file)
print("Required SLcm   SWcm  PLcm  PWcm")
# mean
meanSepalLength = file['SepalLengthCm'].mean();
meanSepalWidth = file['SepalWidthCm'].mean();
meanPetalLength = file['PetalLengthCm'].mean();
meanPetalWidth = file['PetalWidthCm'].mean();

meanSepalLength = "{:.2f}".format(meanSepalLength)
meanSepalWidth = "{:.3f}".format(meanSepalWidth)
meanPetalLength = "{:.2f}".format(meanPetalWidth)
meanPetalWidth = "{:.3f}".format(meanPetalWidth)

print(f"Mean   : {meanSepalLength} , {meanSepalWidth} , {meanPetalLength} , {meanPetalWidth}")

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

modeSepalLength[0] = "{:.2f}".format(modeSepalLength[0])
modeSepalWidth[0] = "{:.3f}".format(modeSepalWidth[0])
modePetalLength[0] = "{:.2f}".format(modePetalWidth[0])
modePetalWidth[0] = "{:.3f}".format(modePetalWidth[0])

print(f"Mode   : {modeSepalLength[0]} , {modeSepalWidth[0]} , {modePetalLength[0]} , {modePetalWidth[0]}")

# std
stdSepalLength = file['SepalLengthCm'].std();
stdSepalWidth = file['SepalWidthCm'].std();
stdPetalLength = file['PetalLengthCm'].std();
stdPetalWidth = file['PetalWidthCm'].std();

stdSepalLength = "{:.2f}".format(stdSepalLength)
stdSepalWidth = "{:.3f}".format(stdSepalWidth)
stdPetalLength = "{:.2f}".format(stdPetalWidth)
stdPetalWidth = "{:.3f}".format(stdPetalWidth)

print(f"std    : {stdSepalLength} , {stdSepalWidth} , {stdPetalLength} , {stdPetalWidth}")

# skewness
skewSepalLength = file['SepalLengthCm'].skew()
skewSepalWidth = file['SepalWidthCm'].skew();
skewPetalLength = file['PetalLengthCm'].skew();
skewPetalWidth = file['PetalWidthCm'].skew();

skewSepalLength = "{:.2f}".format(skewSepalLength)
skewSepalWidth = "{:.3f}".format(skewSepalWidth)
skewPetalLength = "{:.2f}".format(skewPetalWidth)
skewPetalWidth = "{:.3f}".format(skewPetalWidth)

print(f"skew   : {skewSepalLength} , {skewSepalWidth} , {skewPetalLength} , {skewPetalWidth}")

# kurtosis
kurtSepalLength = file['SepalLengthCm'].kurt()
kurtSepalWidth = file['SepalWidthCm'].kurt();
kurtPetalLength = file['PetalLengthCm'].kurt();
kurtPetalWidth = file['PetalWidthCm'].kurt();

kurtSepalLength = "{:.2f}".format(kurtSepalLength)
kurtSepalWidth = "{:.3f}".format(kurtSepalWidth)
kurtPetalLength = "{:.2f}".format(kurtPetalWidth)
kurtPetalWidth = "{:.3f}".format(kurtPetalWidth)

print(f"kurt   : {kurtSepalLength} , {kurtSepalWidth} , {kurtPetalLength} , {kurtPetalWidth}")