chars= b"\x0e\x0b!?&\x04\x1eH\x0b&!\x7f'4.\x17]\x0e\x07\n<[\x10>%&!\x7f'4.\x17]\x0e\x07~&4Q\x15\x01\x04"

for xor_key in range(256):
    decod=''.join(chr(b^xor_key)for b in chars) 
    if decod.isprintable():
        print(xor_key,decod)