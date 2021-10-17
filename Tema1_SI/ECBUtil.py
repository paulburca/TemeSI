from Crypto.Util.Padding import pad, unpad

import AESUtil
import Node


def encrypt(text, K):
    enc = b''
    while text:
        block = text[0:16]
        text = text[16:]
        block = AESUtil.encrypt_AES(pad(block, 16), K)
        enc += bytes(block)
    return enc


def decrypt(text, K):
    dec = b''
    while text:
        block = text[0:16]
        text = text[16:]
        block = AESUtil.decrypt_AES(block, K)
        block = unpad(block, 16)
        dec += bytes(block)
    return dec
