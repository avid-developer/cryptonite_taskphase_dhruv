# Let's Decrypt
## Description
If you can prove you own CryptoHack.org, then you get access to one of our secrets.

Connect at `socket.cryptohack.org 13391`

Challenge files:
  - [13391.py](./13391_5bb4e548ed254cef357799685c887460.py)
## Solution
- installed the `pwntools` and `pkcs1` libraries using `pip` command to solve the challenge.
- I first analyzed the provided python script [13391.py](./13391_5bb4e548ed254cef357799685c887460.py)
- The script sets up a server validates domain ownership using RSA signatueres.
- The code has a placeholder `FLAG` and the `MSG`: `We are hyperreality and Jack and we own CryptoHack.org`
- It then encodes this message using PKCS#1 v1.5 padding to a 256 byte `DIGEST`.
- It then signs the digest using the private key and stores it in `SIGNATURE`.
- Sending the JSON request: 
```json
{"option": "get_signature"}
``` 
to the server will return the public key (`N`, `e`) and the signature in hex format.
- Sending the JSON request:
```json
{
    "option": "verify",
    "msg": msg,
    "N": hex(n),
    "e": hex(e)
}
```
where `msg` is the message to be signed, `n` is the modulus and `e` is the public exponent does the following:
  - It stores `msg`, `n` and `e` as:
  ```python
  msg = your_input['msg']
  n = int(your_input['N'], 16)
  e = int(your_input['e'], 16)
  ```
  - it then encodes the message using PKCS#1 v1.5 padding to a 256 byte `digest`.
  - it then performs modular exponentiation on the `SIGNATURE` using the public key and stores the result in `calculated_digest`.
  - If the `calculated_digest` is equal to the integer representation of `digest`:
    - it checks if the `msg` matches the regular expression `^I am Mallory.*own CryptoHack.org$`. If it does, it returns the flag.
- I then wrote the following [Let's_Decrypt.py](./Let's_Decrypt.py) script to solve the challenge:
```py
from pwn import remote
import json
from Crypto.Util.number import bytes_to_long
from pkcs1 import emsa_pkcs1_v15

HOST = 'socket.cryptohack.org'
PORT = 13391
conn = remote(HOST, PORT)
print(conn.recvline().decode())

def send_and_receive(data):
    conn.sendline(json.dumps(data).encode())
    response = conn.recvline()
    return json.loads(response.decode())

data = {"option": "get_signature"}
response = send_and_receive(data)

SIGNATURE = int(response['signature'], 16)
SERVER_N = int(response['N'], 16)
SERVER_E = int(response['e'], 16)

print(f"Received SIGNATURE: {hex(SIGNATURE)}")
print(f"Received N: {hex(SERVER_N)}")
print(f"Received e: {hex(SERVER_E)}")

msg = "I am Mallory and I own CryptoHack.org"

digest = emsa_pkcs1_v15.encode(msg.encode(), 256)
digest_long = bytes_to_long(digest)

e = 1
n = SIGNATURE - digest_long

if n <= 0:
    raise ValueError("Computed n is not positive.")

print(f"Computed n: {hex(n)}")
print(f"Using e: {hex(e)}")

data = {
    "option": "verify",
    "msg": msg,
    "N": hex(n),
    "e": hex(e)
}

response = send_and_receive(data)

if 'msg' in response:
    print(response['msg'])
else:
    print(f"Error: {response.get('error', 'Unknown error')}")

conn.close()
```
- The script first connects to the server and prints the welcome message: `This server validates domain ownership with RSA signatures. Present your message and public key, and if the signature matches ours, you must own the domain.\n`
- It then sends the JSON request `{"option": "get_signature"}` to the server and receives the public key and signature and prints them in integer format.
- It then sets the `msg` to `I am Mallory and I own CryptoHack.org` as it matches the regular expression in the server code.
- It then encodes the message using PKCS#1 v1.5 padding to a 256 byte `digest` and converts it to a long integer `digest_long`.
- This is how the attack works:
  - Since we control `e` and `n`, and we have access to `SIGNATURE`, we can manipulate these values to satisfy the condition `bytes_to_long(digest) == calculated_digest`.
  - `calculated_digest` is computed as:
  ```py
  calculated_digest = pow(SIGNATURE, e, n)
  ``` 
  - We set `e` = 1 to simplify the equation to: 
  ```py
  calculated_digest = pow(SIGNATURE, 1, n) = SIGNATURE % n
  ```
  - `n` is then computed as:
  ```py
    n = SIGNATURE - bytes_to_long(digest) = SIGNATURE - digest_long
  ```
  - this ensures that:
  ```py
  SIGNATURE % n = SIGNATURE - (SIGNATURE - bytes_to_long(digest)) = bytes_to_long(digest)
  ```
  - To ensure that `n` is positive, we check if `n <= 0` and raise an error if it is.
