# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 09:36:28 2021

@author: 20pw16
"""

no=int(input("enter the num to be checked:"))
f=0
for i in range(2,int(no/2)):
    if(no%i==0):
        print("Composite num")
        f=1
        break
if(f==0):
    print("Prime Number")
    