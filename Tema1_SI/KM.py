import os
import socket
import AESUtil
import Node

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((Node.IP, Node.PORT_1))
    s.listen()
    conn, _ = s.accept()
    K = os.urandom(16)
    conn.send(bytes(AESUtil.encrypt_AES(K, Node.K1)))
    conn.close()
