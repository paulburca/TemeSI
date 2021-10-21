from Crypto.Util.Padding import pad, unpad
from CryptoUtils import AESUtil


def xor(first, second):
    return bytes(first[index] ^ second[index] for index in range(0, 16))


def encrypt(text, iv, k):
    enc = b''
    text = pad(text, 16)
    while text:
        iv = AESUtil.encrypt(iv, k)
        block = text[0:16]
        text = text[16:]
        block = xor(iv, block)
        enc += bytes(block)
    return enc


def decrypt(text, iv, k):
    dec = b''
    while text:
        iv = AESUtil.encrypt(iv, k)
        block = text[0:16]
        text = text[16:]
        block = xor(iv, block)
        dec += bytes(block)
    dec = unpad(dec, 16)
    return dec
