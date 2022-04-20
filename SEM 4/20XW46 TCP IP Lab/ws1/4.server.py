# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:17:37 2021

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
            res = ''.join(format(ord(i), '08b') for i in message)
            c.send(res.encode())
              
c.close()