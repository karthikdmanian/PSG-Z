import socket
import threading
import pickle


HEADER=64
PORT=8500
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER,PORT)

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(ADDR)

def handle_client(conn,addr):
    
    print(f"Client connected.{addr}")

    connected=True
    while connected:
        msg=conn.recv(1024).decode()

        print(f"This is the message received : {msg} .")

        server.send(msg)


    conn.close() 

def start():

    server.listen()
    print(f"the server is listening. . .")
    while True:
        conn, addr= server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"active connectiuons = {threading.active_count()-1}")

print("The server is starting..")
start()
