import socket
import threading

PORT=8000
buffer_size=8192

# setting up the server
server=socket.socket()
server.bind(('',PORT))

def proxy_server(webserver,port,conn,data,addr):
    server=socket.socket()
    server.connect((webserver,port))
    server.send(data.encode())

    while True:
        reply = server.recv(8192)

        if reply:
            conn.send(reply)
            print(reply)

    conn.close()


def handle_client(conn,addr,data):
    first_line=data.split("\n")[0]
    url = first_line.split(" ")[1]

    http_pos = url.find("://")
    print(f"This is the first line {first_line}\n,This is the url {url}]n,THis is the http positrion {http_pos}")

    temp=url
    # if http_pos == -1:
    #     temp = url
    # else:
    #     temp = url[(http_pos+3)]
    #     print(f"Temp is the else part {temp}")

    port_pos = temp.find(":")

    webserver_pos=temp.find('/')

    if webserver_pos == -1:
        webserver_pos = len(temp)
    webserver=""
    port=-1

    if port_pos == -1 or webserver_pos<port_pos:
        port=80
        webserver = temp[:webserver_pos]
    else:
        port=int(temp[(port_pos+1):] [:webserver_pos-port_pos-1])
        webserver=temp[:port_pos]

    print(webserver)
    proxy_server(webserver,port,conn,data,addr)



def start():
    server.listen()
    print(f"server is listening on {PORT}")

    while True:
        conn, addr = server.accept()
        data=conn.recv(8192).decode()
        print(f"this is the DATA {data}")
        thread = threading.Thread(target=handle_client, args=(conn, addr, data))
        thread.start()
        print(f"active connectiuons = {threading.active_count() - 1}")

print("Server is starting...")
start()