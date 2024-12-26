# level8.0
## Description
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
## Solution
- The executable program's name is `babyrev-level-8-0`
- Running the program and giving it a test input `bacde`:
```
###
### Welcome to ./babyrev-level-8-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

bacde
Initial input:

        62 61 63 64 65 0a 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0a 65 64 63 61 62 

This challenge is now mangling your input using the `xor` mangler with key `0x8f076ea2f8b6bc`

This mangled your input, resulting in:

        8f 07 6e a2 f8 b6 bc 8f 07 6e a2 f8 b6 bc 8f 07 6e a2 f8 b6 bc 8f 07 6e a2 f8 b6 bc 8f 07 6e a8 9d d2 df ee 65 

This challenge is now mangling your input using the `swap` mangler for indexes `5` and `30`.

This mangled your input, resulting in:

        8f 07 6e a2 f8 6e bc 8f 07 6e a2 f8 b6 bc 8f 07 6e a2 f8 b6 bc 8f 07 6e a2 f8 b6 bc 8f 07 b6 a8 9d d2 df ee 65 

This challenge is now mangling your input using the `xor` mangler with key `0x3d77c16466`

This mangled your input, resulting in:

        b2 70 af c6 9e 53 cb 4e 63 08 9f 8f 77 d8 e9 3a 19 63 9c d0 81 f8 c6 0a c4 c5 c1 7d eb 61 8b df 5c b6 b9 d3 12 

This challenge is now mangling your input using the `sort` mangler.

This mangled your input, resulting in:

        08 0a 12 19 3a 4e 53 5c 61 63 63 70 77 7d 81 8b 8f 9c 9e 9f af b2 b6 b9 c1 c4 c5 c6 c6 cb d0 d3 d8 df e9 eb f8 

This challenge is now mangling your input using the `xor` mangler with key `0x494e4778`

This mangled your input, resulting in:

        41 44 55 61 73 00 14 24 28 2d 24 08 3e 33 c6 f3 c6 d2 d9 e7 e6 fc f1 c1 88 8a 82 be 8f 85 97 ab 91 91 ae 93 b1 

This challenge is now mangling your input using the `xor` mangler with key `0x93cdcd39`

This mangled your input, resulting in:

        d2 89 98 58 e0 cd d9 1d bb e0 e9 31 ad fe 0b ca 55 1f 14 de 75 31 3c f8 1b 47 4f 87 1c 48 5a 92 02 5c 63 aa 22 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        d2 89 98 58 e0 cd d9 1d bb e0 e9 31 ad fe 0b ca 55 1f 14 de 75 31 3c f8 1b 47 4f 87 1c 48 5a 92 02 5c 63 aa 22 

Expected result:

        da 80 8e 45 cb 97 93 65 f3 d0 dc 21 b8 ed 1b d9 44 21 22 e9 70 2f 38 f3 68 36 3d f8 19 5b 56 a5 36 70 7c ba 21 

Checking the received license key!

Wrong! No flag for you!
```
- We need to simply reverse the mangling process to get the correct license key.
- One thing to note is that, for example, xoring with the key `0x93cdcd39` means that:
  - `index % 0 == 0` is xored with `0x93`
  - `index % 1 == 0` is xored with `0xcd`
  - `index % 2 == 0` is xored with `0xcd`
  - `index % 3 == 0` is xored with `0x39`, and similar pattern for rest of the xor keys
