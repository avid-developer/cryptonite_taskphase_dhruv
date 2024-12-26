# level1.0
## Description
Reverse engineer this challenge to find the correct license key.
## Solution
- ran `cd /challenge` in the terminal to navigate to the challenge directory. This is where the executable file is located.
- ran `ls` to list the files in the directory. The executable file is named `babyrev-level-1-0`.
- ran `./babyrev-level-1-0` to run the executable file. This is the output:
```
###
### Welcome to ./babyrev-level-1-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

```
- The program is expecting an input. I gave a sample input `test` and the program continued the execution:
```
test
Initial input:

        74 65 73 74 0a

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        74 65 73 74 0a 

Expected result:

        6b 62 61 78 76 

Checking the received license key!

Wrong! No flag for you!
```
- I noticed 2 things:
  - There is no "mangling" done to the input. `Initial input` and `Final result of mangling input` are the same.
  - My entered input `test` is just converted to hex. I verified this by using an online [tool](https://www.rapidtables.com/convert/number/hex-to-ascii.html) to convert `74 65 73 74 0a` to ASCII.
- This means that I can just convert the expected result `6b 62 61 78 76` to ASCII to get the correct license key.
- I converted `6b 62 61 78 76` to ASCII and got `kbaxv`.
- I ran the binary file again and entered `kbaxv` as the input license key:
```
###
### Welcome to ./babyrev-level-1-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

kbaxv
Initial input:

        6b 62 61 78 76 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        6b 62 61 78 76 

Expected result:

        6b 62 61 78 76 

Checking the received license key!

You win! Here is your flag:
pwn.college{w4GURSDKxTEYLJ0KZ79-Ng53Gf4.0VM1IDL5QTO0czW}
```
- The flag is `pwn.college{w4GURSDKxTEYLJ0KZ79-Ng53Gf4.0VM1IDL5QTO0czW}`.