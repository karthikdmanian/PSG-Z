# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 14:58:08 2021

@author: 20pw16
"""

import socket

s = socket.socket()
host = socket.gethostname()
port = 65456

s.bind((host,port))

s.listen(5)
while True:
        c, addr = s.accept()
        while True:
            message = c.recv(1024).decode()
            if message.lower() == 'bye':
                c.send("Goodbye".encode())
                break
            else:
                c.send(message[::-1].encode())
c.close()
