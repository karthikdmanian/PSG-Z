# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:30:37 2021

@author: 20pw16
"""

import socket
s = socket.socket()
host = socket.gethostname()
port = 65456

s.connect((host,port))

while True:
    recvd = s.recv(1024).decode() 
    print(f"{recvd}")
    break
s.close()