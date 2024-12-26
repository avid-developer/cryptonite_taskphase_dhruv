from pwn import remote
from Crypto.Util.number import isPrime, long_to_bytes
from string import ascii_letters, digits
from itertools import combinations
from sympy import divisors

# Connect to the server
HOST = 'saturn.picoctf.net'
PORT = 51224 # The port number here is different as my instance timed out and launching a new instance gave a different port number
conn = remote(HOST, PORT)

conn.recvuntil(b'anger = ')
ciphertext = int(conn.recvline().strip().decode())
print(f'anger = {ciphertext}')

conn.recvuntil(b'envy = ')
d = int(conn.recvline().strip().decode())
print(f'envy = {d}')

e = 65537

print(conn.recvline().decode())

poss = divisors(d*e-1)
primes = [i+1 for i in poss if isPrime(i+1)]
proper_primes = [p for p in primes if p.bit_length() == 128]

poss_plaintexts = []
char = ascii_letters + digits

for p,q in combinations(proper_primes, 2):
    try:
        string = long_to_bytes(pow(ciphertext, d, p*q)).decode("ascii")
        if all(c in char for c in string):
            poss_plaintexts.append(string)
    except:
        continue

print(poss_plaintexts)
if len(poss_plaintexts) == 1:
    M = poss_plaintexts[0]
else:
    print("Multiple possible plaintexts found, try again")
    exit()

conn.sendlineafter("> ", M.encode())

print(conn.recvall().decode())

conn.close()