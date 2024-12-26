# Access Granted
## Description
First things first. MogamBro is so dumb that he might be using the same set of passwords everywhere, so lets try cracking his PC's password for some luck.
## Solution
- Unzipped the `tar.gz` file and got [mogambro](./mogambro/) directory.
- In it, there are 3 files:
  - [artifacts.ad1](./mogambro/artifacts.ad1)
  - [memdump.mem](./mogambro/memdump.mem)
  - [trace.pcap](./mogambro/trace.pcap)
- I had no idea what these files were and what to do with them, so this involved a lot of Googling and looking up the file extensions.
- I learnt that `ad1` is a disk image file, `mem` is a memory dump file, and `pcap` is a packet capture file.
- Since `mem` is a snapshot of the RAM, it contains running processes, passwords etc. So, I decided to start with this file.
- I got to know about a tool called `volatility` which is used to analyze memory dumps. So I installed this tool using `pip3 install volatility3`.
- Ran `vol -f mogambro/memdump.mem windows.info` to get the basic system information:
```
Variable        Value

Kernel Base     0xf80611800000
DTB     0x1aa000
Symbols file:///Users/Dhruv1/Library/Python/3.12/lib/python/site-packages/volatility3/symbols/windows/ntkrnlmp.pdb/D9424FC4861E47C10FAD1B35DEC6DCC8-1.json.xz
Is64Bit True
IsPAE   False
layer_name      0 WindowsIntel32e
memory_layer    1 FileLayer
KdVersionBlock  0xf8061240f400
Major/Minor     15.19041
MachineType     34404
KeNumberProcessors      4
SystemTime      2024-02-15 16:37:18+00:00
NtSystemRoot    C:\Windows
NtProductType   NtProductWinNt
NtMajorVersion  10
NtMinorVersion  0
PE MajorOperatingSystemVersion  10
PE MinorOperatingSystemVersion  0
PE Machine      34404
PE TimeDateStamp        Mon Dec  9 11:07:51 2019
```
- This means that we're working with a Windows 10 64bit system.
- Since the challenge's description clearly suggests that we need to crack the password, I looked up how to do that using `volatility`. I found that by using `vol -f mogambro/memdump.mem windows.hashdump`, we can get the password hashes stored in the memory dump.
- Running the command, I got:
```
User    rid     lmhash  nthash

Administrator   500     aad3b435b51404eeaad3b435b51404ee        8a320467c7c22e321c3173e757194bb3
Guest   501     aad3b435b51404eeaad3b435b51404ee        31d6cfe0d16ae931b73c59d7e0c089c0
DefaultAccount  503     aad3b435b51404eeaad3b435b51404ee        31d6cfe0d16ae931b73c59d7e0c089c0
WDAGUtilityAccount      504     aad3b435b51404eeaad3b435b51404ee        74d0db3c3f38778476a44ff9ce0aefe2
MogamBro        1000    aad3b435b51404eeaad3b435b51404ee        8a320467c7c22e321c3173e757194bb3
```
- We have the NT Hash of the `MogamBro` user: `8a320467c7c22e321c3173e757194bb3`. I looked up how to crack this hash and learnt about the tool [CrackStation](https://crackstation.net/).
- I entered the hash on the site and got the password: `adolfhitlerrulesallthepeople`.
- So the flag is probably `BITSCTF{adolfhitlerrulesallthepeople}` or something similar.
- As the challenge description suggests, the same password may be used in the later challenges.