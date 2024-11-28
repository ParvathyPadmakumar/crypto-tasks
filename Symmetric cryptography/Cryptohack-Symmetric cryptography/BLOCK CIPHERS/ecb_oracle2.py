import requests
import string
url = "http://aes.cryptohack.org/ecb_oracle/"
s0 = 'a'*16
s1 = 'a'*16
k = string.printable
flag = ''
t = ''
for i in range (31):
    s1 =s1[1:]+t
    for  j in k:
        c = s0+s1+j+'a'*(31-i)
        c = c.encode().hex()
        r = requests.get(f"{url}/encrypt/{c}")
        data = r.json()
        cipher = data["ciphertext"]
        cipher = bytes.fromhex(cipher)
        if(cipher[16:32]==cipher[48:64]):
            flag +=j
            t=j
            print(flag)
            break