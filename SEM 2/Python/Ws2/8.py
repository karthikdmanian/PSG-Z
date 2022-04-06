# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 09:51:44 2021

@author: 20pw16
"""

A=set()
B=set()
n1=int(input("Enter the no of elements in set1:"))
n2=int(input("Enter the no of elements in set2:"))
print("ENter the elememts of the set1:")
for i in range(0,n1):
    ele=int(input())
    A.add(ele)
print("enter the elements of set 2:")
for i in range(0,n2):
    ele=int(input())
    B.add(ele)
print("the sets are :",A)
print(B)
print("The union is :",A|B)
print("The intersection is:",A&B)
print("THe difference is :",A-B)
print("The symmetric difference is:",A^B)