# level3.0
## Description
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
## Solution
- The executable program's name is `babyrev-level-3-0`
- Running the program and giving it a test input `abcde`:
```
###
### Welcome to ./babyrev-level-3-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

abcde
Initial input:

        61 62 63 64 65 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

        65 64 63 62 61 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        65 64 63 62 61 

Expected result:

        65 76 73 76 75 

Checking the received license key!

Wrong! No flag for you!
```
- The program takes the input and reverses it, then compares it with the expected result.
- The expected result `65 76 73 76 75` converted hex to ASCII is `evsvu`. Reversing this to get the correct license key `uvsve`.
- Running the program again with the correct license key `uvsve`:
```
###
### Welcome to ./babyrev-level-3-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

uvsve
Initial input:

        75 76 73 76 65 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

        65 76 73 76 75 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        65 76 73 76 75 

Expected result:

        65 76 73 76 75 

Checking the received license key!

You win! Here is your flag:
pwn.college{UFU2vcDykzy7LbkkoRcQIRpfEUt.0VN1IDL5QTO0czW}
```
- The flag is `pwn.college{UFU2vcDykzy7LbkkoRcQIRpfEUt.0VN1IDL5QTO0czW}`.