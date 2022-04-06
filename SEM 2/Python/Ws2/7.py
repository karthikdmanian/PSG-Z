# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 09:21:49 2021

@author: 20pw16
"""
B1=set()
B2=set()
A={1,2,3,4,5,6,7,8}
B={1,3,2,4,6,7,5,9}
if A == B:
    print("Sets are equal")
else:
    for i in B:
        if(i not in A):
            B1.add(i)
    for i in A:
        if(i not in B):
            B2.add(i)
print(B1)
print(B2)        
