import socket
<<<<<<< HEAD
import time
import pickle


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1243))
s.listen(5)

while True:

    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    d = {1:"hi", 2: "there"}
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    print(msg)
    clientsocket.send(msg)

=======
import threading

HEADER = 64 #to receive message sizing every message at recv() to 64 and padding it
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #getting the IP address
ADDR = (SERVER,PORT)
DISCONNECT_MESSAGE = "bye"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET - IPv4 , SOCK_STREAM - TCP
# print(type(server))
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"New connection {addr} connected.")

    connected = True
    while connected:
        msg_length =conn.recv(HEADER).decode('utf-8') #measuring length
        if msg_length:
            msg_length=int(msg_length) #converting it to integer
            msg=conn.recv(msg_length).decode('utf-8') #bytes of message to be received
            if msg==DISCONNECT_MESSAGE:
                connected=False
                

            print(f"{addr} : {msg}")

            conn.send("Message Received !!!".encode('utf-8'))

    conn.close()
def start():
    server.listen()
    print(f"server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"active connectiuons = {threading.active_count()-1}")

print("server is starting ... ")
start()
>>>>>>> 18496913fb31def74731ab4f96fe77e20fe502b7
