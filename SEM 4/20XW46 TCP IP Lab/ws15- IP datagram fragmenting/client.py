import socket
import pickle

<<<<<<< HEAD
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1243))
=======
HEADER = 64 #to receive message sizing every message at recv() to 64 and padding it
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #getting the IP address
DISCONNECT_MESSAGE = "bye"
ADDR=(SERVER,PORT)
>>>>>>> 18496913fb31def74731ab4f96fe77e20fe502b7

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

<<<<<<< HEAD
        print(f"full message length: {msglen}")

        full_msg += msg

        print(len(full_msg))

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            print(pickle.loads(full_msg[HEADERSIZE:]))
            new_msg = True
            full_msg = b""
=======
def send(msg):
    message =msg.encode('utf-8')
    msg_length = len(message)
    send_length = str(msg_length).encode('utf-8')
    send_length+= b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    ret_msg=client.recv(HEADER).decode('utf-8')
    print(ret_msg)

d=[12,3,4]
msg = pickle.dumps(d)
msg = bytes(f"{len(msg):<{HEADER}}", 'utf-8')+msg

send(msg)
# send("warudoooo")
# send("bye")
>>>>>>> 18496913fb31def74731ab4f96fe77e20fe502b7
