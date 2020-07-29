from cryptography.fernet import Fernet
cipher_key = Fernet.generate_key()
print (cipher_key)
#b'APM1JDVgT8WDGOWBgQv6EIhvxl4vDYvUnVdg-Vjdt0o='

cipher = Fernet(cipher_key)
text = b'My super secret message'
encrypted_text = cipher.encrypt(text)
print (encrypted_text)
#(b'gAAAAABXOnV86aeUGADA6mTe9xEL92y_m0_TlC9vcqaF6NzHqRKkjEqh4d21PInEP3C9HuiUkS9f'
# b'6bdHsSlRiCNWbSkPuRd_62zfEv3eaZjJvLAm3omnya8=')

decrypted_text = cipher.decrypt(encrypted_text)
print (decrypted_text)
#b'My super secret message'