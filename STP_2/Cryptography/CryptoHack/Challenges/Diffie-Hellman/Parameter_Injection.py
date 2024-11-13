from pwn import remote
import json
import hashlib
from Crypto.Cipher import AES

# Connect to the server
HOST = 'socket.cryptohack.org'
PORT = 13371
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

# Modify g to 1
alice['g'] = '0x01'
# Forward modified message to Bob
print("Send to Bob:", alice)
send_json(alice)

conn.readuntil(": ")  # Read until the prompt ": "
bob = recv_json()
print("Intercepted from Bob:", bob)

# No need to modify Bob's public key B as it's 1 due to g=1
# Forward Bob's message to Alice
print("Send to Alice:", bob)
send_json(bob)

# Receive encrypted flag from Alice
conn.readuntil(": ")  # Read until the prompt ": "
encrypted = recv_json()
print("Intercepted from Alice:", encrypted)

# Now compute the shared secret
shared_secret = 1  # Since g=1, shared_secret is 1

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