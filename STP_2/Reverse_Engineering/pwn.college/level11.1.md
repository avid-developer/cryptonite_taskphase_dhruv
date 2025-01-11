# level11.1
## Description
- Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key. This challenge allows you to patch 2 bytes in the binary, but performs an integrity check afterwards.
## Solution
- The executable program's name is `babyrev-level-11-1`
- I ran `objdump -d -M intel babyrev-level-11-1` to disassemble the binary and got the following:
```

babyrev-level-11-1:     file format elf64-x86-64


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
    1293:       4c 8d 05 86 15 00 00    lea    r8,[rip+0x1586]        # 2820 <open@plt+0x15b0>
    129a:       48 8d 0d 0f 15 00 00    lea    rcx,[rip+0x150f]        # 27b0 <open@plt+0x1540>
    12a1:       48 8d 3d a1 10 00 00    lea    rdi,[rip+0x10a1]        # 2349 <open@plt+0x10d9>
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
    1373:       90                      nop
...
    223d:       90                      nop
    223e:       90                      nop
    223f:       90                      nop
    2240:       5d                      pop    rbp
    2241:       c3                      ret
    2242:       f3 0f 1e fa             endbr64
    2246:       55                      push   rbp
    2247:       48 89 e5                mov    rbp,rsp
    224a:       48 8d 3d b7 0d 00 00    lea    rdi,[rip+0xdb7]        # 3008 <open@plt+0x1d98>
    2251:       e8 3a ef ff ff          call   1190 <puts@plt>
    2256:       be 00 00 00 00          mov    esi,0x0
    225b:       48 8d 3d c2 0d 00 00    lea    rdi,[rip+0xdc2]        # 3024 <open@plt+0x1db4>
    2262:       b8 00 00 00 00          mov    eax,0x0
    2267:       e8 04 f0 ff ff          call   1270 <open@plt>
    226c:       89 05 ee 2d 00 00       mov    DWORD PTR [rip+0x2dee],eax        # 5060 <stdout@GLIBC_2.2.5+0x18>
    2272:       8b 05 e8 2d 00 00       mov    eax,DWORD PTR [rip+0x2de8]        # 5060 <stdout@GLIBC_2.2.5+0x18>
    2278:       85 c0                   test   eax,eax
    227a:       79 4d                   jns    22c9 <open@plt+0x1059>
    227c:       e8 9f ef ff ff          call   1220 <__errno_location@plt>
    2281:       8b 00                   mov    eax,DWORD PTR [rax]
    2283:       89 c7                   mov    edi,eax
    2285:       e8 86 ef ff ff          call   1210 <strerror@plt>
    228a:       48 89 c6                mov    rsi,rax
    228d:       48 8d 3d 9c 0d 00 00    lea    rdi,[rip+0xd9c]        # 3030 <open@plt+0x1dc0>
    2294:       b8 00 00 00 00          mov    eax,0x0
    2299:       e8 d2 ee ff ff          call   1170 <printf@plt>
    229e:       e8 3d ef ff ff          call   11e0 <geteuid@plt>
    22a3:       85 c0                   test   eax,eax
    22a5:       74 18                   je     22bf <open@plt+0x104f>
    22a7:       48 8d 3d b2 0d 00 00    lea    rdi,[rip+0xdb2]        # 3060 <open@plt+0x1df0>
    22ae:       e8 dd ee ff ff          call   1190 <puts@plt>
    22b3:       48 8d 3d ce 0d 00 00    lea    rdi,[rip+0xdce]        # 3088 <open@plt+0x1e18>
    22ba:       e8 d1 ee ff ff          call   1190 <puts@plt>
    22bf:       bf ff ff ff ff          mov    edi,0xffffffff
    22c4:       e8 d7 ee ff ff          call   11a0 <exit@plt>
    22c9:       8b 05 91 2d 00 00       mov    eax,DWORD PTR [rip+0x2d91]        # 5060 <stdout@GLIBC_2.2.5+0x18>
    22cf:       ba 00 01 00 00          mov    edx,0x100
    22d4:       48 8d 35 a5 2d 00 00    lea    rsi,[rip+0x2da5]        # 5080 <stdout@GLIBC_2.2.5+0x38>
    22db:       89 c7                   mov    edi,eax
    22dd:       e8 ee ee ff ff          call   11d0 <read@plt>
    22e2:       89 05 98 2e 00 00       mov    DWORD PTR [rip+0x2e98],eax        # 5180 <stdout@GLIBC_2.2.5+0x138>
    22e8:       8b 05 92 2e 00 00       mov    eax,DWORD PTR [rip+0x2e92]        # 5180 <stdout@GLIBC_2.2.5+0x138>
    22ee:       85 c0                   test   eax,eax
    22f0:       7f 2c                   jg     231e <open@plt+0x10ae>
    22f2:       e8 29 ef ff ff          call   1220 <__errno_location@plt>
    22f7:       8b 00                   mov    eax,DWORD PTR [rax]
    22f9:       89 c7                   mov    edi,eax
    22fb:       e8 10 ef ff ff          call   1210 <strerror@plt>
    2300:       48 89 c6                mov    rsi,rax
    2303:       48 8d 3d d6 0d 00 00    lea    rdi,[rip+0xdd6]        # 30e0 <open@plt+0x1e70>
    230a:       b8 00 00 00 00          mov    eax,0x0
    230f:       e8 5c ee ff ff          call   1170 <printf@plt>
    2314:       bf ff ff ff ff          mov    edi,0xffffffff
    2319:       e8 82 ee ff ff          call   11a0 <exit@plt>
    231e:       8b 05 5c 2e 00 00       mov    eax,DWORD PTR [rip+0x2e5c]        # 5180 <stdout@GLIBC_2.2.5+0x138>
    2324:       48 98                   cdqe
    2326:       48 89 c2                mov    rdx,rax
    2329:       48 8d 35 50 2d 00 00    lea    rsi,[rip+0x2d50]        # 5080 <stdout@GLIBC_2.2.5+0x38>
    2330:       bf 01 00 00 00          mov    edi,0x1
    2335:       e8 26 ef ff ff          call   1260 <write@plt>
    233a:       48 8d 3d c9 0d 00 00    lea    rdi,[rip+0xdc9]        # 310a <open@plt+0x1e9a>
    2341:       e8 4a ee ff ff          call   1190 <puts@plt>
    2346:       90                      nop
    2347:       5d                      pop    rbp
    2348:       c3                      ret
    2349:       f3 0f 1e fa             endbr64
    234d:       55                      push   rbp
    234e:       48 89 e5                mov    rbp,rsp
    2351:       48 81 ec 00 01 00 00    sub    rsp,0x100
    2358:       89 bd 1c ff ff ff       mov    DWORD PTR [rbp-0xe4],edi
    235e:       48 89 b5 10 ff ff ff    mov    QWORD PTR [rbp-0xf0],rsi
    2365:       48 89 95 08 ff ff ff    mov    QWORD PTR [rbp-0xf8],rdx
    236c:       64 48 8b 04 25 28 00    mov    rax,QWORD PTR fs:0x28
    2373:       00 00 
    2375:       48 89 45 f8             mov    QWORD PTR [rbp-0x8],rax
    2379:       31 c0                   xor    eax,eax
    237b:       48 8b 05 be 2c 00 00    mov    rax,QWORD PTR [rip+0x2cbe]        # 5040 <stdin@GLIBC_2.2.5>
    2382:       b9 00 00 00 00          mov    ecx,0x0
    2387:       ba 02 00 00 00          mov    edx,0x2
    238c:       be 00 00 00 00          mov    esi,0x0
    2391:       48 89 c7                mov    rdi,rax
    2394:       e8 17 ee ff ff          call   11b0 <setvbuf@plt>
    2399:       48 8b 05 a8 2c 00 00    mov    rax,QWORD PTR [rip+0x2ca8]        # 5048 <stdout@GLIBC_2.2.5>
    23a0:       b9 00 00 00 00          mov    ecx,0x0
    23a5:       ba 02 00 00 00          mov    edx,0x2
    23aa:       be 00 00 00 00          mov    esi,0x0
    23af:       48 89 c7                mov    rdi,rax
    23b2:       e8 f9 ed ff ff          call   11b0 <setvbuf@plt>
    23b7:       48 8d 3d 4e 0d 00 00    lea    rdi,[rip+0xd4e]        # 310c <open@plt+0x1e9c>
    23be:       e8 cd ed ff ff          call   1190 <puts@plt>
    23c3:       48 8b 85 10 ff ff ff    mov    rax,QWORD PTR [rbp-0xf0]
    23ca:       48 8b 00                mov    rax,QWORD PTR [rax]
    23cd:       48 89 c6                mov    rsi,rax
    23d0:       48 8d 3d 39 0d 00 00    lea    rdi,[rip+0xd39]        # 3110 <open@plt+0x1ea0>
    23d7:       b8 00 00 00 00          mov    eax,0x0
    23dc:       e8 8f ed ff ff          call   1170 <printf@plt>
    23e1:       48 8d 3d 24 0d 00 00    lea    rdi,[rip+0xd24]        # 310c <open@plt+0x1e9c>
    23e8:       e8 a3 ed ff ff          call   1190 <puts@plt>
    23ed:       bf 0a 00 00 00          mov    edi,0xa
    23f2:       e8 c9 ed ff ff          call   11c0 <putchar@plt>
    23f7:       48 8d 3d 2a 0d 00 00    lea    rdi,[rip+0xd2a]        # 3128 <open@plt+0x1eb8>
    23fe:       e8 8d ed ff ff          call   1190 <puts@plt>
    2403:       48 8d 3d 96 0d 00 00    lea    rdi,[rip+0xd96]        # 31a0 <open@plt+0x1f30>
    240a:       e8 81 ed ff ff          call   1190 <puts@plt>
    240f:       48 8d 3d 02 0e 00 00    lea    rdi,[rip+0xe02]        # 3218 <open@plt+0x1fa8>
    2416:       e8 75 ed ff ff          call   1190 <puts@plt>
    241b:       48 8d 3d 6e 0e 00 00    lea    rdi,[rip+0xe6e]        # 3290 <open@plt+0x2020>
    2422:       e8 69 ed ff ff          call   1190 <puts@plt>
    2427:       48 8d 3d a2 0e 00 00    lea    rdi,[rip+0xea2]        # 32d0 <open@plt+0x2060>
    242e:       e8 5d ed ff ff          call   1190 <puts@plt>
    2433:       c7 85 28 ff ff ff 00    mov    DWORD PTR [rbp-0xd8],0x0
    243a:       00 00 00 
    243d:       48 8d 05 25 ef ff ff    lea    rax,[rip+0xffffffffffffef25]        # 1369 <open@plt+0xf9>
    2444:       48 25 00 f0 ff ff       and    rax,0xfffffffffffff000
    244a:       48 2d 00 10 00 00       sub    rax,0x1000
    2450:       48 89 85 38 ff ff ff    mov    QWORD PTR [rbp-0xc8],rax
    2457:       90                      nop
    2458:       8b 85 28 ff ff ff       mov    eax,DWORD PTR [rbp-0xd8]
    245e:       8d 50 01                lea    edx,[rax+0x1]
    2461:       89 95 28 ff ff ff       mov    DWORD PTR [rbp-0xd8],edx
    2467:       c1 e0 0c                shl    eax,0xc
    246a:       48 63 d0                movsxd rdx,eax
    246d:       48 8b 85 38 ff ff ff    mov    rax,QWORD PTR [rbp-0xc8]
    2474:       48 01 d0                add    rax,rdx
    2477:       ba 07 00 00 00          mov    edx,0x7
    247c:       be 00 10 00 00          mov    esi,0x1000
    2481:       48 89 c7                mov    rdi,rax
    2484:       e8 d7 ec ff ff          call   1160 <mprotect@plt>
    2489:       85 c0                   test   eax,eax
    248b:       74 cb                   je     2458 <open@plt+0x11e8>
    248d:       48 8d 3d 9c 0e 00 00    lea    rdi,[rip+0xe9c]        # 3330 <open@plt+0x20c0>
    2494:       e8 f7 ec ff ff          call   1190 <puts@plt>
    2499:       48 8d 85 40 ff ff ff    lea    rax,[rbp-0xc0]
    24a0:       48 89 c7                mov    rdi,rax
    24a3:       e8 88 ed ff ff          call   1230 <MD5_Init@plt>
    24a8:       c7 85 2c ff ff ff 00    mov    DWORD PTR [rbp-0xd4],0x0
    24af:       00 00 00 
    24b2:       eb 35                   jmp    24e9 <open@plt+0x1279>
    24b4:       8b 85 2c ff ff ff       mov    eax,DWORD PTR [rbp-0xd4]
    24ba:       c1 e0 0c                shl    eax,0xc
    24bd:       48 63 d0                movsxd rdx,eax
    24c0:       48 8b 85 38 ff ff ff    mov    rax,QWORD PTR [rbp-0xc8]
    24c7:       48 8d 0c 02             lea    rcx,[rdx+rax*1]
    24cb:       48 8d 85 40 ff ff ff    lea    rax,[rbp-0xc0]
    24d2:       ba 00 10 00 00          mov    edx,0x1000
    24d7:       48 89 ce                mov    rsi,rcx
    24da:       48 89 c7                mov    rdi,rax
    24dd:       e8 1e ed ff ff          call   1200 <MD5_Update@plt>
    24e2:       83 85 2c ff ff ff 01    add    DWORD PTR [rbp-0xd4],0x1
    24e9:       8b 85 28 ff ff ff       mov    eax,DWORD PTR [rbp-0xd8]
    24ef:       83 e8 01                sub    eax,0x1
    24f2:       39 85 2c ff ff ff       cmp    DWORD PTR [rbp-0xd4],eax
    24f8:       7c ba                   jl     24b4 <open@plt+0x1244>
    24fa:       48 8d 95 40 ff ff ff    lea    rdx,[rbp-0xc0]
    2501:       48 8d 45 a0             lea    rax,[rbp-0x60]
    2505:       48 89 d6                mov    rsi,rdx
    2508:       48 89 c7                mov    rdi,rax
    250b:       e8 e0 ec ff ff          call   11f0 <MD5_Final@plt>
    2510:       c7 85 30 ff ff ff 00    mov    DWORD PTR [rbp-0xd0],0x0
    2517:       00 00 00 
    251a:       e9 ce 00 00 00          jmp    25ed <open@plt+0x137d>
    251f:       8b 85 30 ff ff ff       mov    eax,DWORD PTR [rbp-0xd0]
    2525:       83 c0 01                add    eax,0x1
    2528:       89 c6                   mov    esi,eax
    252a:       48 8d 3d 49 0e 00 00    lea    rdi,[rip+0xe49]        # 337a <open@plt+0x210a>
    2531:       b8 00 00 00 00          mov    eax,0x0
    2536:       e8 35 ec ff ff          call   1170 <printf@plt>
    253b:       48 8d 3d 4d 0e 00 00    lea    rdi,[rip+0xe4d]        # 338f <open@plt+0x211f>
    2542:       b8 00 00 00 00          mov    eax,0x0
    2547:       e8 24 ec ff ff          call   1170 <printf@plt>
    254c:       48 8d 85 26 ff ff ff    lea    rax,[rbp-0xda]
    2553:       48 89 c6                mov    rsi,rax
    2556:       48 8d 3d 4b 0e 00 00    lea    rdi,[rip+0xe4b]        # 33a8 <open@plt+0x2138>
    255d:       b8 00 00 00 00          mov    eax,0x0
    2562:       e8 d9 ec ff ff          call   1240 <__isoc99_scanf@plt>
    2567:       48 8d 3d 3e 0e 00 00    lea    rdi,[rip+0xe3e]        # 33ac <open@plt+0x213c>
    256e:       b8 00 00 00 00          mov    eax,0x0
    2573:       e8 f8 eb ff ff          call   1170 <printf@plt>
    2578:       48 8d 85 25 ff ff ff    lea    rax,[rbp-0xdb]
    257f:       48 89 c6                mov    rsi,rax
    2582:       48 8d 3d 35 0e 00 00    lea    rdi,[rip+0xe35]        # 33be <open@plt+0x214e>
    2589:       b8 00 00 00 00          mov    eax,0x0
    258e:       e8 ad ec ff ff          call   1240 <__isoc99_scanf@plt>
    2593:       0f b6 8d 25 ff ff ff    movzx  ecx,BYTE PTR [rbp-0xdb]
    259a:       0f b7 85 26 ff ff ff    movzx  eax,WORD PTR [rbp-0xda]
    25a1:       0f b7 d0                movzx  edx,ax
    25a4:       48 8b 85 38 ff ff ff    mov    rax,QWORD PTR [rbp-0xc8]
    25ab:       48 01 d0                add    rax,rdx
    25ae:       89 ca                   mov    edx,ecx
    25b0:       88 10                   mov    BYTE PTR [rax],dl
    25b2:       0f b6 85 25 ff ff ff    movzx  eax,BYTE PTR [rbp-0xdb]
    25b9:       0f b6 c0                movzx  eax,al
    25bc:       0f b7 95 26 ff ff ff    movzx  edx,WORD PTR [rbp-0xda]
    25c3:       0f b7 ca                movzx  ecx,dx
    25c6:       48 8b 95 38 ff ff ff    mov    rdx,QWORD PTR [rbp-0xc8]
    25cd:       48 01 d1                add    rcx,rdx
    25d0:       89 c2                   mov    edx,eax
    25d2:       48 89 ce                mov    rsi,rcx
    25d5:       48 8d 3d ec 0d 00 00    lea    rdi,[rip+0xdec]        # 33c8 <open@plt+0x2158>
    25dc:       b8 00 00 00 00          mov    eax,0x0
    25e1:       e8 8a eb ff ff          call   1170 <printf@plt>
    25e6:       83 85 30 ff ff ff 01    add    DWORD PTR [rbp-0xd0],0x1
    25ed:       83 bd 30 ff ff ff 01    cmp    DWORD PTR [rbp-0xd0],0x1
    25f4:       0f 8e 25 ff ff ff       jle    251f <open@plt+0x12af>
    25fa:       48 8d 85 40 ff ff ff    lea    rax,[rbp-0xc0]
    2601:       48 89 c7                mov    rdi,rax
    2604:       e8 27 ec ff ff          call   1230 <MD5_Init@plt>
    2609:       c7 85 34 ff ff ff 00    mov    DWORD PTR [rbp-0xcc],0x0
    2610:       00 00 00 
    2613:       eb 35                   jmp    264a <open@plt+0x13da>
    2615:       8b 85 34 ff ff ff       mov    eax,DWORD PTR [rbp-0xcc]
    261b:       c1 e0 0c                shl    eax,0xc
    261e:       48 63 d0                movsxd rdx,eax
    2621:       48 8b 85 38 ff ff ff    mov    rax,QWORD PTR [rbp-0xc8]
    2628:       48 8d 0c 02             lea    rcx,[rdx+rax*1]
    262c:       48 8d 85 40 ff ff ff    lea    rax,[rbp-0xc0]
    2633:       ba 00 10 00 00          mov    edx,0x1000
    2638:       48 89 ce                mov    rsi,rcx
    263b:       48 89 c7                mov    rdi,rax
    263e:       e8 bd eb ff ff          call   1200 <MD5_Update@plt>
    2643:       83 85 34 ff ff ff 01    add    DWORD PTR [rbp-0xcc],0x1
    264a:       8b 85 28 ff ff ff       mov    eax,DWORD PTR [rbp-0xd8]
    2650:       83 e8 01                sub    eax,0x1
    2653:       39 85 34 ff ff ff       cmp    DWORD PTR [rbp-0xcc],eax
    2659:       7c ba                   jl     2615 <open@plt+0x13a5>
    265b:       48 8d 95 40 ff ff ff    lea    rdx,[rbp-0xc0]
    2662:       48 8d 45 b0             lea    rax,[rbp-0x50]
    2666:       48 89 d6                mov    rsi,rdx
    2669:       48 89 c7                mov    rdi,rax
    266c:       e8 7f eb ff ff          call   11f0 <MD5_Final@plt>
    2671:       48 8d 4d b0             lea    rcx,[rbp-0x50]
    2675:       48 8d 45 a0             lea    rax,[rbp-0x60]
    2679:       ba 10 00 00 00          mov    edx,0x10
    267e:       48 89 ce                mov    rsi,rcx
    2681:       48 89 c7                mov    rdi,rax
    2684:       e8 c7 eb ff ff          call   1250 <memcmp@plt>
    2689:       85 c0                   test   eax,eax
    268b:       0f 85 dd 00 00 00       jne    276e <open@plt+0x14fe>
    2691:       48 8d 3d 58 0d 00 00    lea    rdi,[rip+0xd58]        # 33f0 <open@plt+0x2180>
    2698:       e8 f3 ea ff ff          call   1190 <puts@plt>
    269d:       48 c7 45 d0 00 00 00    mov    QWORD PTR [rbp-0x30],0x0
    26a4:       00 
    26a5:       48 c7 45 d8 00 00 00    mov    QWORD PTR [rbp-0x28],0x0
    26ac:       00 
    26ad:       48 c7 45 e0 00 00 00    mov    QWORD PTR [rbp-0x20],0x0
    26b4:       00 
    26b5:       c7 45 e8 00 00 00 00    mov    DWORD PTR [rbp-0x18],0x0
    26bc:       48 8d 3d 8d 0d 00 00    lea    rdi,[rip+0xd8d]        # 3450 <open@plt+0x21e0>
    26c3:       e8 c8 ea ff ff          call   1190 <puts@plt>
    26c8:       48 8d 45 d0             lea    rax,[rbp-0x30]
    26cc:       ba 1b 00 00 00          mov    edx,0x1b
    26d1:       48 89 c6                mov    rsi,rax
    26d4:       bf 00 00 00 00          mov    edi,0x0
    26d9:       e8 f2 ea ff ff          call   11d0 <read@plt>
    26de:       48 8d 85 40 ff ff ff    lea    rax,[rbp-0xc0]
    26e5:       48 89 c7                mov    rdi,rax
    26e8:       e8 43 eb ff ff          call   1230 <MD5_Init@plt>
    26ed:       48 8d 4d d0             lea    rcx,[rbp-0x30]
    26f1:       48 8d 85 40 ff ff ff    lea    rax,[rbp-0xc0]
    26f8:       ba 1b 00 00 00          mov    edx,0x1b
    26fd:       48 89 ce                mov    rsi,rcx
    2700:       48 89 c7                mov    rdi,rax
    2703:       e8 f8 ea ff ff          call   1200 <MD5_Update@plt>
    2708:       48 8d 95 40 ff ff ff    lea    rdx,[rbp-0xc0]
    270f:       48 8d 45 c0             lea    rax,[rbp-0x40]
    2713:       48 89 d6                mov    rsi,rdx
    2716:       48 89 c7                mov    rdi,rax
    2719:       e8 d2 ea ff ff          call   11f0 <MD5_Final@plt>
    271e:       48 8d 45 d0             lea    rax,[rbp-0x30]
    2722:       ba 1b 00 00 00          mov    edx,0x1b
    2727:       be 00 00 00 00          mov    esi,0x0
    272c:       48 89 c7                mov    rdi,rax
    272f:       e8 4c ea ff ff          call   1180 <memset@plt>
    2734:       48 8b 45 c0             mov    rax,QWORD PTR [rbp-0x40]
    2738:       48 8b 55 c8             mov    rdx,QWORD PTR [rbp-0x38]
    273c:       48 89 45 d0             mov    QWORD PTR [rbp-0x30],rax
    2740:       48 89 55 d8             mov    QWORD PTR [rbp-0x28],rdx
    2744:       48 8d 3d 2d 0d 00 00    lea    rdi,[rip+0xd2d]        # 3478 <open@plt+0x2208>
    274b:       e8 40 ea ff ff          call   1190 <puts@plt>
    2750:       48 8d 45 d0             lea    rax,[rbp-0x30]
    2754:       ba 1b 00 00 00          mov    edx,0x1b
    2759:       48 8d 35 b0 28 00 00    lea    rsi,[rip+0x28b0]        # 5010 <open@plt+0x3da0>
    2760:       48 89 c7                mov    rdi,rax
    2763:       e8 e8 ea ff ff          call   1250 <memcmp@plt>
    2768:       85 c0                   test   eax,eax
    276a:       75 2c                   jne    2798 <open@plt+0x1528>
    276c:       eb 16                   jmp    2784 <open@plt+0x1514>
    276e:       48 8d 3d a3 0c 00 00    lea    rdi,[rip+0xca3]        # 3418 <open@plt+0x21a8>
    2775:       e8 16 ea ff ff          call   1190 <puts@plt>
    277a:       bf 01 00 00 00          mov    edi,0x1
    277f:       e8 1c ea ff ff          call   11a0 <exit@plt>
    2784:       b8 00 00 00 00          mov    eax,0x0
    2789:       e8 b4 fa ff ff          call   2242 <open@plt+0xfd2>
    278e:       bf 00 00 00 00          mov    edi,0x0
    2793:       e8 08 ea ff ff          call   11a0 <exit@plt>
    2798:       48 8d 3d fd 0c 00 00    lea    rdi,[rip+0xcfd]        # 349c <open@plt+0x222c>
    279f:       e8 ec e9 ff ff          call   1190 <puts@plt>
    27a4:       bf 01 00 00 00          mov    edi,0x1
    27a9:       e8 f2 e9 ff ff          call   11a0 <exit@plt>
    27ae:       66 90                   xchg   ax,ax
    27b0:       f3 0f 1e fa             endbr64
    27b4:       41 57                   push   r15
    27b6:       4c 8d 3d 63 25 00 00    lea    r15,[rip+0x2563]        # 4d20 <open@plt+0x3ab0>
    27bd:       41 56                   push   r14
    27bf:       49 89 d6                mov    r14,rdx
    27c2:       41 55                   push   r13
    27c4:       49 89 f5                mov    r13,rsi
    27c7:       41 54                   push   r12
    27c9:       41 89 fc                mov    r12d,edi
    27cc:       55                      push   rbp
    27cd:       48 8d 2d 54 25 00 00    lea    rbp,[rip+0x2554]        # 4d28 <open@plt+0x3ab8>
    27d4:       53                      push   rbx
    27d5:       4c 29 fd                sub    rbp,r15
    27d8:       48 83 ec 08             sub    rsp,0x8
    27dc:       e8 1f e8 ff ff          call   1000 <__cxa_finalize@plt-0x150>
    27e1:       48 c1 fd 03             sar    rbp,0x3
    27e5:       74 1f                   je     2806 <open@plt+0x1596>
    27e7:       31 db                   xor    ebx,ebx
    27e9:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]
    27f0:       4c 89 f2                mov    rdx,r14
    27f3:       4c 89 ee                mov    rsi,r13
    27f6:       44 89 e7                mov    edi,r12d
    27f9:       41 ff 14 df             call   QWORD PTR [r15+rbx*8]
    27fd:       48 83 c3 01             add    rbx,0x1
    2801:       48 39 dd                cmp    rbp,rbx
    2804:       75 ea                   jne    27f0 <open@plt+0x1580>
    2806:       48 83 c4 08             add    rsp,0x8
    280a:       5b                      pop    rbx
    280b:       5d                      pop    rbp
    280c:       41 5c                   pop    r12
    280e:       41 5d                   pop    r13
    2810:       41 5e                   pop    r14
    2812:       41 5f                   pop    r15
    2814:       c3                      ret
    2815:       66 66 2e 0f 1f 84 00    data16 cs nop WORD PTR [rax+rax*1+0x0]
    281c:       00 00 00 00 
    2820:       f3 0f 1e fa             endbr64
    2824:       c3                      ret

Disassembly of section .fini:

0000000000002828 <.fini>:
    2828:       f3 0f 1e fa             endbr64
    282c:       48 83 ec 08             sub    rsp,0x8
    2830:       48 83 c4 08             add    rsp,0x8
    2834:       c3                      ret
```
- I searched for `memcmp` and found 2 results in the disassembly, taking a look a the `jne`s that follow them:
  - `    268b:       0f 85 dd 00 00 00       jne    276e <open@plt+0x14fe>`
  - `    276a:       75 2c                   jne    2798 <open@plt+0x1528>`
- The instruction at offset `276a` is the same one we saw in [level11.0](./level11.0.md), but the one at `268b` is different. So I looked it up.
- I found that the opcode `75` is used for short jumps, where the jump offset is a signed 8 bit number. But when the offset is too large, the assembler will automatically convert it to a near jump, which is a 32 bit offset with opcode of `0f 85`.
- With this information, we can obtain the flag by running the binary and entering the correct input:
```
###
### Welcome to ./babyrev-level-11-1!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Unfortunately for you, the license key cannot be reversed. You'll have to crack this program.

In order to ensure code integrity, the code will be hashed and verified.

Changing byte 1/2.
Offset (hex) to change: 276b
New value (hex): 0
The byte has been changed: *0x5c255ec6276b = 0.
Changing byte 2/2.
Offset (hex) to change: 268d
New value (hex): 0
The byte has been changed: *0x5c255ec6268d = 0.
The code's integrity is secure!

Ready to receive your license key!


Checking the received license key!

You win! Here is your flag:
pwn.college{M4DEJednGP2NgsSuHYitR89C0N4.0lM3IDL5QTO0czW}
```
- The flag is `pwn.college{M4DEJednGP2NgsSuHYitR89C0N4.0lM3IDL5QTO0czW}`.