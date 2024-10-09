# Perceiving Permissions
## Changing File Ownership
- ran `chmod hacker /flag` in the terminal to change the ownership of the file `flag` to the user `hacker`
- ran `/flag` in the terminal but was greeted with a permission denied error
- ran `ls -l` to try and understand the permissions of the file `flag` and saw that the file was owned by `hacker` but only had read and write permissions for the owner
- ran `cat /flag` in the terminal to read the contents of the file and got the flag: `pwn.college{IVAszXVkfwFX8YIpuBd6dpRAhBI.dFTM2QDL5QTO0czW}`
## Groups and Files
- ran `chgrp hacker /flag` in the terminal to change the group of the file `flag` to the group `hacker`
- ran `cat /flag` in the terminal to read the contents of the file and got the flag: `pwn.college{YfewQu3vOLs1dsTGVUtF4FSSWQQ.dFzNyUDL5QTO0czW}`
## Fun With Groups Names
- ran `id` in the terminal to see the user and group information
- found the name of the randomised group `hacker` user is in to be `grp28153`
- ran `chgrp grp28153 /flag` in the terminal to change the group of the file `flag` to the group `grp28153`
- ran `cat /flag` in the terminal to read the contents of the file and got the flag: `pwn.college{Il6t7kfh1IILZtfcmJ-RYvLT-AE.dJzNyUDL5QTO0czW}`
## Changing Permissions
- ran `chmod o+r /flag` in the terminal to add read permissions for others (including the `hacker` user) to the file `flag`
- ran `cat /flag` in the terminal to read the contents of the file and got the flag: `pwn.college{ANkHj7oaTbRAMvrawqgM8QiyRcD.dNzNyUDL5QTO0czW}`
## Executable Files
- ran `ls -l /challenge/run` in the terminal to check the permissions of the file `run`
- saw that the file was owned by `hacker` and did not have execute permissions for the owner
- ran `chmod u+x /challenge/run` in the terminal to add execute permissions for the owner to the file `run`
- ran `/challenge/run` in the terminal to run the command and got the flag: `pwn.college{YanTKnCTLHnLoVun7PP2Ixoqy21.dJTM2QDL5QTO0czW}`
## Permission Tweaking Practice
- ran `/challenge/run` in the terminal to run the command and got the following output:  
```
Round 0 (of 8)!

Current permissions of "/challenge/pwn": rw-r--r--
Needed permissions of "/challenge/pwn": rw-r-xr-x
```
- ran `chmod go+x /challenge/pwn` in the terminal to add execute permissions for the group and others to the file `pwn` and got the following output:  
```
You set the correct permissions!
Round 1 (of 8)!

Current permissions of "/challenge/pwn": rw-r-xr-x
Needed permissions of "/challenge/pwn": rw-r-xrwx
```
- ran `chmod o+w /challenge/pwn` in the terminal to add write permissions for others to the file `pwn` and got the following output:  
```
You set the correct permissions!
Round 2 (of 8)!

Current permissions of "/challenge/pwn": rw-r-xrwx
Needed permissions of "/challenge/pwn": rwxr-xrwx
```
- ran `chmod u+x /challenge/pwn` in the terminal to add execute permissions for the owner to the file `pwn` and got the following output:  
```
You set the correct permissions!
Round 3 (of 8)!

Current permissions of "/challenge/pwn": rwxr-xrwx
Needed permissions of "/challenge/pwn": rwxrwxrwx
```
- ran `chmod g+w /challenge/pwn` in the terminal to add write permissions for the group to the file `pwn` and got the following output:  
```
You set the correct permissions!
Round 4 (of 8)!

Current permissions of "/challenge/pwn": rwxrwxrwx
Needed permissions of "/challenge/pwn": rwxrwx-w-
```
- ran `chmod o-rx /challenge/pwn` in the terminal to remove read and execute permissions for others from the file `pwn` and got the following output:  
```
You set the correct permissions!
Round 5 (of 8)!

Current permissions of "/challenge/pwn": rwxrwx-w-
Needed permissions of "/challenge/pwn": ---------
```
- ran `chmod a-rwx /challenge/pwn` in the terminal to remove all permissions for all users from the file `pwn` and got the following output:  
```
You set the correct permissions!
Round 6 (of 8)!

Current permissions of "/challenge/pwn": ---------
Needed permissions of "/challenge/pwn": rwxrwx---
```
- ran `chmod ug+rwx /challenge/pwn` in the terminal to add read, write, and execute permissions for the owner and group to the file `pwn` and got the following output:  
```
You set the correct permissions!
Round 7 (of 8)!

Current permissions of "/challenge/pwn": rwxrwx---
Needed permissions of "/challenge/pwn": ---------
```
- ran `chmod a-rwx /challenge/pwn` in the terminal to remove all permissions for all users from the file `pwn` and got the following output:  
```
You set the correct permissions!
You've solved all 8 rounds! I have changed the ownership
of the /flag file so that you can 'chmod' it. You won't be able to read
it until you make it readable with chmod!

Current permissions of "/flag": ---------
```
- ran `chmod a+r /flag` in the terminal to add read permissions for all users to the file `flag`
- ran `cat /flag` in the terminal to read the contents of the file and got the flag: `pwn.college{cymTwiD4LQsW-hnimtVIuS5hOqq.dBTM2QDL5QTO0czW}`
## Permissions Setting Practice
- ran `/challenge/run` in the terminal to run the command and got the following output:  
```
Round 0 (of 8)!

Current permissions of "/challenge/pwn": rw-r--r--
Needed permissions of "/challenge/pwn": --xr-xr-x
```
- ran `chmod u=x,g=rx,o=rx /challenge/pwn` in the terminal to set the permissions of the file `pwn` to `--xr-xr-x` and got the following output:  
```
You set the correct permissions!
Round 1 (of 8)!

Current permissions of "/challenge/pwn": --xr-xr-x
Needed permissions of "/challenge/pwn": -wx-wxrw-
```
- ran `chmod u=wx,g=wx,o=rw /challenge/pwn` in the terminal to set the permissions of the file `pwn` to `-wx-wxrw-` and got the following output:  
```
You set the correct permissions!
Round 2 (of 8)!

Current permissions of "/challenge/pwn": -wx-wxrw-
Needed permissions of "/challenge/pwn": r--r---wx
```
- ran `chmod u=r,g=r,o=wx /challenge/pwn` in the terminal to set the permissions of the file `pwn` to `r--r---wx` and got the following output:  
```
You set the correct permissions!
Round 3 (of 8)!

Current permissions of "/challenge/pwn": r--r---wx
Needed permissions of "/challenge/pwn": --xr-xr--
```
- ran `chmod u=x,g=rx,o=r /challenge/pwn` in the terminal to set the permissions of the file `pwn` to `--xr-xr--` and got the following output:  
```
You set the correct permissions!
Round 4 (of 8)!

Current permissions of "/challenge/pwn": --xr-xr--
Needed permissions of "/challenge/pwn": ----wx---
```
- ran `chmod u=-,g=wx,o=- /challenge/pwn` in the terminal to set the permissions of the file `pwn` to `----wx---` and got the following output:  
```
You set the correct permissions!
Round 5 (of 8)!

Current permissions of "/challenge/pwn": ----wx---
Needed permissions of "/challenge/pwn": r-x-wxr--
```
- ran `chmod u=rx,g=wx,o=r /challenge/pwn` in the terminal to set the permissions of the file `pwn` to `r-x-wxr--` and got the following output:  
```
You set the correct permissions!
Round 6 (of 8)!

Current permissions of "/challenge/pwn": r-x-wxr--
Needed permissions of "/challenge/pwn": --x-w-rw-
```
- ran `chmod u=x,g=w,o=rw /challenge/pwn` in the terminal to set the permissions of the file `pwn` to `--x-w-rw-` and got the following output:  
```
You set the correct permissions!
Round 7 (of 8)!

Current permissions of "/challenge/pwn": --x-w-rw-
Needed permissions of "/challenge/pwn": -w------x
```
- ran `chmod u=w,g=-,o=x /challenge/pwn` in the terminal to set the permissions of the file `pwn` to `-w------x` and got the following output:  
```
You set the correct permissions!
You've solved all 8 rounds! I have changed the ownership of the /flag file so that you can 'chmod' it. You won't be able to read it until you make it readable with chmod!

Current permissions of "/flag": ---------
```
- ran `chmod a+r /flag` in the terminal to add read permissions for all users to the file `flag`
- ran `cat /flag` in the terminal to read the contents of the file and got the flag: `pwn.college{8QouXttsSGR7soaiVXUbUwvWNoq.dNTM5QDL5QTO0czW}`
## The SUID Bit
- ran `chmod u+s /challenge/getroot` in the terminal to set the SUID bit on the file `getroot`
- ran `/challenge/getroot` in the terminal to run the command and got the following output:  
```
SUCCESS! You have set the suid bit on this program, and it is running as root! 
Here is your shell...
root@permissions~the-suid-bit:~#
```
- ran `cat /flag` in the terminal to read the contents of the file and got the flag: `pwn.college{wSumhGRfCEMWRcJ-zHzdi_gxN-M.dNTM2QDL5QTO0czW}`