
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

key = b'1234567890abcdef'
plaintext = b'AAAAAAAABBBBBBBBAAAAAAAABBBBBBBB'

# AES ECB
ecb_cipher = AES.new(key, AES.MODE_ECB)
ecb_ct = ecb_cipher.encrypt(pad(plaintext, 16))

# AES CBC
iv = get_random_bytes(16)
cbc_cipher = AES.new(key, AES.MODE_CBC, iv)
cbc_ct = cbc_cipher.encrypt(pad(plaintext, 16))

print("=== AES ECB ===")
print("ECB ciphertext:", ecb_ct.hex())

print("\n=== AES CBC ===")
print("IV:", iv.hex())
print("CBC ciphertext:", cbc_ct.hex())
