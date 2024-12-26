# Sum-O-Primes
## Description
We have so much faith in RSA we give you not just the product of the primes, but their sum as well!
- [gen.py](./gen.py)
- [output.txt](./output.txt)
## Hint
I love squares :)
## Solution
- This is what's there in [gen.py](./gen.py)
```python
#!/usr/bin/python

from binascii import hexlify
from gmpy2 import mpz_urandomb, next_prime, random_state
import math
import os
import sys

if sys.version_info < (3, 9):
    import gmpy2
    math.gcd = gmpy2.gcd
    math.lcm = gmpy2.lcm

FLAG  = open('flag.txt').read().strip()
FLAG  = int(hexlify(FLAG.encode()), 16)
SEED  = int(hexlify(os.urandom(32)).decode(), 16)
STATE = random_state(SEED)

def get_prime(bits):
    return next_prime(mpz_urandomb(STATE, bits) | (1 << (bits - 1)))

p = get_prime(1024)
q = get_prime(1024)

x = p + q
n = p * q

e = 65537

m = math.lcm(p - 1, q - 1)
d = pow(e, -1, m)

c = pow(FLAG, e, n)

print(f'x = {x:x}')
print(f'n = {n:x}')
print(f'c = {c:x}')
```
- And these are the contents of [output.txt](./output.txt)
```
x = 1626a189dcb38ca6b8e9ee26623ab5c3c6cd7e4c7ff6726f4b03831ca48c617a056827c5763458d0aa7172650072b892649cc73f943f156b795ff5dd2fc9a53b140cf9c3ee2cbb8181d17bb0275f404b4090766f798ad156db7e71000e93db65f3e1bc7406532d0f509fbecf095ef215b4ad51f5e8ac765861e5f93808948bf72
n = 720d66204ec312d7f1bc688495d4585ec58520170b86ed3488c3f9c76407b7e9e466b82a282ba90d484698160f2e27f413b07cf8805d560abdffa977547d5fec3190a1ce284dfc8e92193f2f70590bf9c6e6d0ab449e35ef43ed20232b7f8686696125cde1f950230fbc6858392a3715c1b8a4947748b7fadd5cc921716ad5e0129c91ea88fceee140fb1c594606186afacb69143ef8f7b3b1aa2cc3206395c60e71ec0555dd15838d8a8395e8ccf9a4e4c4199ae0ab3f8af7ebc6605edc5ddd480be2d6c41e38618eba5822a1e566080877268802750de71e890ac865ebf87fdc290d9151e407dff4c97390c9e7388fd538e2716515cea2240f55963c2e0c21
c = 554b90eb12fbece709d7bf23ab91f9b52d71cd77fbf42f65d68623c2055d99956b9bcf2eaf14771fa5781fae86624e44b452a0f68768849faba1b9695ce353a17238a3e7040ee7aede68b35bf4b51daf0982653910b280ac98aad9a5b3c49d226e10b2e8660effc2cb2a553039bde527e42f1795bc078af6ed2928505be6df1ebe993f2ed8c10477dd5cc9f899d1e69b6512b71c732472dde521f5393c76b2f9fbed668560d4e50ca177dd14b923414549d688b20fab94dba7cad7b5a729941c772dc4a1db79b0e6a111d2d2e8998b4e2a272dc940a9dd4cf856faa5a2ee0cb6f36f0ce6edbb421697e517a4d589cc5a880eecf6fbf65e5f6a1a437b06e5ff9a
```
- So the script encrypts the flag using RSA (I noticed it uses the LCM method instead of the Euler's Totient function to calculate the private key, but that's not important for this challenge), and gives us the sum of the primes used to generate the RSA modulus, the modulus itself, and the ciphertext in hexadecimal format.
- we can use a simple quadric equation to find the primes `p` and `q`:
  - We have the 2 equations:
    - `p + q = x`
    - `p * q = n`
  - We can rewrite the first equation as `p = x - q`, and substitute it in the second equation:
    - `(x - q) * q = n`
    - `q^2 - x * q + n = 0`
  - this can be compared to the general form of a quadric equation `ax^2 + bx + c = 0` where:
    - `a = 1`
    - `b = -x`
    - `c = n`
  - we can use the quadric formula to find the value of `q`:
    - `q = (-b + sqrt(b^2 - 4ac)) / 2a`
  - and then calculate p as `p = n / q`
