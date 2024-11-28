import requests
import binascii
url="https://aes.cryptohack.org/lazy_cbc/"
plaintext=binascii.hexlify(("a"*16*3).encode())
def encrypt(plaintext):
    r=requests.get(f"{url}/encrypt/{plaintext}/")
    data=r.json()
    ciphertext=data["ciphertext"]
    return ciphertext

def decrypt(ciphertext):
    r=requests.get(f"{url}/receive/{ciphertext}/")
    data=r.json()
    plaintext=data["error"]
    return plaintext

c=encrypt(plaintext)
print(c)
p=decrypt(c)
print(p)
