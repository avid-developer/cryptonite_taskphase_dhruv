# Parameter Injection
## Description
You're in a position to not only intercept Alice and Bob's DH key exchange, but also rewrite their messages. Think about how you can play with the DH equation that they calculate, and therefore sidestep the need to crack any discrete logarithm problem.

Use the [script](./decrypt_08c0fede9185868aba4a6ae21aca0148.py) from "Deriving Symmetric Keys" to decrypt the flag once you've recovered the shared secret.

Connect at `socket.cryptohack.org 13371`
## Solution
- Connected to the server and analysed what's going on:
  - First, the server sends the text `Intercepted from Alice: ` and then `p`, `g`, and `A` values in JSON format.
  - Then, the server prompts us with the text `Send to Bob: ` where we can send the `p`, `g`, and `A` values in JSON format. We can modify these values before sending them to the server.
  - Similarly, the server sends the text `Intercepted from Bob: ` and then `B` value in JSON format.
  - Then, the server prompts us with the text `Send to Alice: ` where we can send the `B` value in JSON format. We can also modify this value before sending it to the server.
  - Finally, the server sends the text `Intercepted from Alice: ` and then `iv` (initialization vector) and `encrypted_flag` values in JSON format.
- The server is using the `AES` encryption algorithm in `CBC` mode to encrypt the flag.
- The server is using the `Diffie-Hellman` key exchange algorithm to establish a shared secret key between Alice and Bob.
- The server is using the `p` and `g` values as the public parameters for the `Diffie-Hellman` key exchange algorithm.
- The server is using the `A` and `B` values as the public keys for Alice and Bob respectively and using these values to calculate the shared secret key.
- The server is using the `iv` value as the initialization vector for the `AES` encryption algorithm.
- I wrote the following [Parameter_Injection.py](./Parameter_Injection.py) script to find the flag:
```python
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
```
- The script does the following:
  - Modifies the `g` value to `1` in the message intercepted from Alice and sends it to Bob.
    - Doing so will result in `B` being `1` as well as `B = g^b mod p = 1^b mod p = 1` where `b` is the private key of Bob.
  - When `B` is sent to Alice, the shared secret key is calculated as `s = B^a mod p = 1^a mod p = 1` where `a` is the private key of Alice.
  - The shared secret key `1` is used to derive the `AES` key.
  - It uses code from the helper script [decrypt.py](./decrypt_08c0fede9185868aba4a6ae21aca0148.py) to decrypt the flag.
- Executed the script to get the flag:
```bash
[+] Opening connection to socket.cryptohack.org on port 13371: Done
/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pwnlib/tubes/tube.py:1489: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  return func(self, *a, **kw)
Intercepted from Alice: {'p': '0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff', 'g': '0x02', 'A': '0xbe17505c97066acc9affa2c24d3ba17818551d084cab3ae9d395763b459a8d14c6c5aa4aac8ed8f3cb96f46b0a939d8007de8b2b23582343e646ed4d71708b35c6522ebcb61421673ee14a4a7200686862a3d744092e238903fb9f01a34116749ae4ef44d64ddfe6a22872d7b5ae2b87c37f846e341db597fc467aa6a19fd3ebb290f079a9d7c78b0dd25302f65eb0d11af91b23814ab23b7e64f60da5dd57d9eb57f82a1562b35637969233c69eba6198b71cf28209732e85a1e81ba0ae2edd'}
Send to Bob: {'p': '0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff', 'g': '0x01', 'A': '0xbe17505c97066acc9affa2c24d3ba17818551d084cab3ae9d395763b459a8d14c6c5aa4aac8ed8f3cb96f46b0a939d8007de8b2b23582343e646ed4d71708b35c6522ebcb61421673ee14a4a7200686862a3d744092e238903fb9f01a34116749ae4ef44d64ddfe6a22872d7b5ae2b87c37f846e341db597fc467aa6a19fd3ebb290f079a9d7c78b0dd25302f65eb0d11af91b23814ab23b7e64f60da5dd57d9eb57f82a1562b35637969233c69eba6198b71cf28209732e85a1e81ba0ae2edd'}
/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pwnlib/tubes/tube.py:841: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  res = self.recvuntil(delim, timeout=timeout)
Intercepted from Bob: {'B': '0x1'}
Send to Alice: {'B': '0x1'}
Intercepted from Alice: {'iv': 'fbe8d06b67d60fc2285dab1d2ee34981', 'encrypted_flag': '1e407b747250ebabe00820c45a27c751cfbf405666218e4d1f9c96a8582faa4b'}
Flag: crypto{n1c3_0n3_m4ll0ry!!!!!!!!}
[*] Closed connection to socket.cryptohack.org port 13371
```