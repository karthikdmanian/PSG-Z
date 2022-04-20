# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:16:31 2021

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
            if message:
                c.send(message.encode())
              
c.close()