message hashed by sha256
```

import hashlib
hashed=sha256(message)
```

This gives a hash object
To convert hash object to byte value:
```
byte=hashed.digest()
```
To convert to long:
```
print(bytes_to_long(byte))
```

