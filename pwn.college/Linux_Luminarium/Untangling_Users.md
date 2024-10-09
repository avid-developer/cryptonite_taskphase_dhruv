# Untangling Users
## Becoming root with su
- ran `su` in the terminal to switch to the root user and got prompted to enter the root password
- entered the root password `hack-the-planet` and became the root user
- ran `cat /flag` in the terminal to read the contents of the file and got the flag: `pwn.college{w7xR632rmZqrjynK_FhresuyAwg.dVTN0UDL5QTO0czW}`
## Other users with su
- ran `su zardus` in the terminal to switch to the user `zardus` and got prompted to enter the password
- entered the password `dont-hack-me` and became the user `zardus`
- ran `/challenge/run` in the terminal to run the command and got the flag: `pwn.college{8vUb40dv6MwYR5c_sdkWFja9c-S.dZTN0UDL5QTO0czW}`
## Cracking passwords
- ran `john /challenge/shadow-leak` in the terminal to crack the password hashes in the file `shadow-leak`
- got the cracked password `aardvark` for the user `zardus`
- ran `su zardus` in the terminal to switch to the user `zardus` and got prompted to enter the password
- entered the password `aardvark` and became the user `zardus`
- ran `/challenge/run` in the terminal to run the command and got the flag: `pwn.college{8S1wKKjYWAXGEP-aaHUdo2f9KLh.ddTN0UDL5QTO0czW}`
## Using sudo
- ran `sudo cat /flag` in the terminal to read the contents of the file `flag` as the root user and got the flag: `pwn.college{sed_MVaSDgM8sbVdwJzRKutKJOF.dhTN0UDL5QTO0czW}`