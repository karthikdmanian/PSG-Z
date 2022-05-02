import socket

PORT=5051
SERVER="192.168.29.227"

client=socket.socket()
client.connect((SERVER,PORT))

while True:
    sms=input("Enter the message to the server.:")
    client.send(sms.encode())

    ch = input("Do you want to continue?")
    client.send(ch.encode())

    return_msg=client.recv(1024).decode()
    print(f"Msg from the server {return_msg}")
    if ch.lower()=="n":
        break


