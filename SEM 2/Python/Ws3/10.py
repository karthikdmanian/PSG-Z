# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:40:46 2021

@author: 20pw16
"""

num=int(input("Enter the Number:"))
dig=0
while(1):
    num=num/10
    dig+=1
    if(num%10==0):
        break
print("The no of digits in the numbr is:",dig)