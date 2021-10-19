from Crypto.Util.Padding import pad, unpad

import AESUtil


def encrypt(text, K):
    enc = b''
    text = pad(text, 16)
    while text:
        block = text[0:16]
        text = text[16:]
        block = AESUtil.encrypt_AES(block, K)
        enc += bytes(block)
    return enc


def decrypt(text, K):
    dec = b''
    while text:
        block = text[0:16]
        text = text[16:]
        block = AESUtil.decrypt_AES(block, K)
        print(block)
        dec += bytes(block)
    dec = unpad(dec, 16)
    return dec
