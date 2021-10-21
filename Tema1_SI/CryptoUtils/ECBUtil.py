from Crypto.Util.Padding import pad, unpad
from CryptoUtils import AESUtil


def encrypt(text, k):
    enc = b''
    text = pad(text, 16)
    # adds padding so that it can be divided in 16 bytes blocks
    while text:
        block = text[0:16]
        text = text[16:]
        block = AESUtil.encrypt(block, k)
        enc += bytes(block)
    return enc


def decrypt(text, k):
    dec = b''
    while text:
        block = text[0:16]
        text = text[16:]
        block = AESUtil.decrypt(block, k)
        dec += bytes(block)
    dec = unpad(dec, 16)
    # deletes the padding
    return dec
