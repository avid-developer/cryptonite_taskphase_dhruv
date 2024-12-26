# not supported
## Description
Straightforward challenge, the flag is written on running notepad process. 
## Solution
- We're given [memdump.mem](./memdump.mem) file, which is a memory dump. I tried for some time to find the flag but kept running into dead ends. I glanced through an [online writeup](https://ashketchum.medium.com/blackhat-mea-ctf-2023-forensic-not-supported-595b5091b557) and realised that the challenge description is incomplete. The description also contains this: `Flag is direct without BHFlagY{} tag`.
- I ran `strings memdump.mem | grep -i "BHFlagY{"` to find the flag and got this: `BHflagY{d22a 3  e e  d 0  5 0  c 2  3 c  0 8  8 0  c c  9 1  2 3  6 8 9 0  5  c  9  d 2 5  2 7 a  4 1 c 3 2 8  f 8 1  e f  1 1  5 b  9  4 64 b  8 0  0f 7 42 5 33 3 edb7 1d5  7b4 40b  94 d c 7  6 6a 2d 4 9 61 1 d4  69 68 47  7b09dfa1  f246585d  8 7d 7b 5 a}`
- Removing the whitespaces and the `BHflagY{}` tag, we get the flag: `d22a3eed050c23c080cc912368905c9d2527a41c328f81ef115b9464b800f7425333edb71d57b440b94dc766a2d49611d46968477b09dfa1f246585d87d7b5a`.