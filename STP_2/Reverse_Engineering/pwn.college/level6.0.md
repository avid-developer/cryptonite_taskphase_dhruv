# level6.0
## Description
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
## Solution
- The executable program's name is `babyrev-level-6-0`
- Running the program and giving it a test input `bacde`:
```
###
### Welcome to ./babyrev-level-6-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

bacde
Initial input:

        62 61 63 64 65 0a 00 00 00 00 00 00 00 00 00 00 00 00 00 

This challenge is now mangling your input using the `sort` mangler.

This mangled your input, resulting in:

        00 00 00 00 00 00 00 00 00 00 00 00 00 0a 61 62 63 64 65 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

        65 64 63 62 61 0a 00 00 00 00 00 00 00 00 00 00 00 00 00 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

        00 00 00 00 00 00 00 00 00 00 00 00 00 0a 61 62 63 64 65 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        00 00 00 00 00 00 00 00 00 00 00 00 00 0a 61 62 63 64 65 

Expected result:

        61 66 66 67 68 6a 6d 6d 71 72 73 75 75 76 76 77 78 79 7a 

Checking the received license key!

Wrong! No flag for you!
```
- The program mangles the input by sorting the input and reversing it twice.
- Since reversing the sorted input twice effectively does nothing, the program just takes the input, sorts it, and then compares it with the expected result.
- Similar to [level4.0](./level4.0.md), we can directly enter the expected result as the license key to get the flag.
- Converting the expected result `61 66 66 67 68 6a 6d 6d 71 72 73 75 75 76 76 77 78 79 7a` to ASCII gives `affghjmmqrsuuvvwxyz`.
- Running the program and giving it `affghjmmqrsuuvvwxyz` as the license key:
```
###
### Welcome to ./babyrev-level-6-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

affghjmmqrsuuvvwxyz                                     
Initial input:

        61 66 66 67 68 6a 6d 6d 71 72 73 75 75 76 76 77 78 79 7a 

This challenge is now mangling your input using the `sort` mangler.

This mangled your input, resulting in:

        61 66 66 67 68 6a 6d 6d 71 72 73 75 75 76 76 77 78 79 7a 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

        7a 79 78 77 76 76 75 75 73 72 71 6d 6d 6a 68 67 66 66 61 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

        61 66 66 67 68 6a 6d 6d 71 72 73 75 75 76 76 77 78 79 7a 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        61 66 66 67 68 6a 6d 6d 71 72 73 75 75 76 76 77 78 79 7a 

Expected result:

        61 66 66 67 68 6a 6d 6d 71 72 73 75 75 76 76 77 78 79 7a 

Checking the received license key!

You win! Here is your flag:
pwn.college{Yj7E-Oay4wBwbYMU93YaAxoeMm0.0VM2IDL5QTO0czW}
```
- The flag is `pwn.college{Yj7E-Oay4wBwbYMU93YaAxoeMm0.0VM2IDL5QTO0czW}`.