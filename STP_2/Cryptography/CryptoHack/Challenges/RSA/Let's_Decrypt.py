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