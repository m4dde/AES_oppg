from Crypto.Cipher import AES 
from Crypto.Random import get_random_bytes 

my_key = get_random_bytes(16)
iv = get_random_bytes(16)

def pad(s):
    padding = 16 - len(s) % 16
    return s + padding * chr(padding)

melding = "hemmelig melding"
melding = pad(melding).encode
cipher = AES.new(my_key, AES.MODE_CBC, iv)
kryptogram = cipher.encrypt(melding)
print("Kryptert melding:", kryptogram)

def unpad(s):
    padding_verdi = s[-1]
    return s[:-padding_verdi]

def test_unpad():
    original_melding = "hemmelig melding"
    padded_melding = pad(original_melding).encode()
    unpadded_melding = unpad(padded_melding)
    return original_melding == unpadded_melding.decode()

cipher = AES.new(my_key, AES.MODE_CBC, iv)
dekryptert = cipher.decrypt(kryptogram)
dekryptert = unpad(dekryptert).decode()
print("Dekryptert melding:", dekryptert)



