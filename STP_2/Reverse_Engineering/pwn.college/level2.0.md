# level2.0
## Description
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
## Solution
- The executable program's name is `babyrev-level-2-0`
- Running the program and giving it a `test` input:
```
###
### Welcome to ./babyrev-level-2-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

test
Initial input:

        74 65 73 74 0a 

This challenge is now mangling your input using the `swap` mangler for indexes `1` and `4`.

This mangled your input, resulting in:

        74 0a 73 74 65 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        74 0a 73 74 65 

Expected result:

        6a 76 73 79 6f 

Checking the received license key!

Wrong! No flag for you!
```
- The program takes the input and swaps the bytes at indexes `1` and `4` and compares the result with the expected result.
- Using an online [tool](https://www.rapidtables.com/convert/number/hex-to-ascii.html) to convert the expected result to ASCII, we get `jvsyo`.
- But since the indexes 1 and 4 are swapped, we need to swap them back to get the correct license key.
- The correct license key is `josyv`.
- Running the program and giving it the correct license key:
```
###
### Welcome to ./babyrev-level-2-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

josyv
Initial input:

        6a 6f 73 79 76 

This challenge is now mangling your input using the `swap` mangler for indexes `1` and `4`.

This mangled your input, resulting in:

        6a 76 73 79 6f 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        6a 76 73 79 6f 

Expected result:

        6a 76 73 79 6f 

Checking the received license key!

You win! Here is your flag:
pwn.college{o3TEMS83PN_clh2h_w-adevDjTH.01M1IDL5QTO0czW}
```
- The flag is `pwn.college{o3TEMS83PN_clh2h_w-adevDjTH.01M1IDL5QTO0czW}`.