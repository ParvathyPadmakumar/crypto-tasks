from Cryptodome.Util.number import *
import primefac 
N= 984994081290620368062168960884976209711107645166770780785733
e = 65537
ct = 948553474947320504624302879933619818331484350431616834086273

p=1160939713152385063689030212503
q=848445505077945374527983649411
phi=(p-1)*(q-1)
d=pow(e,-1,phi)
m=pow(ct,d,N)
decr=long_to_bytes(m)
print(decr)