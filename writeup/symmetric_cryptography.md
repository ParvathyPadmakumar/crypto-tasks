QUESTIONS RELATED TO AES

encryption of AES
key expansion-creates roundkeys
initial round-plaintext is mixed with the initial roundkey
rounds-
	subbytes-each byte in the text now is replaced with a corresponding byte from a pre-defined s-box
	shiftrows-by 1,2 and then 3 etc
	mixcolumns 
	add round key
ciphertext obtained

decryption of AES
key expansion
ciphertext to matrix
initial addroundkey
inverse subbytes
inverse shiftrows
inverse mixcolumns
addroundkey
final round(all these 3 except inv_mix_columns)
matrix2bytes
plaintext obtained