- we then print the computed `n` and `e` (which is 1) in hex format and send the JSON request:
```json
{
    "option": "verify",
    "msg": msg,
    "N": hex(n),
    "e": hex(e)
}
```
- We then receive the response from the server and print the `msg` which contains the flag.
- Running the script gives the flag: `crypto{dupl1c4t3_s1gn4tur3_k3y_s3l3ct10n}`
```
[+] Opening connection to socket.cryptohack.org on port 13391: Done
This server validates domain ownership with RSA signatures. Present your message and public key, and if the signature matches ours, you must own the domain.

Received SIGNATURE: 0x55c231eebc642cd1e44199e10937ee8b9e93c0c2d10a18b7b53a207fb1ddd4e6c2e08368a1943187bb1efe0378567340a0851710c426f609aa79d3b5bb3f8efe7f531cfdb54a9fba9e77e3ca2adcecdc299ebf601bd8926dd6ed4e7e71f96ef61cc041159eb0584ff4ce9f0d9e5cb49a91ba15226740f378340e40805aff2e20e275b783aa43a0ac670ec1af2d4e834acceda189add6ed7daf64ed8f9f9718f030c8a7d64afee7cf33beef5f790611eaef40e7c978e2355f3039a6df4f38113ce83ed669a733ce6a93e1fb04fdd6c28815beb6b62f886a47150fbdd34668aa7ff55787874a7b6787a5942da4d73b3197eb792b39d0e338f48fc5f4c01a16a178
Received N: 0x80a5b8245992f64d2d11f1279a88d23dd76594fa0a37427e55482c819fe6eb727f7cde0a715c018f8e3c98cc721ff1f779e8c704f3ad2ce877eaecf680c7105685581ac1dc8d5040d602a47d8dba333e787599a7528154f8f72581f1119c1c1267078e8bfb4e2a67b00ad13827660381b8105590a72b7d1fa45bdd2c07cc12ab2d8f7c6578178e93aac1a29ccdd1ecbeeafa25fa425988376384f745a7613af437ad235826d7d1499a0b2e83401ce0781fb85aa801ae9c43a9f79b2bd4bc8817a2a0725272e847e3b397e1d27b86fa0ba038b2704534a98a12e5e133f2358521ee0ee59a892928543c4a71460cadc2c89e011b019c2094ca6d17a0c143dc9297
Received e: 0x10001
Computed n: 0x55c031eebc642cd1e44199e10937ee8b9e93c0c2d10a18b7b53a207fb1ddd4e6c2e08368a1943187bb1efe0378567340a0851710c426f609aa79d3b5bb3f8efe7f531cfdb54a9fba9e77e3ca2adcecdc299ebf601bd8926dd6ed4e7e71f96ef61cc041159eb0584ff4ce9f0d9e5cb49a91ba15226740f378340e40805aff2e20e275b783aa43a0ac670ec1af2d4e834acceda189add6ed7daf64ed8f9f9718f030c8a7d64afee7cf33beef5f790611eaef40e7c978e2355f3039a6df4f38113ce83ed669a733ce6a93e1fb04fdd6c28815beb6b62f886a47150fbdd44638894fec51825c3c78656da0942990ce22a474772c6b25f1b0509048b448b31ac26e69
Using e: 0x1
Congratulations, here's a secret: crypto{dupl1c4t3_s1gn4tur3_k3y_s3l3ct10n}
[*] Closed connection to socket.cryptohack.org port 13391
```