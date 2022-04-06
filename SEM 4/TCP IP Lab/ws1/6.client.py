# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:50:27 2021

@author: 20pw16
"""

import socket
import pickle

s = socket.socket()
host = socket.gethostname()
port = 65456

s.connect((host,port))

while True:
    recvd = s.recv(1024) 
    print(pickle.loads(recvd))
    break
s.close()