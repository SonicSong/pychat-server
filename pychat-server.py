import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 8080
ThreadCount = 0

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection...')
ServerSocket.listen(5)

def thread_cli(connection):
    connection.send(str.encode('Welcome to the server'))
    while True:
        data = connection.recv(2048)
        print(data)
        reply = 'Server says: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
        print(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(thread_cli, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
