from pwn import remote
import string

# Connect to the server
HOST = 'mercury.picoctf.net'
PORT = 6276
conn = remote(HOST, PORT)

conn.recvuntil(b'flag: ')
encrypted_flag = conn.recvline().decode().strip()
print(f'Encrypted flag: {encrypted_flag}')

# Ignore N and e (not required)
conn.recvline()
conn.recvline()

# Decrypt the flag
decrypted_flag = ''
removecipher = []

while "}" not in decrypted_flag:
    for c in string.ascii_lowercase + string.digits + "{}_CTF":
        curr = decrypted_flag + c
        conn.sendlineafter(": ", curr)
        conn.recvuntil(b': ')
        curr_cipher = conn.recvline().decode().strip()
        for cipher in removecipher:
            curr_cipher = curr_cipher.replace(cipher, "")
        if curr_cipher in encrypted_flag:
            print(decrypted_flag + c)
            decrypted_flag += c
            removecipher.append(curr_cipher)
            break
print(f'Decrypted flag: {decrypted_flag}')

conn.close()