import socket

PORT=5051
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print(SERVER)
server.bind(ADDR)

print("The Server is starting..")


def handle_client(conn,addr):

    connected=True

    while connected:
        msg1=conn.recv(1024).decode()
        msg2=conn.recv(1024).decode()
        print(msg1)
        print(conn.send(msg1.encode()))

        if msg2.lower()=="n":
            connected=False

    conn.close()


def start():
    server.listen()
    conn,addr=server.accept()
    handle_client(conn,addr)

start()