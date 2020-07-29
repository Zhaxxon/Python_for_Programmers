import hashlib
import binascii
dk = hashlib.pbkdf2_hmac(hash_name='sha256',
        password=b'bad_password34',
        salt=b'bad_salt',
        iterations=100000)
print (binascii.hexlify(dk))
#b'6e97bad21f6200f9087036a71e7ca9fa01a59e1d697f7e0284cd7f9b897d7c02'