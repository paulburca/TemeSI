import os
import socket
from CryptoUtils import AESUtil
from Node import *

# connects to the server, generates a new key and sends it back
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP, PORT_KM))
    while True:
        s.listen()
        print("Listening for connections")
        conn, _ = s.accept()
        print("Connected to A")
        K = os.urandom(16)
        print("Key randomized")
        conn.send(bytes(AESUtil.encrypt(K, K1)))
        print("Key encrypted and sent")
        conn.close()
        print("Connection closed")

