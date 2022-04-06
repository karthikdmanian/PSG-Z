# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:21:22 2021

@author: 20pw16
"""

for i in range(1,101):
    if(i%5==0 and i%3==0):
        print(i,"FizzBuzz")
    elif(i%5==0):
        print(i,"Buzz")
    elif(i%3==0):
        print(i,"Fizz")