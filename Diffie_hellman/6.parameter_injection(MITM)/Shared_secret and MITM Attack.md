A=pow(g,a,p)
s=pow(A,b,p)

## MITM ATTACK

choose an a and b of your choice
g-given
Ya=pow(g,a,p)
Yb=pow(g,b,p)

given A
sA=pow(A,b,p)
sent sA

sB=pow(B,a,p)
sent sB

decrypt flag(sA,ct,iv): 
- get the key from the shared secret
- decrypt ciphertext with CBC_MODE