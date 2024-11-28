from Cryptodome.Cipher import AES
from base64 import *
key=b"YELLOW SUBMARINE"
with open(r"C:\Users\puppy\Downloads\ecb.txt","r") as f:
    fh=f.readlines()

cipher=AES.new(key,AES.MODE_ECB)

def decrypt(ciphertext):
    print((ciphertext))
    plaintext=cipher.decrypt(ciphertext)
    return plaintext

s=""
for line in fh:
    line=line.rstrip()
    s+=line
s=b64decode(s)
print(s)
#16 chars
for i in range(16,3840,16):
    block=(s[:i])
    print(block)
    print(decrypt(block))

