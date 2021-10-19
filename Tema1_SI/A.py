import socket
import Node
import AESUtil
import ECBUtil
import OFBUtil

mode = 'ECB'
K = b''
enc_k = b''


def set_mode(m):
    global mode
    mode = m


def send_mode(sock):
    global mode
    sock.send(bytes(mode,'utf-8'))


def get_key(sock):
    global enc_k, K
    enc_k = sock.recv(16)
    K = AESUtil.decrypt_AES(enc_k, Node.K1)


def connect_b(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((Node.IP, port))
    return sock


def connect_km(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((Node.IP, port))
    return sock


def wait_signal(sock):
    sock.recv(2)


def encrypt_message(text):
    if mode == 'ECB':
        message = ECBUtil.encrypt(text, K)
    else:
        message = OFBUtil.encrypt(text, Node.iv, K)
    return message


def send_message(s, enc_text):
    s.send(enc_text)


def text_send(s):
    wait_signal(s)
    f = open("text.txt", "rb")
    text = f.read()
    enc_text = encrypt_message(text)
    s.send(len(enc_text).to_bytes(4, 'big'))
    send_message(s, enc_text)


def send_key(s):
    s.send(enc_k)


if __name__ == "__main__":
    s = connect_km(Node.PORT_1)
    s1 = connect_b(Node.PORT_2)
    send_mode(s1)
    get_key(s)
    s.close()
    send_key(s1)
    text_send(s1)
    s1.close()
