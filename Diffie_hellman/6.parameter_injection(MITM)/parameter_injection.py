
inp= {"p": 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff, "g": 0x02, "A": 0xfcdc3f8c60cb19e3bb6b00541618f7fc822bab2c116084af3c44f31a26e272bbcbe4cb013eafe0204636d172fdc80f163be24f5468caea4dea67b8284d80d26905fb94cf9df6ab927579d353fa047334759ade2572cb12f41e339c045d136d698d83e7426091fd3cce364195421be7a5d4d7e7659aa78d32302f6311a49d72ee2ab6f1e555f754a572a0947e4e01b2f65bb3efdb8ec362dfa0790feeefe8c4525ac5d37398d52139c5b1ce3feb989c0051e8800cf9a04599c51b506070dccc18}
p=inp["p"]
g=inp["g"]
A=inp["A"]

a=10001
b=10101
Ya=pow(g,a,p)
Yb=pow(g,b,p)
sA=pow(A,b,p)

print("Ya=",hex(Ya))

B=0xe32e31c722b1ff47941ca3b811920679bd0372dbaabdb857c2fe1c75fa430b530f57202423a1923d4e60d75a0ea33e93dd4fef0319e6555e3d2fa9cc2f5f7973d1a3f1437d6d79898b4811abbcbde4e32136dca38509260622a063e15eed835ede3ee9ae90173facb780268b4e8ea2de29bb4692f4946e0eeac2c0440d87e3bfb1b467675122cede2673fd91fb97d8f271aaddaef5f8956592842bc90d20c7d0c81570b4ea54d41d7940ddd89c4a40357dc5f9bbdbea0aa738c43a3f6ab130b7

print("Yb=",hex(Yb))
sB=pow(B,a,p)

iv="dcc3d61081b09738d86eb589fae2366e"
ct="9974e448404a684c6d773e2894443716e8c5f98772503e5836c8af69c9fd2b5e"


from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')
    
print(decrypt_flag(sA, iv,ct))
