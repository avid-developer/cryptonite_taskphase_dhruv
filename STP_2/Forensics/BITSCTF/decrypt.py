from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

def decrypt_file(file_path, key):
    iv = b'urfuckedmogambro'
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    decrypted_file_path = file_path.replace(".enc", "_decrypted.png")
    with open(decrypted_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

# Convert hexadecimal key to bytes
hex_key = "FBF60E95C2F3C96F36E1195538E34E30CF1A290F1C14CD5E699E476A3BE2BC5E"
key = binascii.unhexlify(hex_key)

decrypt_file("secret.png.enc", key)