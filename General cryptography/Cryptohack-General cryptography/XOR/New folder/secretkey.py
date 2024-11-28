chars= b"\x0e\x0b!?&\x04\x1eH\x0b&!\x7f'4.\x17]\x0e\x07\n<[\x10>%&!\x7f'4.\x17]\x0e\x07~&4Q\x15\x01\x04"
plaintext=b"crypto{1"
key=''.join(chr(b^m) for b,m in zip(chars,plaintext))
print(key)

chars= b"\x0e\x0b!?&\x04\x1eH\x0b&!\x7f'4.\x17]\x0e\x07\n<[\x10>%&!\x7f'4.\x17]\x0e\x07~&4Q\x15\x01\x04"
key=b"myXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORk"
plaintext=''.join(chr(b^m)for b,m in zip(chars,key))
print(plaintext)