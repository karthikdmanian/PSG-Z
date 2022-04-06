# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 11:14:10 2022

@author: 20pw16
"""

import socket
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverAddr=('localhost',9999)

opt='y'

while opt=='y' or opt=='Y':
    msg=input("Enter the message to be sent: ")
    c.sendto(bytes(msg,"utf-8"),serverAddr)
    Servermsg=c.recvfrom(1024)
    print("Message from Server: ",Servermsg[0].decode())
    op=input("Do you want to continue: ")
    opt=op
