# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 11:33:32 2022

@author: 20pw16
"""

#!/usr/bin/env python

from socket import *
import sys

s = socket(AF_INET,SOCK_DGRAM)
host =sys.argv[1]
port = 9999
buf =1024
addr = (host,port)

file_name=sys.argv[2]

f=open(file_name,"rb") 
data = f.read(buf)

s.sendto(file_name,addr)
s.sendto(data,addr)
while (data):
    if(s.sendto(data,addr)):
        print("sending ...")
        data = f.read(buf)
s.close()
f.close()