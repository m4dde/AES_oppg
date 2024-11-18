from Crypto.Cipher import AES 

def unpad(s):
    padding_verdi = s[-1]
    return s[:-padding_verdi]

with open("key.bin", "rb") as f:
    key = f.read()

with open("encrypted_data_bin", "rb") as f:
    data = f.read()
    iv = data[:16]
    kryptogram = data[16:]



