# level10.1
## Description
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key. This challenge allows you to patch 1 byte in the binary.
## Solution
- The executable program's name is `babyrev-level-10-1`
- I ran `objdump -d -M intel babyrev-level-10-1` to disassemble the binary and got the following:
```
babyrev-level-10-1:     file format elf64-x86-64


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
    1293:       4c 8d 05 36 11 00 00    lea    r8,[rip+0x1136]        # 23d0 <open@plt+0x1160>
    129a:       48 8d 0d bf 10 00 00    lea    rcx,[rip+0x10bf]        # 2360 <open@plt+0x10f0>
    12a1:       48 8d 3d 83 0d 00 00    lea    rdi,[rip+0xd83]        # 202b <open@plt+0xdbb>
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
...
    1f20:       90                      nop
    1f21:       90                      nop
    1f22:       5d                      pop    rbp
    1f23:       c3                      ret
    1f24:       f3 0f 1e fa             endbr64
    1f28:       55                      push   rbp
    1f29:       48 89 e5                mov    rbp,rsp
    1f2c:       48 8d 3d d5 10 00 00    lea    rdi,[rip+0x10d5]        # 3008 <open@plt+0x1d98>
    1f33:       e8 58 f2 ff ff          call   1190 <puts@plt>
    1f38:       be 00 00 00 00          mov    esi,0x0
    1f3d:       48 8d 3d e0 10 00 00    lea    rdi,[rip+0x10e0]        # 3024 <open@plt+0x1db4>
    1f44:       b8 00 00 00 00          mov    eax,0x0
    1f49:       e8 22 f3 ff ff          call   1270 <open@plt>
    1f4e:       89 05 0c 31 00 00       mov    DWORD PTR [rip+0x310c],eax        # 5060 <stdout@GLIBC_2.2.5+0x18>
    1f54:       8b 05 06 31 00 00       mov    eax,DWORD PTR [rip+0x3106]        # 5060 <stdout@GLIBC_2.2.5+0x18>
    1f5a:       85 c0                   test   eax,eax
    1f5c:       79 4d                   jns    1fab <open@plt+0xd3b>
    1f5e:       e8 bd f2 ff ff          call   1220 <__errno_location@plt>
    1f63:       8b 00                   mov    eax,DWORD PTR [rax]
    1f65:       89 c7                   mov    edi,eax
    1f67:       e8 a4 f2 ff ff          call   1210 <strerror@plt>
    1f6c:       48 89 c6                mov    rsi,rax
    1f6f:       48 8d 3d ba 10 00 00    lea    rdi,[rip+0x10ba]        # 3030 <open@plt+0x1dc0>
    1f76:       b8 00 00 00 00          mov    eax,0x0
    1f7b:       e8 f0 f1 ff ff          call   1170 <printf@plt>
    1f80:       e8 5b f2 ff ff          call   11e0 <geteuid@plt>
    1f85:       85 c0                   test   eax,eax
    1f87:       74 18                   je     1fa1 <open@plt+0xd31>
    1f89:       48 8d 3d d0 10 00 00    lea    rdi,[rip+0x10d0]        # 3060 <open@plt+0x1df0>
    1f90:       e8 fb f1 ff ff          call   1190 <puts@plt>
    1f95:       48 8d 3d ec 10 00 00    lea    rdi,[rip+0x10ec]        # 3088 <open@plt+0x1e18>
    1f9c:       e8 ef f1 ff ff          call   1190 <puts@plt>
    1fa1:       bf ff ff ff ff          mov    edi,0xffffffff
    1fa6:       e8 f5 f1 ff ff          call   11a0 <exit@plt>
    1fab:       8b 05 af 30 00 00       mov    eax,DWORD PTR [rip+0x30af]        # 5060 <stdout@GLIBC_2.2.5+0x18>
    1fb1:       ba 00 01 00 00          mov    edx,0x100
    1fb6:       48 8d 35 c3 30 00 00    lea    rsi,[rip+0x30c3]        # 5080 <stdout@GLIBC_2.2.5+0x38>
    1fbd:       89 c7                   mov    edi,eax
    1fbf:       e8 0c f2 ff ff          call   11d0 <read@plt>
    1fc4:       89 05 b6 31 00 00       mov    DWORD PTR [rip+0x31b6],eax        # 5180 <stdout@GLIBC_2.2.5+0x138>
    1fca:       8b 05 b0 31 00 00       mov    eax,DWORD PTR [rip+0x31b0]        # 5180 <stdout@GLIBC_2.2.5+0x138>
    1fd0:       85 c0                   test   eax,eax
    1fd2:       7f 2c                   jg     2000 <open@plt+0xd90>
    1fd4:       e8 47 f2 ff ff          call   1220 <__errno_location@plt>
    1fd9:       8b 00                   mov    eax,DWORD PTR [rax]
    1fdb:       89 c7                   mov    edi,eax
    1fdd:       e8 2e f2 ff ff          call   1210 <strerror@plt>
    1fe2:       48 89 c6                mov    rsi,rax
    1fe5:       48 8d 3d f4 10 00 00    lea    rdi,[rip+0x10f4]        # 30e0 <open@plt+0x1e70>
    1fec:       b8 00 00 00 00          mov    eax,0x0
    1ff1:       e8 7a f1 ff ff          call   1170 <printf@plt>
    1ff6:       bf ff ff ff ff          mov    edi,0xffffffff
    1ffb:       e8 a0 f1 ff ff          call   11a0 <exit@plt>
    2000:       8b 05 7a 31 00 00       mov    eax,DWORD PTR [rip+0x317a]        # 5180 <stdout@GLIBC_2.2.5+0x138>
    2006:       48 98                   cdqe
    2008:       48 89 c2                mov    rdx,rax
    200b:       48 8d 35 6e 30 00 00    lea    rsi,[rip+0x306e]        # 5080 <stdout@GLIBC_2.2.5+0x38>
    2012:       bf 01 00 00 00          mov    edi,0x1
    2017:       e8 44 f2 ff ff          call   1260 <write@plt>
    201c:       48 8d 3d e7 10 00 00    lea    rdi,[rip+0x10e7]        # 310a <open@plt+0x1e9a>
    2023:       e8 68 f1 ff ff          call   1190 <puts@plt>
    2028:       90                      nop
    2029:       5d                      pop    rbp
    202a:       c3                      ret
    202b:       f3 0f 1e fa             endbr64
    202f:       55                      push   rbp
    2030:       48 89 e5                mov    rbp,rsp
    2033:       48 81 ec e0 00 00 00    sub    rsp,0xe0
    203a:       89 bd 3c ff ff ff       mov    DWORD PTR [rbp-0xc4],edi
    2040:       48 89 b5 30 ff ff ff    mov    QWORD PTR [rbp-0xd0],rsi
    2047:       48 89 95 28 ff ff ff    mov    QWORD PTR [rbp-0xd8],rdx
    204e:       64 48 8b 04 25 28 00    mov    rax,QWORD PTR fs:0x28
    2055:       00 00 
    2057:       48 89 45 f8             mov    QWORD PTR [rbp-0x8],rax
    205b:       31 c0                   xor    eax,eax
    205d:       48 8b 05 dc 2f 00 00    mov    rax,QWORD PTR [rip+0x2fdc]        # 5040 <stdin@GLIBC_2.2.5>
    2064:       b9 00 00 00 00          mov    ecx,0x0
    2069:       ba 02 00 00 00          mov    edx,0x2
    206e:       be 00 00 00 00          mov    esi,0x0
    2073:       48 89 c7                mov    rdi,rax
    2076:       e8 35 f1 ff ff          call   11b0 <setvbuf@plt>
    207b:       48 8b 05 c6 2f 00 00    mov    rax,QWORD PTR [rip+0x2fc6]        # 5048 <stdout@GLIBC_2.2.5>
    2082:       b9 00 00 00 00          mov    ecx,0x0
    2087:       ba 02 00 00 00          mov    edx,0x2
    208c:       be 00 00 00 00          mov    esi,0x0
    2091:       48 89 c7                mov    rdi,rax
    2094:       e8 17 f1 ff ff          call   11b0 <setvbuf@plt>
    2099:       48 8d 3d 6c 10 00 00    lea    rdi,[rip+0x106c]        # 310c <open@plt+0x1e9c>
    20a0:       e8 eb f0 ff ff          call   1190 <puts@plt>
    20a5:       48 8b 85 30 ff ff ff    mov    rax,QWORD PTR [rbp-0xd0]
    20ac:       48 8b 00                mov    rax,QWORD PTR [rax]
    20af:       48 89 c6                mov    rsi,rax
    20b2:       48 8d 3d 57 10 00 00    lea    rdi,[rip+0x1057]        # 3110 <open@plt+0x1ea0>
    20b9:       b8 00 00 00 00          mov    eax,0x0
    20be:       e8 ad f0 ff ff          call   1170 <printf@plt>
    20c3:       48 8d 3d 42 10 00 00    lea    rdi,[rip+0x1042]        # 310c <open@plt+0x1e9c>
    20ca:       e8 c1 f0 ff ff          call   1190 <puts@plt>
    20cf:       bf 0a 00 00 00          mov    edi,0xa
    20d4:       e8 e7 f0 ff ff          call   11c0 <putchar@plt>
    20d9:       48 8d 3d 48 10 00 00    lea    rdi,[rip+0x1048]        # 3128 <open@plt+0x1eb8>
    20e0:       e8 ab f0 ff ff          call   1190 <puts@plt>
    20e5:       48 8d 3d b4 10 00 00    lea    rdi,[rip+0x10b4]        # 31a0 <open@plt+0x1f30>
    20ec:       e8 9f f0 ff ff          call   1190 <puts@plt>
    20f1:       48 8d 3d 20 11 00 00    lea    rdi,[rip+0x1120]        # 3218 <open@plt+0x1fa8>
    20f8:       e8 93 f0 ff ff          call   1190 <puts@plt>
    20fd:       48 8d 3d 8c 11 00 00    lea    rdi,[rip+0x118c]        # 3290 <open@plt+0x2020>
    2104:       e8 87 f0 ff ff          call   1190 <puts@plt>
    2109:       48 8d 3d c0 11 00 00    lea    rdi,[rip+0x11c0]        # 32d0 <open@plt+0x2060>
    2110:       e8 7b f0 ff ff          call   1190 <puts@plt>
    2115:       c7 85 50 ff ff ff 00    mov    DWORD PTR [rbp-0xb0],0x0
    211c:       00 00 00 
    211f:       48 8d 05 43 f2 ff ff    lea    rax,[rip+0xfffffffffffff243]        # 1369 <open@plt+0xf9>
    2126:       48 25 00 f0 ff ff       and    rax,0xfffffffffffff000
    212c:       48 2d 00 10 00 00       sub    rax,0x1000
    2132:       48 89 85 58 ff ff ff    mov    QWORD PTR [rbp-0xa8],rax
    2139:       90                      nop
    213a:       8b 85 50 ff ff ff       mov    eax,DWORD PTR [rbp-0xb0]
    2140:       8d 50 01                lea    edx,[rax+0x1]
    2143:       89 95 50 ff ff ff       mov    DWORD PTR [rbp-0xb0],edx
    2149:       c1 e0 0c                shl    eax,0xc
    214c:       48 63 d0                movsxd rdx,eax
    214f:       48 8b 85 58 ff ff ff    mov    rax,QWORD PTR [rbp-0xa8]
    2156:       48 01 d0                add    rax,rdx
    2159:       ba 07 00 00 00          mov    edx,0x7
    215e:       be 00 10 00 00          mov    esi,0x1000
    2163:       48 89 c7                mov    rdi,rax
    2166:       e8 f5 ef ff ff          call   1160 <mprotect@plt>
    216b:       85 c0                   test   eax,eax
    216d:       74 cb                   je     213a <open@plt+0xeca>
    216f:       c7 85 54 ff ff ff 00    mov    DWORD PTR [rbp-0xac],0x0
    2176:       00 00 00 
    2179:       e9 ce 00 00 00          jmp    224c <open@plt+0xfdc>
    217e:       8b 85 54 ff ff ff       mov    eax,DWORD PTR [rbp-0xac]
    2184:       83 c0 01                add    eax,0x1
    2187:       89 c6                   mov    esi,eax
    2189:       48 8d 3d 9f 11 00 00    lea    rdi,[rip+0x119f]        # 332f <open@plt+0x20bf>
    2190:       b8 00 00 00 00          mov    eax,0x0
    2195:       e8 d6 ef ff ff          call   1170 <printf@plt>
    219a:       48 8d 3d a3 11 00 00    lea    rdi,[rip+0x11a3]        # 3344 <open@plt+0x20d4>
    21a1:       b8 00 00 00 00          mov    eax,0x0
    21a6:       e8 c5 ef ff ff          call   1170 <printf@plt>
    21ab:       48 8d 85 4e ff ff ff    lea    rax,[rbp-0xb2]
    21b2:       48 89 c6                mov    rsi,rax
    21b5:       48 8d 3d a1 11 00 00    lea    rdi,[rip+0x11a1]        # 335d <open@plt+0x20ed>
    21bc:       b8 00 00 00 00          mov    eax,0x0
    21c1:       e8 7a f0 ff ff          call   1240 <__isoc99_scanf@plt>
    21c6:       48 8d 3d 94 11 00 00    lea    rdi,[rip+0x1194]        # 3361 <open@plt+0x20f1>
    21cd:       b8 00 00 00 00          mov    eax,0x0
    21d2:       e8 99 ef ff ff          call   1170 <printf@plt>
    21d7:       48 8d 85 4d ff ff ff    lea    rax,[rbp-0xb3]
    21de:       48 89 c6                mov    rsi,rax
    21e1:       48 8d 3d 8b 11 00 00    lea    rdi,[rip+0x118b]        # 3373 <open@plt+0x2103>
    21e8:       b8 00 00 00 00          mov    eax,0x0
    21ed:       e8 4e f0 ff ff          call   1240 <__isoc99_scanf@plt>
    21f2:       0f b6 8d 4d ff ff ff    movzx  ecx,BYTE PTR [rbp-0xb3]
    21f9:       0f b7 85 4e ff ff ff    movzx  eax,WORD PTR [rbp-0xb2]
    2200:       0f b7 d0                movzx  edx,ax
    2203:       48 8b 85 58 ff ff ff    mov    rax,QWORD PTR [rbp-0xa8]
    220a:       48 01 d0                add    rax,rdx
    220d:       89 ca                   mov    edx,ecx
    220f:       88 10                   mov    BYTE PTR [rax],dl
    2211:       0f b6 85 4d ff ff ff    movzx  eax,BYTE PTR [rbp-0xb3]
    2218:       0f b6 c0                movzx  eax,al
    221b:       0f b7 95 4e ff ff ff    movzx  edx,WORD PTR [rbp-0xb2]
    2222:       0f b7 ca                movzx  ecx,dx
    2225:       48 8b 95 58 ff ff ff    mov    rdx,QWORD PTR [rbp-0xa8]
    222c:       48 01 d1                add    rcx,rdx
    222f:       89 c2                   mov    edx,eax
    2231:       48 89 ce                mov    rsi,rcx
    2234:       48 8d 3d 3d 11 00 00    lea    rdi,[rip+0x113d]        # 3378 <open@plt+0x2108>
    223b:       b8 00 00 00 00          mov    eax,0x0
    2240:       e8 2b ef ff ff          call   1170 <printf@plt>
    2245:       83 85 54 ff ff ff 01    add    DWORD PTR [rbp-0xac],0x1
    224c:       83 bd 54 ff ff ff 00    cmp    DWORD PTR [rbp-0xac],0x0
    2253:       0f 8e 25 ff ff ff       jle    217e <open@plt+0xf0e>
    2259:       48 c7 45 d0 00 00 00    mov    QWORD PTR [rbp-0x30],0x0
    2260:       00 
    2261:       48 c7 45 d8 00 00 00    mov    QWORD PTR [rbp-0x28],0x0
    2268:       00 
    2269:       48 c7 45 e0 00 00 00    mov    QWORD PTR [rbp-0x20],0x0
    2270:       00 
    2271:       c7 45 e8 00 00 00 00    mov    DWORD PTR [rbp-0x18],0x0
    2278:       66 c7 45 ec 00 00       mov    WORD PTR [rbp-0x14],0x0
    227e:       48 8d 3d 1b 11 00 00    lea    rdi,[rip+0x111b]        # 33a0 <open@plt+0x2130>
    2285:       e8 06 ef ff ff          call   1190 <puts@plt>
    228a:       48 8d 45 d0             lea    rax,[rbp-0x30]
    228e:       ba 1d 00 00 00          mov    edx,0x1d
    2293:       48 89 c6                mov    rsi,rax
    2296:       bf 00 00 00 00          mov    edi,0x0
    229b:       e8 30 ef ff ff          call   11d0 <read@plt>
    22a0:       48 8d 85 60 ff ff ff    lea    rax,[rbp-0xa0]
    22a7:       48 89 c7                mov    rdi,rax
    22aa:       e8 81 ef ff ff          call   1230 <MD5_Init@plt>
    22af:       48 8d 4d d0             lea    rcx,[rbp-0x30]
    22b3:       48 8d 85 60 ff ff ff    lea    rax,[rbp-0xa0]
    22ba:       ba 1d 00 00 00          mov    edx,0x1d
    22bf:       48 89 ce                mov    rsi,rcx
    22c2:       48 89 c7                mov    rdi,rax
    22c5:       e8 36 ef ff ff          call   1200 <MD5_Update@plt>
    22ca:       48 8d 95 60 ff ff ff    lea    rdx,[rbp-0xa0]
    22d1:       48 8d 45 c0             lea    rax,[rbp-0x40]
    22d5:       48 89 d6                mov    rsi,rdx
    22d8:       48 89 c7                mov    rdi,rax
    22db:       e8 10 ef ff ff          call   11f0 <MD5_Final@plt>
    22e0:       48 8d 45 d0             lea    rax,[rbp-0x30]
    22e4:       ba 1d 00 00 00          mov    edx,0x1d
    22e9:       be 00 00 00 00          mov    esi,0x0
    22ee:       48 89 c7                mov    rdi,rax
    22f1:       e8 8a ee ff ff          call   1180 <memset@plt>
    22f6:       48 8b 45 c0             mov    rax,QWORD PTR [rbp-0x40]
    22fa:       48 8b 55 c8             mov    rdx,QWORD PTR [rbp-0x38]
    22fe:       48 89 45 d0             mov    QWORD PTR [rbp-0x30],rax
    2302:       48 89 55 d8             mov    QWORD PTR [rbp-0x28],rdx
    2306:       48 8d 3d bb 10 00 00    lea    rdi,[rip+0x10bb]        # 33c8 <open@plt+0x2158>
    230d:       e8 7e ee ff ff          call   1190 <puts@plt>
    2312:       48 8d 45 d0             lea    rax,[rbp-0x30]
    2316:       ba 1d 00 00 00          mov    edx,0x1d
    231b:       48 8d 35 ee 2c 00 00    lea    rsi,[rip+0x2cee]        # 5010 <open@plt+0x3da0>
    2322:       48 89 c7                mov    rdi,rax
    2325:       e8 26 ef ff ff          call   1250 <memcmp@plt>
    232a:       85 c0                   test   eax,eax
    232c:       75 14                   jne    2342 <open@plt+0x10d2>
    232e:       b8 00 00 00 00          mov    eax,0x0
    2333:       e8 ec fb ff ff          call   1f24 <open@plt+0xcb4>
    2338:       bf 00 00 00 00          mov    edi,0x0
    233d:       e8 5e ee ff ff          call   11a0 <exit@plt>
    2342:       48 8d 3d a3 10 00 00    lea    rdi,[rip+0x10a3]        # 33ec <open@plt+0x217c>
    2349:       e8 42 ee ff ff          call   1190 <puts@plt>
    234e:       bf 01 00 00 00          mov    edi,0x1
    2353:       e8 48 ee ff ff          call   11a0 <exit@plt>
    2358:       0f 1f 84 00 00 00 00    nop    DWORD PTR [rax+rax*1+0x0]
    235f:       00 
    2360:       f3 0f 1e fa             endbr64
    2364:       41 57                   push   r15
    2366:       4c 8d 3d b3 29 00 00    lea    r15,[rip+0x29b3]        # 4d20 <open@plt+0x3ab0>
    236d:       41 56                   push   r14
    236f:       49 89 d6                mov    r14,rdx
    2372:       41 55                   push   r13
    2374:       49 89 f5                mov    r13,rsi
    2377:       41 54                   push   r12
    2379:       41 89 fc                mov    r12d,edi
    237c:       55                      push   rbp
    237d:       48 8d 2d a4 29 00 00    lea    rbp,[rip+0x29a4]        # 4d28 <open@plt+0x3ab8>
    2384:       53                      push   rbx
    2385:       4c 29 fd                sub    rbp,r15
    2388:       48 83 ec 08             sub    rsp,0x8
    238c:       e8 6f ec ff ff          call   1000 <__cxa_finalize@plt-0x150>
    2391:       48 c1 fd 03             sar    rbp,0x3
    2395:       74 1f                   je     23b6 <open@plt+0x1146>
    2397:       31 db                   xor    ebx,ebx
    2399:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]
    23a0:       4c 89 f2                mov    rdx,r14
    23a3:       4c 89 ee                mov    rsi,r13
    23a6:       44 89 e7                mov    edi,r12d
    23a9:       41 ff 14 df             call   QWORD PTR [r15+rbx*8]
    23ad:       48 83 c3 01             add    rbx,0x1
    23b1:       48 39 dd                cmp    rbp,rbx
    23b4:       75 ea                   jne    23a0 <open@plt+0x1130>
    23b6:       48 83 c4 08             add    rsp,0x8
    23ba:       5b                      pop    rbx
    23bb:       5d                      pop    rbp
    23bc:       41 5c                   pop    r12
    23be:       41 5d                   pop    r13
    23c0:       41 5e                   pop    r14
    23c2:       41 5f                   pop    r15
    23c4:       c3                      ret
    23c5:       66 66 2e 0f 1f 84 00    data16 cs nop WORD PTR [rax+rax*1+0x0]
    23cc:       00 00 00 00 
    23d0:       f3 0f 1e fa             endbr64
    23d4:       c3                      ret

Disassembly of section .fini:

00000000000023d8 <.fini>:
    23d8:       f3 0f 1e fa             endbr64
    23dc:       48 83 ec 08             sub    rsp,0x8
    23e0:       48 83 c4 08             add    rsp,0x8
    23e4:       c3                      ret
```
- Similar to [level10.0](./level10.0.md), we can patch the offset of the `jne` instruction to `0`, so the `jne` instruction effectively does nothing and the program will continue to execute the next instruction.
- `232c:       75 14                   jne    2342 <open@plt+0x10d2>`, So I need to change the byte at `232d` to `0`. 
- Running and patching the program:
```
###
### Welcome to ./babyrev-level-10-1!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Unfortunately for you, the license key cannot be reversed. You'll have to crack this program.

Changing byte 1/1.
Offset (hex) to change: 232d
New value (hex): 0
The byte has been changed: *0x57893878732d = 0.
Ready to receive your license key!

test
Checking the received license key!

You win! Here is your flag:
pwn.college{49Hpu-RHWgN_oEygC8YkR6hVkEf.0FM3IDL5QTO0czW}
```
- The flag is `pwn.college{49Hpu-RHWgN_oEygC8YkR6hVkEf.0FM3IDL5QTO0czW}`.