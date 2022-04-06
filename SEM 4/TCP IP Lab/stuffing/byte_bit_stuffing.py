# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 10:59:21 2022

@author: 20pw16
"""

s=input("enter the string:")
byteStuff=""

for i in s.split():
    if i=="ESC":
        byteStuff+="ESC ESC "
    elif i=="FLAG":
        byteStuff+="ESC FLAG "
    else:
        byteStuff+=i+" "

print(f"this is data after bytestuffing:\n {byteStuff}")

bitStuff=""

for i in byteStuff.split():
    
    if i=='ESC':
        bitStuff+='10100011 '
    elif i=='FLAG':
        bitStuff+='01111110 '
    elif ord(i)>=65 and ord(i)<=90:
        bitStuff+=format(int(bin(ord(i))[2:]),'#0008')+' '
        
print(f"this is binary data before bitstuffing:\n {bitStuff}")

#bitStuff=bitStuff.strip(" ")

#print(f"this is binary data before bitstuffing:\n {bitStuff}")

for i in bitStuff.split():
    if '11111' in i:
        bitStuff=bitStuff.replace('11111','111110')

print(f"this is binary data after bitstuffing:\n {bitStuff}")

#UNSTUFFING
for i in bitStuff.split():
    if '111110' in i:
        bitStuff=bitStuff.replace('111110','11111')
        
print(f"this is binary data after bitunstuffing:\n {bitStuff}")

unStuff=""

for i in bitStuff.split():
    if i=='10100011':
        unStuff+='ESC '
    elif i=='01111110':
        unStuff+='FLAG '
    else:
        unStuff+=chr(int(i,2))+' '
        
unStuff=unStuff.replace('ESC ESC','ESC')
unStuff=unStuff.replace('ESC FLAG','FLAG')

print(f"this is data after unstuffing:\n {unStuff}")
