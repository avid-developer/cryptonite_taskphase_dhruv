# level5.0
## Description
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
## Solution
- The executable program's name is `babyrev-level-5-0`
- Running the program and giving it a test input `bacde`:
```
###
### Welcome to ./babyrev-level-5-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

bacde
Initial input:

        62 61 63 64 65 

This challenge is now mangling your input using the `xor` mangler with key `0x46`

This mangled your input, resulting in:

        24 27 25 22 23 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        24 27 25 22 23 

Expected result:

        34 3c 2f 27 37 

Checking the received license key!

Wrong! No flag for you!
```
- The program takes the input and mangles it using the `xor` mangler with key `0x46` and compares the result with the expected result.
- We can get the correct license key by xoring the expected result with the key `0x46` (as xoring twice will give the original value).
- Using an [online tool](https://md5decrypt.net/en/Xor/) to xor the expected result `34 3c 2f 27 37` with the key `0x46` and got `727a696171`. 
- Converting this hex to ASCII gives the correct license key `rziaq`.
- Running the program again with the correct license key `rziaq`:
```
###
### Welcome to ./babyrev-level-5-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

rziaq
Initial input:

        72 7a 69 61 71 

This challenge is now mangling your input using the `xor` mangler with key `0x46`

This mangled your input, resulting in:

        34 3c 2f 27 37 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        34 3c 2f 27 37 

Expected result:

        34 3c 2f 27 37 

Checking the received license key!

You win! Here is your flag:
pwn.college{IS8PaVeRl83IVxRpg3v2yKxoClT.0VO1IDL5QTO0czW}
```
- Flag: `pwn.college{IS8PaVeRl83IVxRpg3v2yKxoClT.0VO1IDL5QTO0czW}`