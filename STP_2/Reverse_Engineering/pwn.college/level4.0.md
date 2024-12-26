# level4.0
## Description
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
## Solution
- The executable program's name is `babyrev-level-4-0`
- Running the program and giving it a test input `abcde`:
```
###
### Welcome to ./babyrev-level-4-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

abcde
Initial input:

        61 62 63 64 65 

This challenge is now mangling your input using the `sort` mangler.

This mangled your input, resulting in:

        61 62 63 64 65 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        61 62 63 64 65 

Expected result:

        64 65 69 6f 73 

Checking the received license key!

Wrong! No flag for you!
```
- The mangled input didn't change, which is weird because a similar no change in mangling happened in [level1.0](./level1.0.md). So, I tried to give the program a different input `bacde`:
```
###
### Welcome to ./babyrev-level-4-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

bacde
Initial input:

        62 61 63 64 65 

This challenge is now mangling your input using the `sort` mangler.

This mangled your input, resulting in:

        61 62 63 64 65 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        61 62 63 64 65 

Expected result:

        64 65 69 6f 73 

Checking the received license key!

Wrong! No flag for you!
```
- The mangling seems to be sorting the input characters in ascending order of their ASCII values. 
- This is confirmed by the fact that the expected result is `64 65 69 6f 73`, hex values in increasing order.
- Converting this to ASCII gives `deios`. This is the correct license key.
- Running the program with the correct license key:
```
###
### Welcome to ./babyrev-level-4-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

deios
Initial input:

        64 65 69 6f 73 

This challenge is now mangling your input using the `sort` mangler.

This mangled your input, resulting in:

        64 65 69 6f 73 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        64 65 69 6f 73 

Expected result:

        64 65 69 6f 73 

Checking the received license key!

You win! Here is your flag:
pwn.college{YBa3f32TtY11iRFl7WDEY0oKVII.01N1IDL5QTO0czW}
```
- Flag is: `pwn.college{YBa3f32TtY11iRFl7WDEY0oKVII.01N1IDL5QTO0czW}`
- One thing to note is that `deios` is not the only correct license key. Any permutation of `deios` like `soide` or `eidos` will also work as the program will sort the input before comparing it to the expected result.