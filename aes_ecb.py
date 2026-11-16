
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b'1234567890abcdef'
plaintext = b'AAAAAAAABBBBBBBBAAAAAAAABBBBBBBB'

cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(plaintext, 16))

print("Ciphertext hex:", ciphertext.hex())

print("\n=== Blok ciphertext ===")
blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]

for i, block in enumerate(blocks, 1):
    print(f"Block {i}: {block.hex()}")

print("\nApakah blok 1 == blok 2?", blocks[0] == blocks[1])
