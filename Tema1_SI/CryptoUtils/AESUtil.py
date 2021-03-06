from Crypto.Cipher import AES


def encrypt(text, key):
    aes = AES.new(key, AES.MODE_ECB)
    enc_text = aes.encrypt(text)
    return enc_text


def decrypt(text, key):
    aes = AES.new(key, AES.MODE_ECB)
    dec_text = aes.decrypt(text)
    return dec_text
