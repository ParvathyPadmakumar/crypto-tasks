from Cryptodome.PublicKey import RSA
from base64 import b64decode
cert='''-----BEGIN RSA PUBLIC KEY-----
MIIBigKCAYEArTy6m2vhhbwx3RVbNVb3ZOenCqqsOXHaJpbtN+OuulLKBSKpIoPB
+ZDbDXn0qWkf4lOxtGSgolkUbgG07Lhzfgs+dul4UL84CkwZExmF3Rf1nRv+v7pq
Lt2dPsCb02YLxJnhHJb4rQaz2ZM4QCtTOcqYDUeKfLHCaZU4Ekm/OApKrpfw4/0o
fn8KOrFN0t4/dqnNuwVRgoaUIhsI47reApB2rs0AP4CggSIi8s6BXCxB4YzgThBK
5760T1giACYQC5MFdq1Gw+INSFmu0CNqt5wdJ5Z4z5448Gke06R+IMtjUiGDQ3Qt
T2fK3gWhZxk14M4UNrdETgTW/mQ4B/BcvikxvoBGpKbttG0agfOjTen6wyzpGfcd
8N9rSbaqqyUwC8uDotzFtFzzutVAU9d91TagGzWBhNoMfplwVTns27GOOgv1dn5s
QSSSmP0hTbPMDlThysKkR9BiOVbBtWGQpV936pPBgyWERGqMqC9xykLdVHv2Vu05
T0WMwKCAetgtAgMBAAE=
-----END RSA PUBLIC KEY-----'''

a=RSA.importKey(cert)    
print(a.n)

#ssh-keygen -f "rsa.pub" -e -m pem