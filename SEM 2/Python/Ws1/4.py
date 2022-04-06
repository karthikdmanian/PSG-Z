# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 09:27:12 2021

@author: 20pw16
"""

str=input("enter the string:")
pos=int(input("Enter the position to be modified:"))
chr=input("Enter the char to be replaced:")
p=-1
for i in str:
   p=p+1
   if(p==pos):
      