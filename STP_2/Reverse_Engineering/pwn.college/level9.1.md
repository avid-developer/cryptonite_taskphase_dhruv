# level9.1
## Description
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key. This challenge allows you to patch 5 bytes in the binary.
## Solution
- The executable program's name is `babyrev-level-9-1`
- I ran `objdump -d -M intel babyrev-level-9-1` to disassemble the binary and got the following:
```
babyrev-level-9-1:     file format elf64-x86-64


Disassembly of section .init:

0000000000001000 <.init>:
    1000:       f3 0f 1e fa             endbr64
    1004:       48 83 ec 08             sub    rsp,0x8
    1008:       48 8b 05 c9 3f 00 00    mov    rax,QWORD PTR [rip+0x3fc9]        # 4fd8 <open@plt+0x3d68>
    100f:       48 85 c0                test   rax,rax
    1012:       74 02                   je     1016 <__cxa_finalize@plt-0x13a>
    1014:       ff d0                   call   rax
    1016:       48 83 c4 08             add    rsp,0x8
    101a:       c3                      ret

Disassembly of section .plt:

0000000000001020 <.plt>:
    1020:       ff 35 12 3f 00 00       push   QWORD PTR [rip+0x3f12]        # 4f38 <open@plt+0x3cc8>
    1026:       f2 ff 25 13 3f 00 00    bnd jmp QWORD PTR [rip+0x3f13]        # 4f40 <open@plt+0x3cd0>
    102d:       0f 1f 00                nop    DWORD PTR [rax]
    1030:       f3 0f 1e fa             endbr64
    1034:       68 00 00 00 00          push   0x0
    1039:       f2 e9 e1 ff ff ff       bnd jmp 1020 <__cxa_finalize@plt-0x130>
    103f:       90                      nop
    1040:       f3 0f 1e fa             endbr64
    1044:       68 01 00 00 00          push   0x1
    1049:       f2 e9 d1 ff ff ff       bnd jmp 1020 <__cxa_finalize@plt-0x130>
    104f:       90                      nop
    1050:       f3 0f 1e fa             endbr64
    1054:       68 02 00 00 00          push   0x2
    1059:       f2 e9 c1 ff ff ff       bnd jmp 1020 <__cxa_finalize@plt-0x130>
    105f:       90                      nop
    1060:       f3 0f 1e fa             endbr64
    1064:       68 03 00 00 00          push   0x3
    1069:       f2 e9 b1 ff ff ff       bnd jmp 1020 <__cxa_finalize@plt-0x130>
    106f:       90                      nop
    1070:       f3 0f 1e fa             endbr64
    1074:       68 04 00 00 00          push   0x4
    1079:       f2 e9 a1 ff ff ff       bnd jmp 1020 <__cxa_finalize@plt-0x130>
    107f:       90                      nop
    1080:       f3 0f 1e fa             endbr64
    1084:       68 05 00 00 00          push   0x5
    1089:       f2 e9 91 ff ff ff       bnd jmp 1020 <__cxa_finalize@plt-0x130>
    108f:       90                      nop
    1090:       f3 0f 1e fa             endbr64
    1094:       68 06 00 00 00          push   0x6
    1099:       f2 e9 81 ff ff ff       bnd jmp 1020 <__cxa_finalize@plt-0x130>
    109f:       90                      nop
    10a0:       f3 0f 1e fa             endbr64
    10a4:       68 07 00 00 00          push   0x7
    10a9:       f2 e9 71 ff ff ff       bnd jmp 1020 <__cxa_finalize@plt-0x130>
    10af:       90                      nop
    10b0:       f3 0f 1e fa             endbr64
    10b4:       68 08 00 00 00          push   0x8
    10b9:       f2 e9 61 ff ff ff       bnd jmp 1020 <__cxa_finalize@plt-0x130>
    10bf:       90                      nop
    10c0:       f3 0f 1e fa             endbr64
    10c4:       68 09 00 00 00          push   0x9
    10c9:       f2 e9 51 ff ff ff       bnd jmp 1020 <__cxa_finalize@plt-0x130>
    10cf:       90                      nop
    10d0:       f3 0f 1e fa             endbr64
    10d4:       68 0a 00 00 00          push   0xa
    10d9:       f2 e9 41 ff ff ff       bnd jmp 1020 <__cxa_finalize@plt-0x130>
    10df:       90                      nop
    10e0:       f3 0f 1e fa             endbr64
    10e4:       68 0b 00 00 00          push   0xb
    10e9:       f2 e9 31 ff ff ff       bnd jmp 1020 <__cxa_finalize@plt-0x130>
    10ef:       90                      nop
    10f0:       f3 0f 1e fa             endbr64
    10f4:       68 0c 00 00 00          push   0xc
    10f9:       f2 e9 21 ff ff ff       bnd jmp 1020 <__cxa_finalize@plt-0x130>
    10ff:       90                      nop
    1100:       f3 0f 1e fa             endbr64
    1104:       68 0d 00 00 00          push   0xd
    1109:       f2 e9 11 ff ff ff       bnd jmp 1020 <__cxa_finalize@plt-0x130>
    110f:       90                      nop
    1110:       f3 0f 1e fa             endbr64
    1114:       68 0e 00 00 00          push   0xe
    1119:       f2 e9 01 ff ff ff       bnd jmp 1020 <__cxa_finalize@plt-0x130>
    111f:       90                      nop
    1120:       f3 0f 1e fa             endbr64
    1124:       68 0f 00 00 00          push   0xf
    1129:       f2 e9 f1 fe ff ff       bnd jmp 1020 <__cxa_finalize@plt-0x130>
    112f:       90                      nop
    1130:       f3 0f 1e fa             endbr64
    1134:       68 10 00 00 00          push   0x10
    1139:       f2 e9 e1 fe ff ff       bnd jmp 1020 <__cxa_finalize@plt-0x130>
    113f:       90                      nop
    1140:       f3 0f 1e fa             endbr64
    1144:       68 11 00 00 00          push   0x11
    1149:       f2 e9 d1 fe ff ff       bnd jmp 1020 <__cxa_finalize@plt-0x130>
    114f:       90                      nop

Disassembly of section .plt.got:

0000000000001150 <__cxa_finalize@plt>:
    1150:       f3 0f 1e fa             endbr64
    1154:       f2 ff 25 9d 3e 00 00    bnd jmp QWORD PTR [rip+0x3e9d]        # 4ff8 <open@plt+0x3d88>
    115b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

Disassembly of section .plt.sec:

0000000000001160 <mprotect@plt>:
    1160:       f3 0f 1e fa             endbr64
    1164:       f2 ff 25 dd 3d 00 00    bnd jmp QWORD PTR [rip+0x3ddd]        # 4f48 <open@plt+0x3cd8>
    116b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001170 <printf@plt>:
    1170:       f3 0f 1e fa             endbr64
    1174:       f2 ff 25 d5 3d 00 00    bnd jmp QWORD PTR [rip+0x3dd5]        # 4f50 <open@plt+0x3ce0>
    117b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001180 <memset@plt>:
    1180:       f3 0f 1e fa             endbr64
    1184:       f2 ff 25 cd 3d 00 00    bnd jmp QWORD PTR [rip+0x3dcd]        # 4f58 <open@plt+0x3ce8>
    118b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001190 <puts@plt>:
    1190:       f3 0f 1e fa             endbr64
    1194:       f2 ff 25 c5 3d 00 00    bnd jmp QWORD PTR [rip+0x3dc5]        # 4f60 <open@plt+0x3cf0>
    119b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

00000000000011a0 <exit@plt>:
    11a0:       f3 0f 1e fa             endbr64
    11a4:       f2 ff 25 bd 3d 00 00    bnd jmp QWORD PTR [rip+0x3dbd]        # 4f68 <open@plt+0x3cf8>
    11ab:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

00000000000011b0 <setvbuf@plt>:
    11b0:       f3 0f 1e fa             endbr64
    11b4:       f2 ff 25 b5 3d 00 00    bnd jmp QWORD PTR [rip+0x3db5]        # 4f70 <open@plt+0x3d00>
    11bb:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

00000000000011c0 <putchar@plt>:
    11c0:       f3 0f 1e fa             endbr64
    11c4:       f2 ff 25 ad 3d 00 00    bnd jmp QWORD PTR [rip+0x3dad]        # 4f78 <open@plt+0x3d08>
    11cb:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

00000000000011d0 <read@plt>:
    11d0:       f3 0f 1e fa             endbr64
    11d4:       f2 ff 25 a5 3d 00 00    bnd jmp QWORD PTR [rip+0x3da5]        # 4f80 <open@plt+0x3d10>
    11db:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

00000000000011e0 <geteuid@plt>:
    11e0:       f3 0f 1e fa             endbr64
    11e4:       f2 ff 25 9d 3d 00 00    bnd jmp QWORD PTR [rip+0x3d9d]        # 4f88 <open@plt+0x3d18>
    11eb:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

00000000000011f0 <MD5_Final@plt>:
    11f0:       f3 0f 1e fa             endbr64
    11f4:       f2 ff 25 95 3d 00 00    bnd jmp QWORD PTR [rip+0x3d95]        # 4f90 <open@plt+0x3d20>
    11fb:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001200 <MD5_Update@plt>:
    1200:       f3 0f 1e fa             endbr64
    1204:       f2 ff 25 8d 3d 00 00    bnd jmp QWORD PTR [rip+0x3d8d]        # 4f98 <open@plt+0x3d28>
    120b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001210 <strerror@plt>:
    1210:       f3 0f 1e fa             endbr64
    1214:       f2 ff 25 85 3d 00 00    bnd jmp QWORD PTR [rip+0x3d85]        # 4fa0 <open@plt+0x3d30>
    121b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001220 <__errno_location@plt>:
    1220:       f3 0f 1e fa             endbr64
    1224:       f2 ff 25 7d 3d 00 00    bnd jmp QWORD PTR [rip+0x3d7d]        # 4fa8 <open@plt+0x3d38>
    122b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001230 <MD5_Init@plt>:
    1230:       f3 0f 1e fa             endbr64
    1234:       f2 ff 25 75 3d 00 00    bnd jmp QWORD PTR [rip+0x3d75]        # 4fb0 <open@plt+0x3d40>
    123b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001240 <__isoc99_scanf@plt>:
    1240:       f3 0f 1e fa             endbr64
    1244:       f2 ff 25 6d 3d 00 00    bnd jmp QWORD PTR [rip+0x3d6d]        # 4fb8 <open@plt+0x3d48>
    124b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001250 <memcmp@plt>:
    1250:       f3 0f 1e fa             endbr64
    1254:       f2 ff 25 65 3d 00 00    bnd jmp QWORD PTR [rip+0x3d65]        # 4fc0 <open@plt+0x3d50>
    125b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001260 <write@plt>:
    1260:       f3 0f 1e fa             endbr64
    1264:       f2 ff 25 5d 3d 00 00    bnd jmp QWORD PTR [rip+0x3d5d]        # 4fc8 <open@plt+0x3d58>
    126b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001270 <open@plt>:
    1270:       f3 0f 1e fa             endbr64
    1274:       f2 ff 25 55 3d 00 00    bnd jmp QWORD PTR [rip+0x3d55]        # 4fd0 <open@plt+0x3d60>
    127b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

Disassembly of section .text:

0000000000001280 <.text>:
    1280:       f3 0f 1e fa             endbr64
    1284:       31 ed                   xor    ebp,ebp
    1286:       49 89 d1                mov    r9,rdx
    1289:       5e                      pop    rsi
    128a:       48 89 e2                mov    rdx,rsp
    128d:       48 83 e4 f0             and    rsp,0xfffffffffffffff0
    1291:       50                      push   rax
    1292:       54                      push   rsp
    1293:       4c 8d 05 e6 0d 00 00    lea    r8,[rip+0xde6]        # 2080 <open@plt+0xe10>
    129a:       48 8d 0d 6f 0d 00 00    lea    rcx,[rip+0xd6f]        # 2010 <open@plt+0xda0>
    12a1:       48 8d 3d 35 0a 00 00    lea    rdi,[rip+0xa35]        # 1cdd <open@plt+0xa6d>
    12a8:       ff 15 32 3d 00 00       call   QWORD PTR [rip+0x3d32]        # 4fe0 <open@plt+0x3d70>
    12ae:       f4                      hlt
    12af:       90                      nop
    12b0:       48 8d 3d 71 3d 00 00    lea    rdi,[rip+0x3d71]        # 5028 <open@plt+0x3db8>
    12b7:       48 8d 05 6a 3d 00 00    lea    rax,[rip+0x3d6a]        # 5028 <open@plt+0x3db8>
    12be:       48 39 f8                cmp    rax,rdi
    12c1:       74 15                   je     12d8 <open@plt+0x68>
    12c3:       48 8b 05 1e 3d 00 00    mov    rax,QWORD PTR [rip+0x3d1e]        # 4fe8 <open@plt+0x3d78>
    12ca:       48 85 c0                test   rax,rax
    12cd:       74 09                   je     12d8 <open@plt+0x68>
    12cf:       ff e0                   jmp    rax
    12d1:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]
    12d8:       c3                      ret
    12d9:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]
    12e0:       48 8d 3d 41 3d 00 00    lea    rdi,[rip+0x3d41]        # 5028 <open@plt+0x3db8>
    12e7:       48 8d 35 3a 3d 00 00    lea    rsi,[rip+0x3d3a]        # 5028 <open@plt+0x3db8>
    12ee:       48 29 fe                sub    rsi,rdi
    12f1:       48 89 f0                mov    rax,rsi
    12f4:       48 c1 ee 3f             shr    rsi,0x3f
    12f8:       48 c1 f8 03             sar    rax,0x3
    12fc:       48 01 c6                add    rsi,rax
    12ff:       48 d1 fe                sar    rsi,1
    1302:       74 14                   je     1318 <open@plt+0xa8>
    1304:       48 8b 05 e5 3c 00 00    mov    rax,QWORD PTR [rip+0x3ce5]        # 4ff0 <open@plt+0x3d80>
    130b:       48 85 c0                test   rax,rax
    130e:       74 08                   je     1318 <open@plt+0xa8>
    1310:       ff e0                   jmp    rax
    1312:       66 0f 1f 44 00 00       nop    WORD PTR [rax+rax*1+0x0]
    1318:       c3                      ret
    1319:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]
    1320:       f3 0f 1e fa             endbr64
    1324:       80 3d 25 3d 00 00 00    cmp    BYTE PTR [rip+0x3d25],0x0        # 5050 <stdout@GLIBC_2.2.5+0x8>
    132b:       75 2b                   jne    1358 <open@plt+0xe8>
    132d:       55                      push   rbp
    132e:       48 83 3d c2 3c 00 00    cmp    QWORD PTR [rip+0x3cc2],0x0        # 4ff8 <open@plt+0x3d88>
    1335:       00 
    1336:       48 89 e5                mov    rbp,rsp
    1339:       74 0c                   je     1347 <open@plt+0xd7>
    133b:       48 8b 3d c6 3c 00 00    mov    rdi,QWORD PTR [rip+0x3cc6]        # 5008 <open@plt+0x3d98>
    1342:       e8 09 fe ff ff          call   1150 <__cxa_finalize@plt>
    1347:       e8 64 ff ff ff          call   12b0 <open@plt+0x40>
    134c:       c6 05 fd 3c 00 00 01    mov    BYTE PTR [rip+0x3cfd],0x1        # 5050 <stdout@GLIBC_2.2.5+0x8>
    1353:       5d                      pop    rbp
    1354:       c3                      ret
    1355:       0f 1f 00                nop    DWORD PTR [rax]
    1358:       c3                      ret
    1359:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]
    1360:       f3 0f 1e fa             endbr64
    1364:       e9 77 ff ff ff          jmp    12e0 <open@plt+0x70>
    1369:       f3 0f 1e fa             endbr64
    136d:       55                      push   rbp
    136e:       48 89 e5                mov    rbp,rsp
    1371:       90                      nop
    1372:       90                      nop
... (more nop instructions)
    1bd2:       90                      nop
    1bd3:       90                      nop
    1bd4:       5d                      pop    rbp
    1bd5:       c3                      ret
    1bd6:       f3 0f 1e fa             endbr64
    1bda:       55                      push   rbp
    1bdb:       48 89 e5                mov    rbp,rsp
    1bde:       48 8d 3d 23 14 00 00    lea    rdi,[rip+0x1423]        # 3008 <open@plt+0x1d98>
    1be5:       e8 a6 f5 ff ff          call   1190 <puts@plt>
    1bea:       be 00 00 00 00          mov    esi,0x0
    1bef:       48 8d 3d 2e 14 00 00    lea    rdi,[rip+0x142e]        # 3024 <open@plt+0x1db4>
    1bf6:       b8 00 00 00 00          mov    eax,0x0
    1bfb:       e8 70 f6 ff ff          call   1270 <open@plt>
    1c00:       89 05 5a 34 00 00       mov    DWORD PTR [rip+0x345a],eax        # 5060 <stdout@GLIBC_2.2.5+0x18>
    1c06:       8b 05 54 34 00 00       mov    eax,DWORD PTR [rip+0x3454]        # 5060 <stdout@GLIBC_2.2.5+0x18>
    1c0c:       85 c0                   test   eax,eax
    1c0e:       79 4d                   jns    1c5d <open@plt+0x9ed>
    1c10:       e8 0b f6 ff ff          call   1220 <__errno_location@plt>
    1c15:       8b 00                   mov    eax,DWORD PTR [rax]
    1c17:       89 c7                   mov    edi,eax
    1c19:       e8 f2 f5 ff ff          call   1210 <strerror@plt>
    1c1e:       48 89 c6                mov    rsi,rax
    1c21:       48 8d 3d 08 14 00 00    lea    rdi,[rip+0x1408]        # 3030 <open@plt+0x1dc0>
    1c28:       b8 00 00 00 00          mov    eax,0x0
    1c2d:       e8 3e f5 ff ff          call   1170 <printf@plt>
    1c32:       e8 a9 f5 ff ff          call   11e0 <geteuid@plt>
    1c37:       85 c0                   test   eax,eax
    1c39:       74 18                   je     1c53 <open@plt+0x9e3>
    1c3b:       48 8d 3d 1e 14 00 00    lea    rdi,[rip+0x141e]        # 3060 <open@plt+0x1df0>
    1c42:       e8 49 f5 ff ff          call   1190 <puts@plt>
    1c47:       48 8d 3d 3a 14 00 00    lea    rdi,[rip+0x143a]        # 3088 <open@plt+0x1e18>
    1c4e:       e8 3d f5 ff ff          call   1190 <puts@plt>
    1c53:       bf ff ff ff ff          mov    edi,0xffffffff
    1c58:       e8 43 f5 ff ff          call   11a0 <exit@plt>
    1c5d:       8b 05 fd 33 00 00       mov    eax,DWORD PTR [rip+0x33fd]        # 5060 <stdout@GLIBC_2.2.5+0x18>
    1c63:       ba 00 01 00 00          mov    edx,0x100
    1c68:       48 8d 35 11 34 00 00    lea    rsi,[rip+0x3411]        # 5080 <stdout@GLIBC_2.2.5+0x38>
    1c6f:       89 c7                   mov    edi,eax
    1c71:       e8 5a f5 ff ff          call   11d0 <read@plt>
    1c76:       89 05 04 35 00 00       mov    DWORD PTR [rip+0x3504],eax        # 5180 <stdout@GLIBC_2.2.5+0x138>
    1c7c:       8b 05 fe 34 00 00       mov    eax,DWORD PTR [rip+0x34fe]        # 5180 <stdout@GLIBC_2.2.5+0x138>
    1c82:       85 c0                   test   eax,eax
    1c84:       7f 2c                   jg     1cb2 <open@plt+0xa42>
    1c86:       e8 95 f5 ff ff          call   1220 <__errno_location@plt>
    1c8b:       8b 00                   mov    eax,DWORD PTR [rax]
    1c8d:       89 c7                   mov    edi,eax
    1c8f:       e8 7c f5 ff ff          call   1210 <strerror@plt>
    1c94:       48 89 c6                mov    rsi,rax
    1c97:       48 8d 3d 42 14 00 00    lea    rdi,[rip+0x1442]        # 30e0 <open@plt+0x1e70>
    1c9e:       b8 00 00 00 00          mov    eax,0x0
    1ca3:       e8 c8 f4 ff ff          call   1170 <printf@plt>
    1ca8:       bf ff ff ff ff          mov    edi,0xffffffff
    1cad:       e8 ee f4 ff ff          call   11a0 <exit@plt>
    1cb2:       8b 05 c8 34 00 00       mov    eax,DWORD PTR [rip+0x34c8]        # 5180 <stdout@GLIBC_2.2.5+0x138>
    1cb8:       48 98                   cdqe
    1cba:       48 89 c2                mov    rdx,rax
    1cbd:       48 8d 35 bc 33 00 00    lea    rsi,[rip+0x33bc]        # 5080 <stdout@GLIBC_2.2.5+0x38>
    1cc4:       bf 01 00 00 00          mov    edi,0x1
    1cc9:       e8 92 f5 ff ff          call   1260 <write@plt>
    1cce:       48 8d 3d 35 14 00 00    lea    rdi,[rip+0x1435]        # 310a <open@plt+0x1e9a>
    1cd5:       e8 b6 f4 ff ff          call   1190 <puts@plt>
    1cda:       90                      nop
    1cdb:       5d                      pop    rbp
    1cdc:       c3                      ret
    1cdd:       f3 0f 1e fa             endbr64
    1ce1:       55                      push   rbp
    1ce2:       48 89 e5                mov    rbp,rsp
    1ce5:       48 81 ec e0 00 00 00    sub    rsp,0xe0
    1cec:       89 bd 3c ff ff ff       mov    DWORD PTR [rbp-0xc4],edi
    1cf2:       48 89 b5 30 ff ff ff    mov    QWORD PTR [rbp-0xd0],rsi
    1cf9:       48 89 95 28 ff ff ff    mov    QWORD PTR [rbp-0xd8],rdx
    1d00:       64 48 8b 04 25 28 00    mov    rax,QWORD PTR fs:0x28
    1d07:       00 00 
    1d09:       48 89 45 f8             mov    QWORD PTR [rbp-0x8],rax
    1d0d:       31 c0                   xor    eax,eax
    1d0f:       48 8b 05 2a 33 00 00    mov    rax,QWORD PTR [rip+0x332a]        # 5040 <stdin@GLIBC_2.2.5>
    1d16:       b9 00 00 00 00          mov    ecx,0x0
    1d1b:       ba 02 00 00 00          mov    edx,0x2
    1d20:       be 00 00 00 00          mov    esi,0x0
    1d25:       48 89 c7                mov    rdi,rax
    1d28:       e8 83 f4 ff ff          call   11b0 <setvbuf@plt>
    1d2d:       48 8b 05 14 33 00 00    mov    rax,QWORD PTR [rip+0x3314]        # 5048 <stdout@GLIBC_2.2.5>
    1d34:       b9 00 00 00 00          mov    ecx,0x0
    1d39:       ba 02 00 00 00          mov    edx,0x2
    1d3e:       be 00 00 00 00          mov    esi,0x0
    1d43:       48 89 c7                mov    rdi,rax
    1d46:       e8 65 f4 ff ff          call   11b0 <setvbuf@plt>
    1d4b:       48 8d 3d ba 13 00 00    lea    rdi,[rip+0x13ba]        # 310c <open@plt+0x1e9c>
    1d52:       e8 39 f4 ff ff          call   1190 <puts@plt>
    1d57:       48 8b 85 30 ff ff ff    mov    rax,QWORD PTR [rbp-0xd0]
    1d5e:       48 8b 00                mov    rax,QWORD PTR [rax]
    1d61:       48 89 c6                mov    rsi,rax
    1d64:       48 8d 3d a5 13 00 00    lea    rdi,[rip+0x13a5]        # 3110 <open@plt+0x1ea0>
    1d6b:       b8 00 00 00 00          mov    eax,0x0
    1d70:       e8 fb f3 ff ff          call   1170 <printf@plt>
    1d75:       48 8d 3d 90 13 00 00    lea    rdi,[rip+0x1390]        # 310c <open@plt+0x1e9c>
    1d7c:       e8 0f f4 ff ff          call   1190 <puts@plt>
    1d81:       bf 0a 00 00 00          mov    edi,0xa
    1d86:       e8 35 f4 ff ff          call   11c0 <putchar@plt>
    1d8b:       48 8d 3d 96 13 00 00    lea    rdi,[rip+0x1396]        # 3128 <open@plt+0x1eb8>
    1d92:       e8 f9 f3 ff ff          call   1190 <puts@plt>
    1d97:       48 8d 3d 02 14 00 00    lea    rdi,[rip+0x1402]        # 31a0 <open@plt+0x1f30>
    1d9e:       e8 ed f3 ff ff          call   1190 <puts@plt>
    1da3:       48 8d 3d 6e 14 00 00    lea    rdi,[rip+0x146e]        # 3218 <open@plt+0x1fa8>
    1daa:       e8 e1 f3 ff ff          call   1190 <puts@plt>
    1daf:       48 8d 3d da 14 00 00    lea    rdi,[rip+0x14da]        # 3290 <open@plt+0x2020>
    1db6:       e8 d5 f3 ff ff          call   1190 <puts@plt>
    1dbb:       48 8d 3d 0e 15 00 00    lea    rdi,[rip+0x150e]        # 32d0 <open@plt+0x2060>
    1dc2:       e8 c9 f3 ff ff          call   1190 <puts@plt>
    1dc7:       c7 85 50 ff ff ff 00    mov    DWORD PTR [rbp-0xb0],0x0
    1dce:       00 00 00 
    1dd1:       48 8d 05 91 f5 ff ff    lea    rax,[rip+0xfffffffffffff591]        # 1369 <open@plt+0xf9>
    1dd8:       48 25 00 f0 ff ff       and    rax,0xfffffffffffff000
    1dde:       48 2d 00 10 00 00       sub    rax,0x1000
    1de4:       48 89 85 58 ff ff ff    mov    QWORD PTR [rbp-0xa8],rax
    1deb:       90                      nop
    1dec:       8b 85 50 ff ff ff       mov    eax,DWORD PTR [rbp-0xb0]
    1df2:       8d 50 01                lea    edx,[rax+0x1]
    1df5:       89 95 50 ff ff ff       mov    DWORD PTR [rbp-0xb0],edx
    1dfb:       c1 e0 0c                shl    eax,0xc
    1dfe:       48 63 d0                movsxd rdx,eax
    1e01:       48 8b 85 58 ff ff ff    mov    rax,QWORD PTR [rbp-0xa8]
    1e08:       48 01 d0                add    rax,rdx
    1e0b:       ba 07 00 00 00          mov    edx,0x7
    1e10:       be 00 10 00 00          mov    esi,0x1000
    1e15:       48 89 c7                mov    rdi,rax
    1e18:       e8 43 f3 ff ff          call   1160 <mprotect@plt>
    1e1d:       85 c0                   test   eax,eax
    1e1f:       74 cb                   je     1dec <open@plt+0xb7c>
    1e21:       c7 85 54 ff ff ff 00    mov    DWORD PTR [rbp-0xac],0x0
    1e28:       00 00 00 
    1e2b:       e9 ce 00 00 00          jmp    1efe <open@plt+0xc8e>
    1e30:       8b 85 54 ff ff ff       mov    eax,DWORD PTR [rbp-0xac]
    1e36:       83 c0 01                add    eax,0x1
    1e39:       89 c6                   mov    esi,eax
    1e3b:       48 8d 3d ed 14 00 00    lea    rdi,[rip+0x14ed]        # 332f <open@plt+0x20bf>
    1e42:       b8 00 00 00 00          mov    eax,0x0
    1e47:       e8 24 f3 ff ff          call   1170 <printf@plt>
    1e4c:       48 8d 3d f1 14 00 00    lea    rdi,[rip+0x14f1]        # 3344 <open@plt+0x20d4>
    1e53:       b8 00 00 00 00          mov    eax,0x0
    1e58:       e8 13 f3 ff ff          call   1170 <printf@plt>
    1e5d:       48 8d 85 4e ff ff ff    lea    rax,[rbp-0xb2]
    1e64:       48 89 c6                mov    rsi,rax
    1e67:       48 8d 3d ef 14 00 00    lea    rdi,[rip+0x14ef]        # 335d <open@plt+0x20ed>
    1e6e:       b8 00 00 00 00          mov    eax,0x0
    1e73:       e8 c8 f3 ff ff          call   1240 <__isoc99_scanf@plt>
    1e78:       48 8d 3d e2 14 00 00    lea    rdi,[rip+0x14e2]        # 3361 <open@plt+0x20f1>
    1e7f:       b8 00 00 00 00          mov    eax,0x0
    1e84:       e8 e7 f2 ff ff          call   1170 <printf@plt>
    1e89:       48 8d 85 4d ff ff ff    lea    rax,[rbp-0xb3]
    1e90:       48 89 c6                mov    rsi,rax
    1e93:       48 8d 3d d9 14 00 00    lea    rdi,[rip+0x14d9]        # 3373 <open@plt+0x2103>
    1e9a:       b8 00 00 00 00          mov    eax,0x0
    1e9f:       e8 9c f3 ff ff          call   1240 <__isoc99_scanf@plt>
    1ea4:       0f b6 8d 4d ff ff ff    movzx  ecx,BYTE PTR [rbp-0xb3]
    1eab:       0f b7 85 4e ff ff ff    movzx  eax,WORD PTR [rbp-0xb2]
    1eb2:       0f b7 d0                movzx  edx,ax
    1eb5:       48 8b 85 58 ff ff ff    mov    rax,QWORD PTR [rbp-0xa8]
    1ebc:       48 01 d0                add    rax,rdx
    1ebf:       89 ca                   mov    edx,ecx
    1ec1:       88 10                   mov    BYTE PTR [rax],dl
    1ec3:       0f b6 85 4d ff ff ff    movzx  eax,BYTE PTR [rbp-0xb3]
    1eca:       0f b6 c0                movzx  eax,al
    1ecd:       0f b7 95 4e ff ff ff    movzx  edx,WORD PTR [rbp-0xb2]
    1ed4:       0f b7 ca                movzx  ecx,dx
    1ed7:       48 8b 95 58 ff ff ff    mov    rdx,QWORD PTR [rbp-0xa8]
    1ede:       48 01 d1                add    rcx,rdx
    1ee1:       89 c2                   mov    edx,eax
    1ee3:       48 89 ce                mov    rsi,rcx
    1ee6:       48 8d 3d 8b 14 00 00    lea    rdi,[rip+0x148b]        # 3378 <open@plt+0x2108>
    1eed:       b8 00 00 00 00          mov    eax,0x0
    1ef2:       e8 79 f2 ff ff          call   1170 <printf@plt>
    1ef7:       83 85 54 ff ff ff 01    add    DWORD PTR [rbp-0xac],0x1
    1efe:       83 bd 54 ff ff ff 04    cmp    DWORD PTR [rbp-0xac],0x4
    1f05:       0f 8e 25 ff ff ff       jle    1e30 <open@plt+0xbc0>
    1f0b:       48 c7 45 d0 00 00 00    mov    QWORD PTR [rbp-0x30],0x0
    1f12:       00 
    1f13:       48 c7 45 d8 00 00 00    mov    QWORD PTR [rbp-0x28],0x0
    1f1a:       00 
    1f1b:       48 c7 45 e0 00 00 00    mov    QWORD PTR [rbp-0x20],0x0
    1f22:       00 
    1f23:       c7 45 e8 00 00 00 00    mov    DWORD PTR [rbp-0x18],0x0
    1f2a:       48 8d 3d 6f 14 00 00    lea    rdi,[rip+0x146f]        # 33a0 <open@plt+0x2130>
    1f31:       e8 5a f2 ff ff          call   1190 <puts@plt>
    1f36:       48 8d 45 d0             lea    rax,[rbp-0x30]
    1f3a:       ba 1b 00 00 00          mov    edx,0x1b
    1f3f:       48 89 c6                mov    rsi,rax
    1f42:       bf 00 00 00 00          mov    edi,0x0
    1f47:       e8 84 f2 ff ff          call   11d0 <read@plt>
    1f4c:       48 8d 85 60 ff ff ff    lea    rax,[rbp-0xa0]
    1f53:       48 89 c7                mov    rdi,rax
    1f56:       e8 d5 f2 ff ff          call   1230 <MD5_Init@plt>
    1f5b:       48 8d 4d d0             lea    rcx,[rbp-0x30]
    1f5f:       48 8d 85 60 ff ff ff    lea    rax,[rbp-0xa0]
    1f66:       ba 1b 00 00 00          mov    edx,0x1b
    1f6b:       48 89 ce                mov    rsi,rcx
    1f6e:       48 89 c7                mov    rdi,rax
    1f71:       e8 8a f2 ff ff          call   1200 <MD5_Update@plt>
    1f76:       48 8d 95 60 ff ff ff    lea    rdx,[rbp-0xa0]
    1f7d:       48 8d 45 c0             lea    rax,[rbp-0x40]
    1f81:       48 89 d6                mov    rsi,rdx
    1f84:       48 89 c7                mov    rdi,rax
    1f87:       e8 64 f2 ff ff          call   11f0 <MD5_Final@plt>
    1f8c:       48 8d 45 d0             lea    rax,[rbp-0x30]
    1f90:       ba 1b 00 00 00          mov    edx,0x1b
    1f95:       be 00 00 00 00          mov    esi,0x0
    1f9a:       48 89 c7                mov    rdi,rax
    1f9d:       e8 de f1 ff ff          call   1180 <memset@plt>
    1fa2:       48 8b 45 c0             mov    rax,QWORD PTR [rbp-0x40]
    1fa6:       48 8b 55 c8             mov    rdx,QWORD PTR [rbp-0x38]
    1faa:       48 89 45 d0             mov    QWORD PTR [rbp-0x30],rax
    1fae:       48 89 55 d8             mov    QWORD PTR [rbp-0x28],rdx
    1fb2:       48 8d 3d 0f 14 00 00    lea    rdi,[rip+0x140f]        # 33c8 <open@plt+0x2158>
    1fb9:       e8 d2 f1 ff ff          call   1190 <puts@plt>
    1fbe:       48 8d 45 d0             lea    rax,[rbp-0x30]
    1fc2:       ba 1b 00 00 00          mov    edx,0x1b
    1fc7:       48 8d 35 42 30 00 00    lea    rsi,[rip+0x3042]        # 5010 <open@plt+0x3da0>
    1fce:       48 89 c7                mov    rdi,rax
    1fd1:       e8 7a f2 ff ff          call   1250 <memcmp@plt>
    1fd6:       85 c0                   test   eax,eax
    1fd8:       75 14                   jne    1fee <open@plt+0xd7e>
    1fda:       b8 00 00 00 00          mov    eax,0x0
    1fdf:       e8 f2 fb ff ff          call   1bd6 <open@plt+0x966>
    1fe4:       bf 00 00 00 00          mov    edi,0x0
    1fe9:       e8 b2 f1 ff ff          call   11a0 <exit@plt>
    1fee:       48 8d 3d f7 13 00 00    lea    rdi,[rip+0x13f7]        # 33ec <open@plt+0x217c>
    1ff5:       e8 96 f1 ff ff          call   1190 <puts@plt>
    1ffa:       bf 01 00 00 00          mov    edi,0x1
    1fff:       e8 9c f1 ff ff          call   11a0 <exit@plt>
    2004:       66 2e 0f 1f 84 00 00    cs nop WORD PTR [rax+rax*1+0x0]
    200b:       00 00 00 
    200e:       66 90                   xchg   ax,ax
    2010:       f3 0f 1e fa             endbr64
    2014:       41 57                   push   r15
    2016:       4c 8d 3d 03 2d 00 00    lea    r15,[rip+0x2d03]        # 4d20 <open@plt+0x3ab0>
    201d:       41 56                   push   r14
    201f:       49 89 d6                mov    r14,rdx
    2022:       41 55                   push   r13
    2024:       49 89 f5                mov    r13,rsi
    2027:       41 54                   push   r12
    2029:       41 89 fc                mov    r12d,edi
    202c:       55                      push   rbp
    202d:       48 8d 2d f4 2c 00 00    lea    rbp,[rip+0x2cf4]        # 4d28 <open@plt+0x3ab8>
    2034:       53                      push   rbx
    2035:       4c 29 fd                sub    rbp,r15
    2038:       48 83 ec 08             sub    rsp,0x8
    203c:       e8 bf ef ff ff          call   1000 <__cxa_finalize@plt-0x150>
    2041:       48 c1 fd 03             sar    rbp,0x3
    2045:       74 1f                   je     2066 <open@plt+0xdf6>
    2047:       31 db                   xor    ebx,ebx
    2049:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]
    2050:       4c 89 f2                mov    rdx,r14
    2053:       4c 89 ee                mov    rsi,r13
    2056:       44 89 e7                mov    edi,r12d
    2059:       41 ff 14 df             call   QWORD PTR [r15+rbx*8]
    205d:       48 83 c3 01             add    rbx,0x1
    2061:       48 39 dd                cmp    rbp,rbx
    2064:       75 ea                   jne    2050 <open@plt+0xde0>
    2066:       48 83 c4 08             add    rsp,0x8
    206a:       5b                      pop    rbx
    206b:       5d                      pop    rbp
    206c:       41 5c                   pop    r12
    206e:       41 5d                   pop    r13
    2070:       41 5e                   pop    r14
    2072:       41 5f                   pop    r15
    2074:       c3                      ret
    2075:       66 66 2e 0f 1f 84 00    data16 cs nop WORD PTR [rax+rax*1+0x0]
    207c:       00 00 00 00 
    2080:       f3 0f 1e fa             endbr64
    2084:       c3                      ret

Disassembly of section .fini:

0000000000002088 <.fini>:
    2088:       f3 0f 1e fa             endbr64
    208c:       48 83 ec 08             sub    rsp,0x8
    2090:       48 83 c4 08             add    rsp,0x8
    2094:       c3                      ret
```
- Similar to [level9.0](./level9.0.md), we can bypass the `jne` instruction by replacing the instruction with `nop`'s opcode `0x90`.
- `1fd8:       75 14                   jne    1fee <open@plt+0xd7e>`, So we can replace the hex value at addresses `1fd8` and `1fd9` with `0x90`.
- Ran the program and patched it:
```
###
### Welcome to ./babyrev-level-9-1!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Unfortunately for you, the license key cannot be reversed. You'll have to crack this program.

Changing byte 1/5.
Offset (hex) to change: 1fd8
New value (hex): 90
The byte has been changed: *0x62a8f5160fd8 = 90.
Changing byte 2/5.
Offset (hex) to change: 1fd9
New value (hex): 90
The byte has been changed: *0x62a8f5160fd9 = 90.
Changing byte 3/5.
Offset (hex) to change: .
New value (hex): The byte has been changed: *0x62a8f5160fd9 = 90.
Changing byte 4/5.
Offset (hex) to change: New value (hex): The byte has been changed: *0x62a8f5160fd9 = 90.
Changing byte 5/5.
Offset (hex) to change: New value (hex): The byte has been changed: *0x62a8f5160fd9 = 90.
Ready to receive your license key!

Checking the received license key!

You win! Here is your flag:
pwn.college{4NEKs4xXp8suFsf0aYuLVG51see.0FO2IDL5QTO0czW}
```
- Flag: `pwn.college{4NEKs4xXp8suFsf0aYuLVG51see.0FO2IDL5QTO0czW}`