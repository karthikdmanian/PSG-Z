# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 10:34:50 2021

@author: 20pw16
"""

import socket
s = socket.socket()
host = socket.gethostname()
port = 65456

s.connect((host,port))

while True:
    msg = input("Please enter a message to the server: ")
    s.send(msg.encode())
    recvd = s.recv(1024).decode() 
    print(f"Message from the server {recvd}")
    ch=input("Do you want to continue?")
    #s.send(ch.encode())
    if ch.lower()=='n':
        break
    else:
        continue
s.close()