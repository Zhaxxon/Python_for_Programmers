# Encrypting a String
from Crypto.Cipher import DES
key = b'abcdefgh'
def pad(text):
        while len(text) % 8 != 0:
            text += b' '
        return text
des = DES.new(key, DES.MODE_ECB)
text = b'Python rocks!'
padded_text = pad(text)
encrypted_text = des.encrypt(text)
#Traceback (most recent call last):
#  File "<pyshell#35>", line 1, in <module>
#    encrypted_text = des.encrypt(text)
#  File "C:\Programs\Python\Python35-32\lib\site-packages\Crypto\Cipher\blockalgo.py", line 244, in encrypt
#    return self._cipher.encrypt(plaintext)
#ValueError: Input strings must be a multiple of 8 in length


from Crypto.Cipher import DES
key = b'abcdefgh'
def pad(text):
        while len(text) % 8 != 0:
            text += b' '
        return text
des = DES.new(key, DES.MODE_ECB)
text = b'Python rocks!'
padded_text = pad(text)

encrypted_text = des.encrypt(padded_text)
print (encrypted_text)
#b'>\xfc\x1f\x16x\x87\xb2\x93\x0e\xfcH\x02\xd59VQ'

print (des.decrypt(encrypted_text))
#b'Python rocks!   '


# Creating an RSA key
from Crypto.PublicKey import RSA
code = 'nooneknows'
key = RSA.generate(2048)
encrypted_key = key.exportKey(passphrase=code, pkcs=8,
        protection="scryptAndAES128-CBC")
with open('my_private_rsa_key.bin', 'wb') as f:
        f.write(encrypted_key)
with open('my_rsa_public.pem', 'wb') as f:
        f.write(key.publickey().exportKey())


# Encrypting a File
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

with open('encrypted_data.bin', 'wb') as out_file:
    recipient_key = RSA.import_key(
        open('my_rsa_public.pem').read())
    session_key = get_random_bytes(16)

    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    out_file.write(cipher_rsa.encrypt(session_key))

    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    data = b'blah blah blah Python blah blah'
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)

    out_file.write(cipher_aes.nonce)
    out_file.write(tag)
    out_file.write(ciphertext)


# decrypt our data
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

code = 'nooneknows'

with open('encrypted_data.bin', 'rb') as fobj:
    private_key = RSA.import_key(
        open('my_rsa_key.pem').read(),
        passphrase=code)

    enc_session_key, nonce, tag, ciphertext = [ fobj.read(x)
                                                for x in (private_key.size_in_bytes(),
                                                16, 16, -1) ]

    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)

print(data)