- Wrote a [script](./level8.0.py) to reverse the mangling process and get the correct license key:
```python
# Initial hex array
buf = [0xda, 0x80, 0x8e, 0x45, 0xcb, 0x97, 0x93, 0x65, 0xf3, 0xd0, 0xdc, 0x21,
       0xb8, 0xed, 0x1b, 0xd9, 0x44, 0x21, 0x22, 0xe9, 0x70, 0x2f, 0x38, 0xf3,
       0x68, 0x36, 0x3d, 0xf8, 0x19, 0x5b, 0x56, 0xa5, 0x36, 0x70, 0x7c, 0xba, 0x21]

# First XOR with 0x93cdcd39
key1 = [0x93, 0xcd, 0xcd, 0x39]
for i in range(len(buf)):
    buf[i] ^= key1[i % 4]

# Second XOR with 0x494e4778
key2 = [0x49, 0x4e, 0x47, 0x78]
for i in range(len(buf)):
    buf[i] ^= key2[i % 4]

# Sort in descending order
buf.sort(reverse=True)

# Third XOR with 0x3d77c16466
key3 = [0x3d, 0x77, 0xc1, 0x64, 0x66]
for i in range(len(buf)):
    buf[i] ^= key3[i % 5]

# Swap indexes 5 and 30
buf[5], buf[30] = buf[30], buf[5]

# Fourth XOR with 0x8f076ea2f8b6bc
key4 = [0x8f, 0x07, 0x6e, 0xa2, 0xf8, 0xb6, 0xbc]
for i in range(len(buf)):
    buf[i] ^= key4[i % 7]

# Reverse array
buf = buf[::-1]

# Convert to ASCII and print
result = ''.join(chr(x) for x in buf)
print(result)

# Print hex values
print("Hex values:", [hex(x) for x in buf])
```
- Running the script, I got special characters in the output (```p±ÞÖ(Á·EÂ.¥¦dW`r4Ë³[jÅ:(± r5YI```), so I can't directly use this text as the license key as it may be interpreted incorrectly.
- After chatting with an LLM, I found out that I can use the following command to directly send the raw bytes to the license checker:
```bash
echo -ne "\x70\xb1\xde\xd6\x28\xc1\xb7\x45\xc2\x2e\x97\xa5\xa6\x64\x57\x60\x1f\x72\x34\xcb\xb3\x96\x5b\x6a\xc5\x3a\x28\xb1\xa0\x96\x17\x92\x72\x35\x59\x8b\x49" | ./babyrev-level-8-0
```
- `\x` is an escape sequence which tells bash to interpret the following two characters as a hexadecimal number.
- The `-n` echo flag tells echo not to print a newline at the end of the string.
- The `-e` flag tells echo to interpret escape sequences (`\x`) in our case.
- Running the command, I got the flag:
```
###
### Welcome to ./babyrev-level-8-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

Initial input:

        70 b1 de d6 28 c1 b7 45 c2 2e 97 a5 a6 64 57 60 1f 72 34 cb b3 96 5b 6a c5 3a 28 b1 a0 96 17 92 72 35 59 8b 49 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

        49 8b 59 35 72 92 17 96 a0 b1 28 3a c5 6a 5b 96 b3 cb 34 72 1f 60 57 64 a6 a5 97 2e c2 45 b7 c1 28 d6 de b1 70 

This challenge is now mangling your input using the `xor` mangler with key `0x8f076ea2f8b6bc`

This mangled your input, resulting in:

        c6 8c 37 97 8a 24 ab 19 a7 df 8a c2 73 d6 d4 91 dd 69 cc c4 a3 ef 50 0a 04 5d 21 92 4d 42 d9 63 d0 60 62 3e 77 

This challenge is now mangling your input using the `swap` mangler for indexes `5` and `30`.

This mangled your input, resulting in:

        c6 8c 37 97 8a d9 ab 19 a7 df 8a c2 73 d6 d4 91 dd 69 cc c4 a3 ef 50 0a 04 5d 21 92 4d 42 24 63 d0 60 62 3e 77 

This challenge is now mangling your input using the `xor` mangler with key `0x3d77c16466`

This mangled your input, resulting in:

        fb fb f6 f3 ec e4 dc d8 c3 b9 b7 b5 b2 b2 b2 ac aa a8 a8 a2 9e 98 91 6e 62 60 56 53 29 24 19 14 11 04 04 03 00 

This challenge is now mangling your input using the `sort` mangler.

This mangled your input, resulting in:

        00 03 04 04 11 14 19 24 29 53 56 60 62 6e 91 98 9e a2 a8 a8 aa ac b2 b2 b2 b5 b7 b9 c3 d8 dc e4 ec f3 f6 fb fb 

This challenge is now mangling your input using the `xor` mangler with key `0x494e4778`

This mangled your input, resulting in:

        49 4d 43 7c 58 5a 5e 5c 60 1d 11 18 2b 20 d6 e0 d7 ec ef d0 e3 e2 f5 ca fb fb f0 c1 8a 96 9b 9c a5 bd b1 83 b2 

This challenge is now mangling your input using the `xor` mangler with key `0x93cdcd39`

This mangled your input, resulting in:

        da 80 8e 45 cb 97 93 65 f3 d0 dc 21 b8 ed 1b d9 44 21 22 e9 70 2f 38 f3 68 36 3d f8 19 5b 56 a5 36 70 7c ba 21 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        da 80 8e 45 cb 97 93 65 f3 d0 dc 21 b8 ed 1b d9 44 21 22 e9 70 2f 38 f3 68 36 3d f8 19 5b 56 a5 36 70 7c ba 21 

Expected result:

        da 80 8e 45 cb 97 93 65 f3 d0 dc 21 b8 ed 1b d9 44 21 22 e9 70 2f 38 f3 68 36 3d f8 19 5b 56 a5 36 70 7c ba 21 

Checking the received license key!

You win! Here is your flag:
pwn.college{E5FEReN8I1UURBPNFJnQzn7mI76.0VN2IDL5QTO0czW}
```
- The flag is `pwn.college{E5FEReN8I1UURBPNFJnQzn7mI76.0VN2IDL5QTO0czW}`.