# Export-grade
## Description
Alice and Bob are using legacy codebases and need to negotiate parameters they both support. You've man-in-the-middled this negotiation step, and can passively observe thereafter. How are you going to ruin their day this time?

`Connect at socket.cryptohack.org 13379`
## Solution
- Connected to the server and analysed what's going on:
  - First, the server sends the text `Intercepted from Alice: {'supported': ['DH1536', 'DH1024', 'DH512', 'DH256', 'DH128', 'DH64']}`
  - This is the list of supported parameters by Alice
  - If we modify this list to just have `DH64`, then Bob will be forced to choose this parameter. DH64 is the weakest parameter and can be easily broken by brute force
  - So, we modify the list to `{'supported': ['DH64']}` and send it to Bob
  - The server then sends the text `Intercepted from Bob: {'chosen': 'DH64'}`
  - We send `{'chosen': 'DH64'}` to Alice
  - The server then gives us the `g`, `p`, `A`, `B`, `iv`, and the `encrypted_flag` values which we can use to decrypt the flag
- I wrote the following script [Export-grade.py](./Export-grade.py) to get the flag
```python
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
```
- Running the script gives the flag
```
[+] Opening connection to socket.cryptohack.org on port 13379: Done
/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pwnlib/tubes/tube.py:1489: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  return func(self, *a, **kw)
Intercepted from Alice: {'supported': ['DH1536', 'DH1024', 'DH512', 'DH256', 'DH128', 'DH64']}
Send to Bob: {'supported': ['DH64']}
/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pwnlib/tubes/tube.py:841: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  res = self.recvuntil(delim, timeout=timeout)
Intercepted from Bob: {'chosen': 'DH64'}
Send to Alice: {'chosen': 'DH64'}
Intercepted from Alice: {'p': '0xde26ab651b92a129', 'g': '0x2', 'A': '0x3ba23c95d80836cb'}
Intercepted from Bob: {'B': '0xc6ef683b8830f7f4'}
Intercepted from Alice: {'iv': 'b4349f73f566793f175fe4350e722d39', 'encrypted_flag': 'b3b205dfa5b30ee0613c6f6a0e0091b0b97a988606e14f6b3fb485edec5a841d'}
Flag: crypto{d0wn6r4d35_4r3_d4n63r0u5}
[*] Closed connection to socket.cryptohack.org port 13379
```