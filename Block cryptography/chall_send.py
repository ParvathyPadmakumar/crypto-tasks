#CHAINER
import json
from binascii import *
import requests
from pwn import *

plaintext=binascii.hexlify(("a"*16*3).encode())
#print(plaintext)
ans=''

import socket


r=remote("74.225.222.43",5000)
r.recvuntil(b"Your response: ")
r.sendline(b"1")
r.recvuntil(b"plaintext (hex): ")
r.sendline(plaintext)
data = r.recvline().decode().strip("\n")
ciphertext=(eval(data))["ciphertext"]

c0 = ciphertext[:32]
c1 = ciphertext[32:64]
c2 = ciphertext[64:]

newciph = c0+c1+c0

r.recvuntil(b"Your response: ")
r.sendline(b"3")
r.recvuntil(b"ciphertext (hex): ")
r.sendline(newciph.encode())

data = r.recvline().decode().strip("\n")
plaintext=(eval(data))["error"]
plaintext=((plaintext.split(":"))[-1]).lstrip()
plaintext = binascii.unhexlify(plaintext)

p0 = plaintext[:16]
p1 = plaintext[16:32]
p2 = plaintext[32:]

c1 = binascii.unhexlify(c1)

#ans=xor(p0,c1,p2)
#ans2=xor(ans,p2)
#ans=ans.hex() 

for i in range(16):
    ans += hex(p0[i] ^ p2[i] ^ c1[i])[2:].zfill(2)

print(ans)

#ans2 is key which is IV
r.recvuntil(b"Your response: ")
r.sendline(b"2")
r.recvuntil(b"Key (hex): ")
r.sendline(ans.encode())

r.recvline()
flag=r.recvline().decode().strip('\n')
print(flag)

flag=flag.split(": '")[-1].rstrip("'}")
print(flag)
print(unhexlify(flag.encode()))

#bi0s{l4zy_ch41n3d_c1ph3r1n6_cl34v3d}
