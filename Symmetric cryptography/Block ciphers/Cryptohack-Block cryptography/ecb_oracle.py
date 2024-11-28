from Cryptodome.Util.Padding import pad, unpad
from binascii import unhexlify
from Cryptodome.Cipher import AES
import requests
from binascii import hexlify

def response(plaintext):
    url = "http://aes.cryptohack.org/ecb_oracle/encrypt/"
    url += plaintext
    url += '/'
    r = requests.get(url)
    js = r.json()
    block1=js["ciphertext"][:16]
    return js["ciphertext"]
   
block1="009823eda7cefeb137c172644f72f55e"
for i in range(30,128):
    original_i=i
    i=hex(i)[2:]
    plaintext="63"+"72"+"79"+"70"+"74"+"6f"+"7b"+"70"+"33"+"6e"+"36"+"75"+"31"+"6e"+"35"+"63"
    #print(plaintext)
    resp=response(plaintext)
    #print(resp)
    if(block1 in resp):
        print(i)
#b'crypto{p3n6u1n5'













