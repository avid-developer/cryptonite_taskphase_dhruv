from pwn import remote
import json
import hashlib
from Crypto.Cipher import AES
from sympy.ntheory import discrete_log

# Connect to the server
HOST = 'socket.cryptohack.org'
PORT = 13379
conn = remote(HOST, PORT)

# Function to receive JSON data
def recv_json():
    line = conn.recvline()
    return json.loads(line.decode())

# Function to send JSON data after waiting for the prompt
def send_json(data):
    request = json.dumps(data).encode()
    conn.sendlineafter(": ", request)

# Intercept message from Alice
conn.readuntil(": ")  # Read until the prompt ": "
alice = recv_json()
print("Intercepted from Alice:", alice)

alice['supported'] = ["DH64"]
# Forward modified message to Bob
print("Send to Bob:", alice)
send_json(alice)

# Intercept message from Bob
conn.readuntil(": ")  # Read until the prompt ": "
bob = recv_json()
print("Intercepted from Bob:", bob)

# Send to Alice
print("Send to Alice:", bob)
send_json(bob)

# Receive p, g, A, B, iv and encrypted_flag
conn.readuntil(": ")  # Read until the prompt ": "
alice = recv_json()
print("Intercepted from Alice:", alice)
p=int(alice['p'], 16)
g=int(alice['g'], 16)
A=int(alice['A'], 16)

conn.readuntil(": ")  # Read until the prompt ": "
bob = recv_json()
print("Intercepted from Bob:", bob)
B=int(bob['B'], 16)

conn.readuntil(": ")  # Read until the prompt ": "
encrypted = recv_json()
print("Intercepted from Alice:", encrypted)

# Computing private key a using sympy's discrete_log function
a = discrete_log(p, A, g)

# Compute shared secret
shared_secret = pow(B, a, p)

# Derive AES key from shared secret
sha1 = hashlib.sha1()
sha1.update(str(shared_secret).encode('ascii'))
key = sha1.digest()[:16]

# Decrypt the flag
iv = bytes.fromhex(encrypted['iv'])
ciphertext = bytes.fromhex(encrypted['encrypted_flag'])
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)
flag = plaintext.decode('utf-8')

print("Flag:", flag)

# Close the connection
conn.close()