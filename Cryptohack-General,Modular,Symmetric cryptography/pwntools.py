from pwn import * 
import json
from base64 import b64decode
from Cryptodome.Util.number import long_to_bytes
r = remote('socket.cryptohack.org', 13377)
context.log_level = 'debug'
def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)
counter=0
def rot13(word):
    ans=''
    for letter in word.lower():
        if(letter.isalnum()==True):
            ans=ans+chr((ord(letter) - 97 + 13) % 26 + 97)
        elif(letter=="_"):
            ans=ans+"_"
    return ans
    
received = json_recv()
type=received["type"]
encoded=received["encoded"]

while(counter<=100):
    if(type=="base64"):
        ans=b64decode(encoded).decode()
        
    elif(type=="rot13"):
        ans=rot13(encoded)
    elif(type=="hex"):
        ans=bytes.fromhex(encoded).decode()
    elif(type=="bigint"):
        a=int(encoded,16)
        key=long_to_bytes(a)
        ans=key.decode()
    else:
        l=encoded
        ans=""
        for i in encoded:
            ans+=chr(i)
    
     
    ans=str(ans)
    to_send = {
    "decoded":ans
    }
    json_send(to_send)

    received=json_recv()
    print(received)
    type=received["type"]
    encoded=received["encoded"]
    counter+=1



