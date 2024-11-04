from Cryptodome.PublicKey import RSA
from base64 import b64decode
with open(r"C:\Users\puppy\Downloads\privacy_enhanced_mail.pem","r") as f:
   cert = f.read()
   key=b64decode(cert)

a=RSA.importKey(key)
print(a.d)
