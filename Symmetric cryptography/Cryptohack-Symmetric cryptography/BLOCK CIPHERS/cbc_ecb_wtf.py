import requests
import os
from Cryptodome.Util.number import bytes_to_long
url="https://aes.cryptohack.org/ecbcbcwtf/"
def fetch_encrypt():
    r=requests.get(f"{url}/encrypt_flag/")
    data=r.json()
    ciphertext=data["ciphertext"]
    return ciphertext

def fetch_decrypted(ciphertext):
    r=requests.get(f"{url}/decrypt/{ciphertext}")
    data=r.json()
    plaintext=data["plaintext"]
    return plaintext

ciphertext=int(str(bytes_to_long(fetch_encrypt().encode())),16)
iv=str(ciphertext)[:32]#hex
flag=str(ciphertext)[32:]#hex
#print(len(flag))


f1=str(flag)[32:64]
p1=fetch_decrypted(f1)
f2=str(flag)[64:96]
p2=fetch_decrypted(f2)

iv=bytes.fromhex(iv)
f1=bytes.fromhex(f1)
f2=bytes.fromhex(f2)
p1=bytes.fromhex(p1)
p2=bytes.fromhex(p2)

#plaintext=fetch_decrypted(flag)
#print(len(iv))
flag1=''
flag2=''
for i in range(16):
    flag1=flag1+hex(iv[i]^f1[i])[2:]
for j in range(16):
    flag2=flag2+hex(p2[j]^f2[j])[2:]

print(bytes.fromhex(flag1))
print(bytes.fromhex(flag2))

#print(len(ciphertext))
#ciphertext = bytes.fromhex(ciphertext)

