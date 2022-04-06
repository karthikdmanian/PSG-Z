# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 12:04:50 2021

@author: 20pw16
"""

str=input("enter the word:")
ns=''
for i in str:
    ns+='_'
print(ns)
ns=list(ns)
n=1
att=0
while(n):
    atmp=input("guess the char:")
    att+=1
    k=0
    for i in str:
        k+=1
        if atmp==i:
            ns[k-1]=i
            break
    for i in ns:
        print(i,end='')
    for i in ns:
        if i=='_':
            n=1
            break
        else:
            n=0
print()
print("the no of attempts taken is :",att)