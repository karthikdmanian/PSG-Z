# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 11:33:30 2022

@author: 20pw16
"""

from socket import *
import sys
import select

host="0.0.0.0"
port = 9999
s = socket(AF_INET,SOCK_DGRAM)
s.bind((host,port))

addr = (host,port)
buf=1024

f = open("file.pdf",'wb')

data,addr = s.recvfrom(buf)
try:
    while(data):
        f.write(data)
        s.settimeout(2)
        data,addr = s.recvfrom(buf)
except timeout:
    f.close()
    s.close()
    print("File Donwloaded")