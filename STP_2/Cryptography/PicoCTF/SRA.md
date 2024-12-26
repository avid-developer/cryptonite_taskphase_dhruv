# SRA
## Description
I just recently learnt about the SRA public key cryptosystem... or wait, was it supposed to be RSA? Hmmm, I should probably check...
Connect to the program on our server: `nc saturn.picoctf.net 57975`
Download the program: [chal.py](./chal.py)
## Solution
- I initially thought that this challenge is about SRA (Commutative Encryption) but it turns out it has nothing to do with that.
- First connecting to the server, we are given the following:
```
anger = 33921712056553687750864664285547064781983516991485685932150238650655655133733
envy = 38013059312112522090313809492031549947482226013130434236491751509128064275649
vainglory?
> 
```
- Entering a random string, we get the following:
```
anger = 33921712056553687750864664285547064781983516991485685932150238650655655133733
envy = 38013059312112522090313809492031549947482226013130434236491751509128064275649
vainglory?
> l
l
Hubris!
```
- Doing it one more time:
```
anger = 20429677290132627595111758541365181966702148952150330429254597949474593951930
envy = 29655203355559938214594751329453783246092421689444792556649310550094484889601
vainglory?
> 1
1
Hubris!
```
- So entering any random string gives us `Hubris!`. Perhaps when we enter the "correct" string, we will get the flag.
- Let's take a look at [chal.py](./chal.py):
```python
from Crypto.Util.number import getPrime, inverse, bytes_to_long
from string import ascii_letters, digits
from random import choice

pride = "".join(choice(ascii_letters + digits) for _ in range(16))
gluttony = getPrime(128)
greed = getPrime(128)
lust = gluttony * greed
sloth = 65537
envy = inverse(sloth, (gluttony - 1) * (greed - 1))

anger = pow(bytes_to_long(pride.encode()), sloth, lust)

print(f"{anger = }")
print(f"{envy = }")

print("vainglory?")
vainglory = input("> ").strip()

if vainglory == pride:
    print("Conquered!")
    with open("/challenge/flag.txt") as f:
        print(f.read())
else:
    print("Hubris!")
```
- This is an RSA encryption code, but the variables are obfuscated with the seven sins.
- Deobfuscating these variables:
  - `pride` is the plaintext or the Message `M` containing only ascii letters and digits
  - `gluttony` is the first prime number `p` of length 128 bits
  - `greed` is the second prime number `q` of length 128 bits
  - `lust` is the modulus `n`
  - `sloth` is the public exponent `e` = 65537
  - `envy` is the private exponent `d`
  - `anger` is the ciphertext `C`
- `p` and `q` being 128 bits is a bit odd, as it is too small and hence insecure for typical RSA.
- We are given the values of `anger` and `envy` (which are the ciphertext and the private exponent respectively) and we need to find the plaintext `pride` to get the flag.
- The formula for RSA decryption is `M = C^d mod n`
- But we don't know the value of `n` and we don't know `p` and `q` as well.
- I researched a bit to find if there's a way of computing `n` with the information of `e` and `d` and formulated this method:
  - So `phi = (p-1)(q-1)`
  - `d = e^-1 mod phi`
  - Rewriting the above equation, we get `d * e = 1 mod phi`
  - This implies, `d * e - 1 = 0 mod phi`
  - This means that `de-1` divided by phi gives a remainder of 0, which means that `de-1` is a multiple of phi
  - So `de-1 = k * phi` for some integer `k`
  - This implies, `de-1 = k * (p-1) * (q-1)` which means that `p-1` and `q-1` both are factors of `de-1`
  - So we can find all the factors of `de-1` and then add 1 to each of them and check if they are 128 bits long and prime (as p - 1 + 1 = p which is a prime number of 128 bit length) to get our potential `p` and `q` and store these potential `p`s and `q`s in a list
  - Then we have to go through all possible combinations of `p` and `q` and decrypt the ciphertext using the formula `M = C^d mod (p*q)` and check if the plaintext contains ascii letters and digits only and if it does, then store it in a potential plaintext list
  - If our potential plaintext list has only one element, then we can send that to the server and get our flag.
- I wrote the following script [SRA.py](./SRA.py) to achieve this:
```python
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
```
- Running the script, we get the flag:
```
[+] Opening connection to saturn.picoctf.net on port 51224: Done
anger = 47147759063101709519633272323360812095162305846131507740741806127437584220862
envy = 17792871206550806303569545266418415567522686634343390902596737090816168837937
vainglory?

['7uNvRzDjNIViZ0XI']
/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pwnlib/tubes/tube.py:841: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  res = self.recvuntil(delim, timeout=timeout)
[+] Receiving all data: Done (72B)
[*] Closed connection to saturn.picoctf.net port 51224
7uNvRzDjNIViZ0XI
Conquered!
picoCTF{7h053_51n5_4r3_n0_m0r3_38268294}
```
- It is to be noted that this method only worked because `p` and `q` are relatively easy to brute force.