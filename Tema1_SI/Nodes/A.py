import socket
from Node import *
from CryptoUtils import OFBUtil, ECBUtil, AESUtil

mode = ''
K = b''
enc_k = b''


def set_mode():
    # Waits for the input from the console setting the encryption ode that will be used
    global mode
    while not mode:
        num = input("Choose mode:\n1. ECB\n2. OFB\n")
        if num == '1':
            mode = 'ECB'
        elif num == '2':
            mode = 'OFB'
        else:
            print("Wrong id")


def send_mode(sock):
    # Sends the mode through he socket 'sock'
    global mode
    sock.send(bytes(mode, 'utf-8'))
    print("Mode sent to B")


def get_key(sock):
    # Takes the key through the socket 'sock'
    global enc_k, K
    enc_k = sock.recv(16)
    print("Key received from KM")
    K = AESUtil.decrypt(enc_k, K1)


def send_key(sock):
    # Sends the key through socket 'sock'
    sock.send(enc_k)
    print("Key sent to B")


def connect(port):
    # creates a connection through the port 'port' and returns the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP, port))
    print(f"Connected to {IP}:{port}")
    return sock


def wait_signal(sock):
    # Waits for a signal of size 2 through the socket 'sock'
    sock.recv(2)
    print("Start signal received")


def encrypt_message(text):
    # Encrypts the message using the selected mode
    if mode == 'ECB':
        message = ECBUtil.encrypt(text, K)
    else:
        message = OFBUtil.encrypt(text, iv, K)
    return message


def send_text(sock):
    # waits for a signal and then sends and encrypted message through socket 'sock'
    wait_signal(sock)
    f = open("text.txt", "rb")
    text = f.read()
    enc_text = encrypt_message(text)
    print("Message encrypted")
    sock.send(len(enc_text).to_bytes(4, 'big'))
    print("Message size sent")
    sock.send(enc_text)
    print("Message sent")


if __name__ == "__main__":
    set_mode()
    s = connect(PORT_KM)
    s1 = connect(PORT_B)
    send_mode(s1)
    get_key(s)
    s.close()
    print("Connection with KM closed.")
    send_key(s1)
    send_text(s1)
    s1.close()
    print("Connection with B closed.\n")
