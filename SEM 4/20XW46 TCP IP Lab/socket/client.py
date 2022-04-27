import socket

HEADER = 64 #to receive message sizing every message at recv() to 64 and padding it
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #getting the IP address
DISCONNECT_MESSAGE = "bye"
ADDR=(SERVER,PORT)

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message =msg.encode('utf-8')
    msg_length = len(message)
    send_length = str(msg_length).encode('utf-8')
    send_length+= b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    ret_msg=client.recv(HEADER).decode('utf-8')
    print(ret_msg)

send("helloo")
send("warudoooo")
send("bye")