import socket
import Node
import AESUtil
import ECBUtil
import OFBUtil

K = b''
mode = ''


def get_mode(conn):
    return conn.recv(3).decode()


def get_key(conn):
    global K
    enc_k = conn.recv(16)
    K = AESUtil.decrypt_AES(enc_k, Node.K1)


def send_signal(conn):
    conn.send(bytes("GO", 'utf-8'))


def get_text(conn):
    size = conn.recv(4)
    text = conn.recv(int.from_bytes(size, "little"))
    return text


def decrypt_text(text):
    if mode == 'ECB':
        return ECBUtil.decrypt(text, K)
    else:
        return OFBUtil.decrypt(text, Node.iv, K)


def get_data(conn):
    global mode
    mode = get_mode(conn)
    get_key(conn)
    send_signal(conn)
    text = get_text(conn)
    dec_text = decrypt_text(text)
    return dec_text


def accept_conn():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((Node.IP, Node.PORT_2))
    s.listen()
    conn, _ = s.accept()
    message = get_data(conn)
    print(message.decode())
    conn.close()
    s.close()


accept_conn()