- we can then use the following lines from [gen.py](./gen.py) to find `m` and `d`:
```python
m = math.lcm(p - 1, q - 1)
d = pow(e, -1, m)
```
- then we can decrypt the ciphertext using the following line:
```python
flag = pow(cipher, d, n)
```
- since [gen.py](./gen.py) converted the flag to hex using `hexlify`, we need to convert the decrypted flag back to bytes using `unhexlify`
- wrote the following script [Sum-o-primes.py](./Sum-o-primes.py) to decrypt the flag:
```python
import gmpy2
import math
from binascii import unhexlify

x = int(0x1626a189dcb38ca6b8e9ee26623ab5c3c6cd7e4c7ff6726f4b03831ca48c617a056827c5763458d0aa7172650072b892649cc73f943f156b795ff5dd2fc9a53b140cf9c3ee2cbb8181d17bb0275f404b4090766f798ad156db7e71000e93db65f3e1bc7406532d0f509fbecf095ef215b4ad51f5e8ac765861e5f93808948bf72)
n = int(0x720d66204ec312d7f1bc688495d4585ec58520170b86ed3488c3f9c76407b7e9e466b82a282ba90d484698160f2e27f413b07cf8805d560abdffa977547d5fec3190a1ce284dfc8e92193f2f70590bf9c6e6d0ab449e35ef43ed20232b7f8686696125cde1f950230fbc6858392a3715c1b8a4947748b7fadd5cc921716ad5e0129c91ea88fceee140fb1c594606186afacb69143ef8f7b3b1aa2cc3206395c60e71ec0555dd15838d8a8395e8ccf9a4e4c4199ae0ab3f8af7ebc6605edc5ddd480be2d6c41e38618eba5822a1e566080877268802750de71e890ac865ebf87fdc290d9151e407dff4c97390c9e7388fd538e2716515cea2240f55963c2e0c21)
cipher = int(0x554b90eb12fbece709d7bf23ab91f9b52d71cd77fbf42f65d68623c2055d99956b9bcf2eaf14771fa5781fae86624e44b452a0f68768849faba1b9695ce353a17238a3e7040ee7aede68b35bf4b51daf0982653910b280ac98aad9a5b3c49d226e10b2e8660effc2cb2a553039bde527e42f1795bc078af6ed2928505be6df1ebe993f2ed8c10477dd5cc9f899d1e69b6512b71c732472dde521f5393c76b2f9fbed668560d4e50ca177dd14b923414549d688b20fab94dba7cad7b5a729941c772dc4a1db79b0e6a111d2d2e8998b4e2a272dc940a9dd4cf856faa5a2ee0cb6f36f0ce6edbb421697e517a4d589cc5a880eecf6fbf65e5f6a1a437b06e5ff9a)

a, b, c = 1, -x, n
p = (-b + int(gmpy2.isqrt(b**2 - 4*a*c))) // (2*a)
q = n // p

e = 65537

m = math.lcm(p - 1, q - 1)
d = pow(e, -1, m)

flag = pow(cipher, d, n)

print(unhexlify(hex(flag)[2:])).decode()
```
- A few things to note:
  - changed the variable `c` from [output.txt](./output.txt) to `cipher` to avoid confusion with the variable `c` in the quadratic equation
  - I converted `x`, `n`, and `cipher` to integers as RSA works with integers
  - I used `gmpy2.isqrt` instead of `math.isqrt` to avoid floating point errors
  - I used `hex(flag)[2:]` to convert the decrypted flag to hex, and then removed the `0x` at the beginning of the hex string before sending it to `unhexlify`, as the hex string needs to be properly formatted.
- Running the script gives us the flag `picoCTF{pl33z_n0_g1v3_c0ngru3nc3_0f_5qu4r35_92fe3557}`