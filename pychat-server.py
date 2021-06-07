import socket
import os
from _thead import *
    #socket
    # TCP server code

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 8080
ThreadCount = 0

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))



#host="localhost"
#port=8080

#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#sock.bind((host, port))

#sock.listen(1000)
#print("listening for connections...")
#client,address = sock.accept()
#print(f"{address} just connected!")

#while True:
#    try:      
