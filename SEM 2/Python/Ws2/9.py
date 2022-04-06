# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 10:08:56 2021

@author: 20pw16
"""

s=set()
s.add("White")
s.add("Yellow")
s.add("Red")
s.add("Blue")
s.add("Green")
s.remove("Red")
print(s)
a=0
for i in s:
    if i=="Yellow":
        a=1
        break
if(a==0):
    print("N")
else:
    print("Y")
        