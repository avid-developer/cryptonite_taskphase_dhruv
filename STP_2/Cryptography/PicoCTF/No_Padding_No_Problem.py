from pwn import remote
from Crypto.Util.number import long_to_bytes

# Connect to the server
HOST = 'mercury.picoctf.net'
PORT = 2671 
conn = remote(HOST, PORT)

print(conn.recvuntil('n: ').decode())
n = int(conn.recvline().decode().strip())
print(n)

print(conn.recvuntil('ciphertext: ').decode())
ciphertext = int(conn.recvline().decode().strip())
print(ciphertext)

print(conn.recvuntil(': ').decode())
conn.sendline(str(n+ciphertext).encode())

print(conn.recvuntil(': ').decode())
flag = conn.recvline().decode().strip()
print(long_to_bytes(int(flag)).decode())

conn.close()