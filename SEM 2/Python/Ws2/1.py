# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:52:36 2021

@author: 20pw16
"""

str="hello world and practice makes perfect and hello world again"
strlist=str.split()
#print(strlist)
strlist=set(strlist)
print(strlist)
strlist=list(strlist)
strlist.sort()
for i in strlist:
    print(i,end=' ')