# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:16:34 2021

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
    if recvd.lower()=='bye':
        print("Goodbye")
        break
    else:
        print(f"Message from the server {recvd}")
        continue
s.close()