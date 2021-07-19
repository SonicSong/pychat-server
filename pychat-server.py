import socket
import os
import time
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

##TODO:

#give xxxxx^1 user 1
#if xxxxx^2 is not equal to xxxxxx^1 give user 2

#switch between users that allows to send data between them and not the same message sent
#example: user 1 sent "HI"
# user 2 sent "howdy"
# user 1 recv "HI"
# user 2 recv "howdy"



while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    
    start_new_thread(thread_cli, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
