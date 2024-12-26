# level7.0
## Description
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
## Solution
- The executable program's name is `babyrev-level-7-0`
- Running the program and giving it a test input `bacde`:
```
###
### Welcome to ./babyrev-level-7-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

bacde
Initial input:

        62 61 63 64 65 0a 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0a 65 64 63 61 62 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

        62 61 63 64 65 0a 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0a 65 64 63 61 62 

This challenge is now mangling your input using the `sort` mangler.

This mangled your input, resulting in:

        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0a 61 62 63 64 65 

This challenge is now mangling your input using the `swap` mangler for indexes `0` and `20`.

This mangled your input, resulting in:

        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0a 61 62 63 64 65 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0a 61 62 63 64 65 

Expected result:

        73 63 64 66 66 67 67 69 6a 6a 6a 6b 6c 6c 6f 6f 70 70 72 72 61 74 75 75 78 79 7a 7a 

Checking the received license key!

Wrong! No flag for you!
```
- The program mangles the input by doing the following:
  - Reverse the input thrice (effectively reversing the input once)
  - Sorts the result in ascending order of the ASCII values
  - Swaps the characters at index 0 and 20
  - Compares the result with the expected result
- To get the correct license key, we need to reverse the mangling process:
  - Swap the characters at index 0 and 20
  - Sort the result in descending order of the ASCII values
  - Reverse the result.
- The expected result is `73 63 64 66 66 67 67 69 6a 6a 6a 6b 6c 6c 6f 6f 70 70 72 72 61 74 75 75 78 79 7a 7a`.
- Swapping the characters at index 0 and 20 gives us `61 63 64 66 66 67 67 69 6a 6a 6a 6b 6c 6c 6f 6f 70 70 72 72 73 74 75 75 78 79 7a 7a`.
- I sorted this in descending order using an [online tool](https://www.rajeshvu.com/storage/emc/utils/general/sorthexnumbers): `7A 7A 79 78 75 75 74 73 72 72 70 70 6F 6F 6C 6C 6B 6A 6A 6A 69 67 67 66 66 64 63 61`.
- Reversed this result with the help of an LLM: `61636466666767696A6A6A6B6C6C6F6F707072727374757578797A7A`.
- Converted this to ASCII text: `acdffggijjjklloopprrstuuxyzz`.
- Similar to previous levels, we can give this as input to the program to get the flag.
- Running the program with the license key `acdffggijjjklloopprrstuuxyzz`:
```
###
### Welcome to ./babyrev-level-7-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

acdffggijjjklloopprrstuuxyzz
Initial input:

        61 63 64 66 66 67 67 69 6a 6a 6a 6b 6c 6c 6f 6f 70 70 72 72 73 74 75 75 78 79 7a 7a 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

        7a 7a 79 78 75 75 74 73 72 72 70 70 6f 6f 6c 6c 6b 6a 6a 6a 69 67 67 66 66 64 63 61 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

        61 63 64 66 66 67 67 69 6a 6a 6a 6b 6c 6c 6f 6f 70 70 72 72 73 74 75 75 78 79 7a 7a 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

        7a 7a 79 78 75 75 74 73 72 72 70 70 6f 6f 6c 6c 6b 6a 6a 6a 69 67 67 66 66 64 63 61 

This challenge is now mangling your input using the `sort` mangler.

This mangled your input, resulting in:

        61 63 64 66 66 67 67 69 6a 6a 6a 6b 6c 6c 6f 6f 70 70 72 72 73 74 75 75 78 79 7a 7a 

This challenge is now mangling your input using the `swap` mangler for indexes `0` and `20`.

This mangled your input, resulting in:

        73 63 64 66 66 67 67 69 6a 6a 6a 6b 6c 6c 6f 6f 70 70 72 72 61 74 75 75 78 79 7a 7a 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        73 63 64 66 66 67 67 69 6a 6a 6a 6b 6c 6c 6f 6f 70 70 72 72 61 74 75 75 78 79 7a 7a 

Expected result:

        73 63 64 66 66 67 67 69 6a 6a 6a 6b 6c 6c 6f 6f 70 70 72 72 61 74 75 75 78 79 7a 7a 

Checking the received license key!

You win! Here is your flag:
pwn.college{Qte1XG5AEKh0dhLXHtndSkUfJTa.01M2IDL5QTO0czW}
```
- The flag is `pwn.college{Qte1XG5AEKh0dhLXHtndSkUfJTa.01M2IDL5QTO0czW}`.