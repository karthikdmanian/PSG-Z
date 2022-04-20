# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 10:34:39 2021

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



#socket.accept() Accept a connection.The socket must be bound to an address and listening for connections.The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection, and address is the address bound to the socket on the other end of the connection.

