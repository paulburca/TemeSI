from Crypto.Util.Padding import pad, unpad
import AESUtil


def xor(first, second):
    return  bytes(a ^ b for (a, b) in zip(first, second))


def encrypt(text, iv, K):
    enc = b''
    while text:
        iv = AESUtil.encrypt_AES(iv, K)
        block = text[0:16]
        text = text[16:]
        block = xor(iv, block)
        enc += bytes(block)
    return enc


def decrypt(text, iv, K):
    dec = b''
    while text:
        iv = AESUtil.encrypt_AES(iv, K)
        block = text[0:16]
        text = text[16:]
        block = xor(iv, block)
        dec += bytes(block)
    return dec
