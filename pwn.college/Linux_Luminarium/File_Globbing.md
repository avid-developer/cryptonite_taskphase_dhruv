# File Globbing
## Matching with *
- ran `cd /ch*` in the terminal to change the directory to `/challenge`
- ran `/challenge/run` in the terminal and got the flag
## Matching with ?
- ran `cd /?ha??enge` in the terminal to change the directory to `/challenge`
- ran `/challenge/run` in the terminal and got the flag
## Matching with []
- ran `cd /challenge/files` in the terminal to change the directory to `/challenge/files`
- ran `/challenge/run file_[bash]` in the terminal and got the flag
## Matching paths with []
- ran `/challenge/run /challenge/files/file_[bash]` in the terminal and got the flag
## Mixing globs
- ran `cd /challenge/files` in the terminal to change the directory to `/challenge/files`
- ran `ls` in the terminal to list all files in the directory:
```
amazing      educational  incredible  magical     queenly    uplifting   youthful
beautiful    fantastic    jovial      nice        radiant    victorious  zesty
challenging  great        kind        optimistic  splendid   wonderful
delightful   happy        laughing    pwning      thrilling  xenial
```
- i realised that `challenging`, `educational`, and `pwning` were the only files that began with the letters `c`, `e`, and `p` respectively
- ran `/challenge/run [cep]*` in the terminal and got the flag
## Exclusionary globbing
- ran `cd /challenge/files` in the terminal to change the directory to `/challenge/files`
- ran `/challenge/run [^pwn]*` in the terminal and got the flag