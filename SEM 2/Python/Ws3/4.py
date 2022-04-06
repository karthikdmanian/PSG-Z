# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:22:52 2021

@author: 20pw16
"""
for i in range(3,101):
    for j in range(4,101):
        for k in range(5,101):
            if(i**2+j**2==k**2):
                print(i,j,k)
        