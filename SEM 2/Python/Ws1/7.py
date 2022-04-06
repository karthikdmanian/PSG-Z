# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 09:57:27 2021

@author: 20pw16
"""

str=input("Enter the sentence:")
alp="abcdefghijklmnopqrstuvwxyz";
f=0
for i in alp:
    if i not in str.lower():
        f=0
        break
    f=1
if(f==1):
    print("it is a pangram")
else:
    print("it is not a pangram")