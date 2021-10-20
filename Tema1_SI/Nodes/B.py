import socket
from Node import *
from CryptoUtils import OFBUtil, ECBUtil, AESUtil

K = b''
mode = ''


def get_mode(conn):
    # gets the mode through connection 'conn'
    return conn.recv(3).decode()


def get_key(conn):
    # gets the key and decrypts it
    global K
    enc_k = conn.recv(16)
    K = AESUtil.decrypt(enc_k, K1)


def send_signal(conn):
    # sends the signal
    conn.send(bytes("GO", 'utf-8'))


def get_text(conn):
    # reads the text sent through connection 'conn'
    size = conn.recv(4)
    text = conn.recv(int.from_bytes(size, 'big'))
    return text


def decrypt_text(text):
    # decrypts the text using selected mode
    if mode == 'ECB':
        return ECBUtil.decrypt(text, K)
    else:
        return OFBUtil.decrypt(text, iv, K)


def get_data(conn):
    # gets the data from the server and decrypts it
    global mode
    mode = get_mode(conn)
    print("Mode received")
    get_key(conn)
    print("Key received")
    send_signal(conn)
    print("Sent start signal")
    text = get_text(conn)
    print("Message received")
    dec_text = decrypt_text(text)
    print("Message decrypted\n")
    return dec_text


def accept_conn():
    # connects to server, gets data, decrypts it and prints it
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((IP, PORT_B))
        s.listen()
        print("Waiting for connections")
        conn, _ = s.accept()
        print("Connected to A")
        message = get_data(conn)
        print("The message:\n" + message.decode())
        conn.close()


accept_conn()
