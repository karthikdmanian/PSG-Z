# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:30:35 2021

@author: 20pw16
"""

import socket
from datetime import datetime
today=datetime.today()
now=datetime.now()

current_time = now.strftime("%H:%M:%S")
d2 = today.strftime("%B %d, %Y")

s = socket.socket()
host = socket.gethostname()
port = 65456

s.bind((host,port))

s.listen(5)
while True:
        c, addr = s.accept()
        print(f"Got connection from {addr}")
        while True:
            c.send(f"Time i got from the server {d2} {current_time}".encode())
              
c.close()