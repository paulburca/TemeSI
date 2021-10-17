from Crypto.Cipher import AES


def decrypt_AES(text, key):
    aes = AES.new(key, AES.MODE_ECB)
    enc_text = aes.encrypt(text)
    return enc_text


def encrypt_AES(text, key):
    aes = AES.new(key, AES.MODE_ECB)
    dec_text = aes.decrypt(text)
    return dec_text
