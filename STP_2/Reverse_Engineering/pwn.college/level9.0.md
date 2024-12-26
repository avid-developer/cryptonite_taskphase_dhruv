# level9.0
## Description
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key. This challenge allows you to patch 5 bytes in the binary.
## Solution
- The executable program's name is `babyrev-level-9-0`
- Running the program:
```###
### Welcome to ./babyrev-level-9-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Unfortunately for you, the license key cannot be reversed. You'll have to crack this program.

Changing byte 1/5.
Offset (hex) to change: 
```
- Right off the bat, this challenge is different than all the previous levels as we can't reverse the license key. We have to modify bytes and crack this program. I went ahead and gave some sample inputs to see what the program does:
```
Changing byte 1/5.
Offset (hex) to change: 0
New value (hex): 0
The byte has been changed: *0x61ee00d8e000 = 0.
Changing byte 2/5.
Offset (hex) to change: 0
New value (hex): 0
The byte has been changed: *0x61ee00d8e000 = 0.
Changing byte 3/5.
Offset (hex) to change: 0
New value (hex): 0
The byte has been changed: *0x61ee00d8e000 = 0.
Changing byte 4/5.
Offset (hex) to change: 0
New value (hex): 0
The byte has been changed: *0x61ee00d8e000 = 0.
Changing byte 5/5.
Offset (hex) to change: 0
New value (hex): 0
The byte has been changed: *0x61ee00d8e000 = 0.
Ready to receive your license key!

test
Initial input:

        74 65 73 74 0a 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

This challenge is now mangling your input using the `md5` mangler. This mangler cannot be reversed.

This mangled your input, resulting in:

        db 5c cc 66 72 0c fc 07 fb 4a b4 9c f5 cc c6 19 00 00 00 00 00 00 00 00 00 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        db 5c cc 66 72 0c fc 07 fb 4a b4 9c f5 cc c6 19 00 00 00 00 00 00 00 00 00 

Expected result:

        0f c8 33 ac 53 52 fe e2 94 2e a4 5b 27 4e d1 a5 00 00 00 00 00 00 00 00 00 

Checking the received license key!

Wrong! No flag for you!
```
- Since we can't reverse the MD5 hash, we have to find a way to bypass the check. I ran `objdump -d -M intel babyrev-level-9-0` to disassemble the binary and got the following:
```
babyrev-level-9-0:     file format elf64-x86-64


Disassembly of section .init:

0000000000001000 <_init>:
    1000:       f3 0f 1e fa             endbr64
    1004:       48 83 ec 08             sub    rsp,0x8
    1008:       48 8b 05 c9 3f 00 00    mov    rax,QWORD PTR [rip+0x3fc9]        # 4fd8 <__gmon_start__>
    100f:       48 85 c0                test   rax,rax
    1012:       74 02                   je     1016 <_init+0x16>
    1014:       ff d0                   call   rax
    1016:       48 83 c4 08             add    rsp,0x8
    101a:       c3                      ret

Disassembly of section .plt:

0000000000001020 <.plt>:
    1020:       ff 35 12 3f 00 00       push   QWORD PTR [rip+0x3f12]        # 4f38 <_GLOBAL_OFFSET_TABLE_+0x8>
    1026:       f2 ff 25 13 3f 00 00    bnd jmp QWORD PTR [rip+0x3f13]        # 4f40 <_GLOBAL_OFFSET_TABLE_+0x10>
    102d:       0f 1f 00                nop    DWORD PTR [rax]
    1030:       f3 0f 1e fa             endbr64
    1034:       68 00 00 00 00          push   0x0
    1039:       f2 e9 e1 ff ff ff       bnd jmp 1020 <.plt>
    103f:       90                      nop
    1040:       f3 0f 1e fa             endbr64
    1044:       68 01 00 00 00          push   0x1
    1049:       f2 e9 d1 ff ff ff       bnd jmp 1020 <.plt>
    104f:       90                      nop
    1050:       f3 0f 1e fa             endbr64
    1054:       68 02 00 00 00          push   0x2
    1059:       f2 e9 c1 ff ff ff       bnd jmp 1020 <.plt>
    105f:       90                      nop
    1060:       f3 0f 1e fa             endbr64
    1064:       68 03 00 00 00          push   0x3
    1069:       f2 e9 b1 ff ff ff       bnd jmp 1020 <.plt>
    106f:       90                      nop
    1070:       f3 0f 1e fa             endbr64
    1074:       68 04 00 00 00          push   0x4
    1079:       f2 e9 a1 ff ff ff       bnd jmp 1020 <.plt>
    107f:       90                      nop
    1080:       f3 0f 1e fa             endbr64
    1084:       68 05 00 00 00          push   0x5
    1089:       f2 e9 91 ff ff ff       bnd jmp 1020 <.plt>
    108f:       90                      nop
    1090:       f3 0f 1e fa             endbr64
    1094:       68 06 00 00 00          push   0x6
    1099:       f2 e9 81 ff ff ff       bnd jmp 1020 <.plt>
    109f:       90                      nop
    10a0:       f3 0f 1e fa             endbr64
    10a4:       68 07 00 00 00          push   0x7
    10a9:       f2 e9 71 ff ff ff       bnd jmp 1020 <.plt>
    10af:       90                      nop
    10b0:       f3 0f 1e fa             endbr64
    10b4:       68 08 00 00 00          push   0x8
    10b9:       f2 e9 61 ff ff ff       bnd jmp 1020 <.plt>
    10bf:       90                      nop
    10c0:       f3 0f 1e fa             endbr64
    10c4:       68 09 00 00 00          push   0x9
    10c9:       f2 e9 51 ff ff ff       bnd jmp 1020 <.plt>
    10cf:       90                      nop
    10d0:       f3 0f 1e fa             endbr64
    10d4:       68 0a 00 00 00          push   0xa
    10d9:       f2 e9 41 ff ff ff       bnd jmp 1020 <.plt>
    10df:       90                      nop
    10e0:       f3 0f 1e fa             endbr64
    10e4:       68 0b 00 00 00          push   0xb
    10e9:       f2 e9 31 ff ff ff       bnd jmp 1020 <.plt>
    10ef:       90                      nop
    10f0:       f3 0f 1e fa             endbr64
    10f4:       68 0c 00 00 00          push   0xc
    10f9:       f2 e9 21 ff ff ff       bnd jmp 1020 <.plt>
    10ff:       90                      nop
    1100:       f3 0f 1e fa             endbr64
    1104:       68 0d 00 00 00          push   0xd
    1109:       f2 e9 11 ff ff ff       bnd jmp 1020 <.plt>
    110f:       90                      nop
    1110:       f3 0f 1e fa             endbr64
    1114:       68 0e 00 00 00          push   0xe
    1119:       f2 e9 01 ff ff ff       bnd jmp 1020 <.plt>
    111f:       90                      nop
    1120:       f3 0f 1e fa             endbr64
    1124:       68 0f 00 00 00          push   0xf
    1129:       f2 e9 f1 fe ff ff       bnd jmp 1020 <.plt>
    112f:       90                      nop
    1130:       f3 0f 1e fa             endbr64
    1134:       68 10 00 00 00          push   0x10
    1139:       f2 e9 e1 fe ff ff       bnd jmp 1020 <.plt>
    113f:       90                      nop
    1140:       f3 0f 1e fa             endbr64
    1144:       68 11 00 00 00          push   0x11
    1149:       f2 e9 d1 fe ff ff       bnd jmp 1020 <.plt>
    114f:       90                      nop

Disassembly of section .plt.got:

0000000000001150 <__cxa_finalize@plt>:
    1150:       f3 0f 1e fa             endbr64
    1154:       f2 ff 25 9d 3e 00 00    bnd jmp QWORD PTR [rip+0x3e9d]        # 4ff8 <__cxa_finalize@GLIBC_2.2.5>
    115b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

Disassembly of section .plt.sec:

0000000000001160 <mprotect@plt>:
    1160:       f3 0f 1e fa             endbr64
    1164:       f2 ff 25 dd 3d 00 00    bnd jmp QWORD PTR [rip+0x3ddd]        # 4f48 <mprotect@GLIBC_2.2.5>
    116b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001170 <printf@plt>:
    1170:       f3 0f 1e fa             endbr64
    1174:       f2 ff 25 d5 3d 00 00    bnd jmp QWORD PTR [rip+0x3dd5]        # 4f50 <printf@GLIBC_2.2.5>
    117b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001180 <memset@plt>:
    1180:       f3 0f 1e fa             endbr64
    1184:       f2 ff 25 cd 3d 00 00    bnd jmp QWORD PTR [rip+0x3dcd]        # 4f58 <memset@GLIBC_2.2.5>
    118b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001190 <puts@plt>:
    1190:       f3 0f 1e fa             endbr64
    1194:       f2 ff 25 c5 3d 00 00    bnd jmp QWORD PTR [rip+0x3dc5]        # 4f60 <puts@GLIBC_2.2.5>
    119b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

00000000000011a0 <exit@plt>:
    11a0:       f3 0f 1e fa             endbr64
    11a4:       f2 ff 25 bd 3d 00 00    bnd jmp QWORD PTR [rip+0x3dbd]        # 4f68 <exit@GLIBC_2.2.5>
    11ab:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

00000000000011b0 <setvbuf@plt>:
    11b0:       f3 0f 1e fa             endbr64
    11b4:       f2 ff 25 b5 3d 00 00    bnd jmp QWORD PTR [rip+0x3db5]        # 4f70 <setvbuf@GLIBC_2.2.5>
    11bb:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

00000000000011c0 <putchar@plt>:
    11c0:       f3 0f 1e fa             endbr64
    11c4:       f2 ff 25 ad 3d 00 00    bnd jmp QWORD PTR [rip+0x3dad]        # 4f78 <putchar@GLIBC_2.2.5>
    11cb:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

00000000000011d0 <read@plt>:
    11d0:       f3 0f 1e fa             endbr64
    11d4:       f2 ff 25 a5 3d 00 00    bnd jmp QWORD PTR [rip+0x3da5]        # 4f80 <read@GLIBC_2.2.5>
    11db:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

00000000000011e0 <geteuid@plt>:
    11e0:       f3 0f 1e fa             endbr64
    11e4:       f2 ff 25 9d 3d 00 00    bnd jmp QWORD PTR [rip+0x3d9d]        # 4f88 <geteuid@GLIBC_2.2.5>
    11eb:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

00000000000011f0 <MD5_Final@plt>:
    11f0:       f3 0f 1e fa             endbr64
    11f4:       f2 ff 25 95 3d 00 00    bnd jmp QWORD PTR [rip+0x3d95]        # 4f90 <MD5_Final@OPENSSL_1_1_0>
    11fb:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001200 <MD5_Update@plt>:
    1200:       f3 0f 1e fa             endbr64
    1204:       f2 ff 25 8d 3d 00 00    bnd jmp QWORD PTR [rip+0x3d8d]        # 4f98 <MD5_Update@OPENSSL_1_1_0>
    120b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001210 <strerror@plt>:
    1210:       f3 0f 1e fa             endbr64
    1214:       f2 ff 25 85 3d 00 00    bnd jmp QWORD PTR [rip+0x3d85]        # 4fa0 <strerror@GLIBC_2.2.5>
    121b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001220 <__errno_location@plt>:
    1220:       f3 0f 1e fa             endbr64
    1224:       f2 ff 25 7d 3d 00 00    bnd jmp QWORD PTR [rip+0x3d7d]        # 4fa8 <__errno_location@GLIBC_2.2.5>
    122b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001230 <MD5_Init@plt>:
    1230:       f3 0f 1e fa             endbr64
    1234:       f2 ff 25 75 3d 00 00    bnd jmp QWORD PTR [rip+0x3d75]        # 4fb0 <MD5_Init@OPENSSL_1_1_0>
    123b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001240 <__isoc99_scanf@plt>:
    1240:       f3 0f 1e fa             endbr64
    1244:       f2 ff 25 6d 3d 00 00    bnd jmp QWORD PTR [rip+0x3d6d]        # 4fb8 <__isoc99_scanf@GLIBC_2.7>
    124b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001250 <memcmp@plt>:
    1250:       f3 0f 1e fa             endbr64
    1254:       f2 ff 25 65 3d 00 00    bnd jmp QWORD PTR [rip+0x3d65]        # 4fc0 <memcmp@GLIBC_2.2.5>
    125b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001260 <write@plt>:
    1260:       f3 0f 1e fa             endbr64
    1264:       f2 ff 25 5d 3d 00 00    bnd jmp QWORD PTR [rip+0x3d5d]        # 4fc8 <write@GLIBC_2.2.5>
    126b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001270 <open@plt>:
    1270:       f3 0f 1e fa             endbr64
    1274:       f2 ff 25 55 3d 00 00    bnd jmp QWORD PTR [rip+0x3d55]        # 4fd0 <open@GLIBC_2.2.5>
    127b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

Disassembly of section .text:

0000000000001280 <_start>:
    1280:       f3 0f 1e fa             endbr64
    1284:       31 ed                   xor    ebp,ebp
    1286:       49 89 d1                mov    r9,rdx
    1289:       5e                      pop    rsi
    128a:       48 89 e2                mov    rdx,rsp
    128d:       48 83 e4 f0             and    rsp,0xfffffffffffffff0
    1291:       50                      push   rax
    1292:       54                      push   rsp
    1293:       4c 8d 05 c6 15 00 00    lea    r8,[rip+0x15c6]        # 2860 <__libc_csu_fini>
    129a:       48 8d 0d 4f 15 00 00    lea    rcx,[rip+0x154f]        # 27f0 <__libc_csu_init>
    12a1:       48 8d 3d 7d 10 00 00    lea    rdi,[rip+0x107d]        # 2325 <main>
    12a8:       ff 15 32 3d 00 00       call   QWORD PTR [rip+0x3d32]        # 4fe0 <__libc_start_main@GLIBC_2.2.5>
    12ae:       f4                      hlt
    12af:       90                      nop

00000000000012b0 <deregister_tm_clones>:
    12b0:       48 8d 3d 71 3d 00 00    lea    rdi,[rip+0x3d71]        # 5028 <__TMC_END__>
    12b7:       48 8d 05 6a 3d 00 00    lea    rax,[rip+0x3d6a]        # 5028 <__TMC_END__>
    12be:       48 39 f8                cmp    rax,rdi
    12c1:       74 15                   je     12d8 <deregister_tm_clones+0x28>
    12c3:       48 8b 05 1e 3d 00 00    mov    rax,QWORD PTR [rip+0x3d1e]        # 4fe8 <_ITM_deregisterTMCloneTable>
    12ca:       48 85 c0                test   rax,rax
    12cd:       74 09                   je     12d8 <deregister_tm_clones+0x28>
    12cf:       ff e0                   jmp    rax
    12d1:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]
    12d8:       c3                      ret
    12d9:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]

00000000000012e0 <register_tm_clones>:
    12e0:       48 8d 3d 41 3d 00 00    lea    rdi,[rip+0x3d41]        # 5028 <__TMC_END__>
    12e7:       48 8d 35 3a 3d 00 00    lea    rsi,[rip+0x3d3a]        # 5028 <__TMC_END__>
    12ee:       48 29 fe                sub    rsi,rdi
    12f1:       48 89 f0                mov    rax,rsi
    12f4:       48 c1 ee 3f             shr    rsi,0x3f
    12f8:       48 c1 f8 03             sar    rax,0x3
    12fc:       48 01 c6                add    rsi,rax
    12ff:       48 d1 fe                sar    rsi,1
    1302:       74 14                   je     1318 <register_tm_clones+0x38>
    1304:       48 8b 05 e5 3c 00 00    mov    rax,QWORD PTR [rip+0x3ce5]        # 4ff0 <_ITM_registerTMCloneTable>
    130b:       48 85 c0                test   rax,rax
    130e:       74 08                   je     1318 <register_tm_clones+0x38>
    1310:       ff e0                   jmp    rax
    1312:       66 0f 1f 44 00 00       nop    WORD PTR [rax+rax*1+0x0]
    1318:       c3                      ret
    1319:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]

0000000000001320 <__do_global_dtors_aux>:
    1320:       f3 0f 1e fa             endbr64
    1324:       80 3d 25 3d 00 00 00    cmp    BYTE PTR [rip+0x3d25],0x0        # 5050 <completed.8061>
    132b:       75 2b                   jne    1358 <__do_global_dtors_aux+0x38>
    132d:       55                      push   rbp
    132e:       48 83 3d c2 3c 00 00    cmp    QWORD PTR [rip+0x3cc2],0x0        # 4ff8 <__cxa_finalize@GLIBC_2.2.5>
    1335:       00 
    1336:       48 89 e5                mov    rbp,rsp
    1339:       74 0c                   je     1347 <__do_global_dtors_aux+0x27>
    133b:       48 8b 3d c6 3c 00 00    mov    rdi,QWORD PTR [rip+0x3cc6]        # 5008 <__dso_handle>
    1342:       e8 09 fe ff ff          call   1150 <__cxa_finalize@plt>
    1347:       e8 64 ff ff ff          call   12b0 <deregister_tm_clones>
    134c:       c6 05 fd 3c 00 00 01    mov    BYTE PTR [rip+0x3cfd],0x1        # 5050 <completed.8061>
    1353:       5d                      pop    rbp
    1354:       c3                      ret
    1355:       0f 1f 00                nop    DWORD PTR [rax]
    1358:       c3                      ret
    1359:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]

0000000000001360 <frame_dummy>:
    1360:       f3 0f 1e fa             endbr64
    1364:       e9 77 ff ff ff          jmp    12e0 <register_tm_clones>

0000000000001369 <bin_padding>:
    1369:       f3 0f 1e fa             endbr64
    136d:       55                      push   rbp
    136e:       48 89 e5                mov    rbp,rsp
    1371:       90                      nop
    1372:       90                      nop
... (a lot of nop instructions)
    221a:       90                      nop
    221b:       90                      nop
    221c:       5d                      pop    rbp
    221d:       c3                      ret

000000000000221e <win>:
    221e:       f3 0f 1e fa             endbr64
    2222:       55                      push   rbp
    2223:       48 89 e5                mov    rbp,rsp
    2226:       48 8d 3d db 0d 00 00    lea    rdi,[rip+0xddb]        # 3008 <_IO_stdin_used+0x8>
    222d:       e8 5e ef ff ff          call   1190 <puts@plt>
    2232:       be 00 00 00 00          mov    esi,0x0
    2237:       48 8d 3d e6 0d 00 00    lea    rdi,[rip+0xde6]        # 3024 <_IO_stdin_used+0x24>
    223e:       b8 00 00 00 00          mov    eax,0x0
    2243:       e8 28 f0 ff ff          call   1270 <open@plt>
    2248:       89 05 12 2e 00 00       mov    DWORD PTR [rip+0x2e12],eax        # 5060 <flag_fd.5757>
    224e:       8b 05 0c 2e 00 00       mov    eax,DWORD PTR [rip+0x2e0c]        # 5060 <flag_fd.5757>
    2254:       85 c0                   test   eax,eax
    2256:       79 4d                   jns    22a5 <win+0x87>
    2258:       e8 c3 ef ff ff          call   1220 <__errno_location@plt>
    225d:       8b 00                   mov    eax,DWORD PTR [rax]
    225f:       89 c7                   mov    edi,eax
    2261:       e8 aa ef ff ff          call   1210 <strerror@plt>
    2266:       48 89 c6                mov    rsi,rax
    2269:       48 8d 3d c0 0d 00 00    lea    rdi,[rip+0xdc0]        # 3030 <_IO_stdin_used+0x30>
    2270:       b8 00 00 00 00          mov    eax,0x0
    2275:       e8 f6 ee ff ff          call   1170 <printf@plt>
    227a:       e8 61 ef ff ff          call   11e0 <geteuid@plt>
    227f:       85 c0                   test   eax,eax
    2281:       74 18                   je     229b <win+0x7d>
    2283:       48 8d 3d d6 0d 00 00    lea    rdi,[rip+0xdd6]        # 3060 <_IO_stdin_used+0x60>
    228a:       e8 01 ef ff ff          call   1190 <puts@plt>
    228f:       48 8d 3d f2 0d 00 00    lea    rdi,[rip+0xdf2]        # 3088 <_IO_stdin_used+0x88>
    2296:       e8 f5 ee ff ff          call   1190 <puts@plt>
    229b:       bf ff ff ff ff          mov    edi,0xffffffff
    22a0:       e8 fb ee ff ff          call   11a0 <exit@plt>
    22a5:       8b 05 b5 2d 00 00       mov    eax,DWORD PTR [rip+0x2db5]        # 5060 <flag_fd.5757>
    22ab:       ba 00 01 00 00          mov    edx,0x100
    22b0:       48 8d 35 c9 2d 00 00    lea    rsi,[rip+0x2dc9]        # 5080 <flag.5756>
    22b7:       89 c7                   mov    edi,eax
    22b9:       e8 12 ef ff ff          call   11d0 <read@plt>
    22be:       89 05 bc 2e 00 00       mov    DWORD PTR [rip+0x2ebc],eax        # 5180 <flag_length.5758>
    22c4:       8b 05 b6 2e 00 00       mov    eax,DWORD PTR [rip+0x2eb6]        # 5180 <flag_length.5758>
    22ca:       85 c0                   test   eax,eax
    22cc:       7f 2c                   jg     22fa <win+0xdc>
    22ce:       e8 4d ef ff ff          call   1220 <__errno_location@plt>
    22d3:       8b 00                   mov    eax,DWORD PTR [rax]
    22d5:       89 c7                   mov    edi,eax
    22d7:       e8 34 ef ff ff          call   1210 <strerror@plt>
    22dc:       48 89 c6                mov    rsi,rax
    22df:       48 8d 3d fa 0d 00 00    lea    rdi,[rip+0xdfa]        # 30e0 <_IO_stdin_used+0xe0>
    22e6:       b8 00 00 00 00          mov    eax,0x0
    22eb:       e8 80 ee ff ff          call   1170 <printf@plt>
    22f0:       bf ff ff ff ff          mov    edi,0xffffffff
    22f5:       e8 a6 ee ff ff          call   11a0 <exit@plt>
    22fa:       8b 05 80 2e 00 00       mov    eax,DWORD PTR [rip+0x2e80]        # 5180 <flag_length.5758>
    2300:       48 98                   cdqe
    2302:       48 89 c2                mov    rdx,rax
    2305:       48 8d 35 74 2d 00 00    lea    rsi,[rip+0x2d74]        # 5080 <flag.5756>
    230c:       bf 01 00 00 00          mov    edi,0x1
    2311:       e8 4a ef ff ff          call   1260 <write@plt>
    2316:       48 8d 3d ed 0d 00 00    lea    rdi,[rip+0xded]        # 310a <_IO_stdin_used+0x10a>
    231d:       e8 6e ee ff ff          call   1190 <puts@plt>
    2322:       90                      nop
    2323:       5d                      pop    rbp
    2324:       c3                      ret

0000000000002325 <main>:
    2325:       f3 0f 1e fa             endbr64
    2329:       55                      push   rbp
    232a:       48 89 e5                mov    rbp,rsp
    232d:       48 81 ec f0 00 00 00    sub    rsp,0xf0
    2334:       89 bd 2c ff ff ff       mov    DWORD PTR [rbp-0xd4],edi
    233a:       48 89 b5 20 ff ff ff    mov    QWORD PTR [rbp-0xe0],rsi
    2341:       48 89 95 18 ff ff ff    mov    QWORD PTR [rbp-0xe8],rdx
    2348:       64 48 8b 04 25 28 00    mov    rax,QWORD PTR fs:0x28
    234f:       00 00 
    2351:       48 89 45 f8             mov    QWORD PTR [rbp-0x8],rax
    2355:       31 c0                   xor    eax,eax
    2357:       48 8b 05 e2 2c 00 00    mov    rax,QWORD PTR [rip+0x2ce2]        # 5040 <stdin@GLIBC_2.2.5>
    235e:       b9 00 00 00 00          mov    ecx,0x0
    2363:       ba 02 00 00 00          mov    edx,0x2
    2368:       be 00 00 00 00          mov    esi,0x0
    236d:       48 89 c7                mov    rdi,rax
    2370:       e8 3b ee ff ff          call   11b0 <setvbuf@plt>
    2375:       48 8b 05 cc 2c 00 00    mov    rax,QWORD PTR [rip+0x2ccc]        # 5048 <stdout@GLIBC_2.2.5>
    237c:       b9 00 00 00 00          mov    ecx,0x0
    2381:       ba 02 00 00 00          mov    edx,0x2
    2386:       be 00 00 00 00          mov    esi,0x0
    238b:       48 89 c7                mov    rdi,rax
    238e:       e8 1d ee ff ff          call   11b0 <setvbuf@plt>
    2393:       48 8d 3d 72 0d 00 00    lea    rdi,[rip+0xd72]        # 310c <_IO_stdin_used+0x10c>
    239a:       e8 f1 ed ff ff          call   1190 <puts@plt>
    239f:       48 8b 85 20 ff ff ff    mov    rax,QWORD PTR [rbp-0xe0]
    23a6:       48 8b 00                mov    rax,QWORD PTR [rax]
    23a9:       48 89 c6                mov    rsi,rax
    23ac:       48 8d 3d 5d 0d 00 00    lea    rdi,[rip+0xd5d]        # 3110 <_IO_stdin_used+0x110>
    23b3:       b8 00 00 00 00          mov    eax,0x0
    23b8:       e8 b3 ed ff ff          call   1170 <printf@plt>
    23bd:       48 8d 3d 48 0d 00 00    lea    rdi,[rip+0xd48]        # 310c <_IO_stdin_used+0x10c>
    23c4:       e8 c7 ed ff ff          call   1190 <puts@plt>
    23c9:       bf 0a 00 00 00          mov    edi,0xa
    23ce:       e8 ed ed ff ff          call   11c0 <putchar@plt>
    23d3:       48 8d 3d 4e 0d 00 00    lea    rdi,[rip+0xd4e]        # 3128 <_IO_stdin_used+0x128>
    23da:       e8 b1 ed ff ff          call   1190 <puts@plt>
    23df:       48 8d 3d ba 0d 00 00    lea    rdi,[rip+0xdba]        # 31a0 <_IO_stdin_used+0x1a0>
    23e6:       e8 a5 ed ff ff          call   1190 <puts@plt>
    23eb:       48 8d 3d 26 0e 00 00    lea    rdi,[rip+0xe26]        # 3218 <_IO_stdin_used+0x218>
    23f2:       e8 99 ed ff ff          call   1190 <puts@plt>
    23f7:       48 8d 3d 92 0e 00 00    lea    rdi,[rip+0xe92]        # 3290 <_IO_stdin_used+0x290>
    23fe:       e8 8d ed ff ff          call   1190 <puts@plt>
    2403:       48 8d 3d c6 0e 00 00    lea    rdi,[rip+0xec6]        # 32d0 <_IO_stdin_used+0x2d0>
    240a:       e8 81 ed ff ff          call   1190 <puts@plt>
    240f:       c7 85 40 ff ff ff 00    mov    DWORD PTR [rbp-0xc0],0x0
    2416:       00 00 00 
    2419:       48 8d 05 49 ef ff ff    lea    rax,[rip+0xffffffffffffef49]        # 1369 <bin_padding>
    2420:       48 25 00 f0 ff ff       and    rax,0xfffffffffffff000
    2426:       48 2d 00 10 00 00       sub    rax,0x1000
    242c:       48 89 85 58 ff ff ff    mov    QWORD PTR [rbp-0xa8],rax
    2433:       90                      nop
    2434:       8b 85 40 ff ff ff       mov    eax,DWORD PTR [rbp-0xc0]
    243a:       8d 50 01                lea    edx,[rax+0x1]
    243d:       89 95 40 ff ff ff       mov    DWORD PTR [rbp-0xc0],edx
    2443:       c1 e0 0c                shl    eax,0xc
    2446:       48 63 d0                movsxd rdx,eax
    2449:       48 8b 85 58 ff ff ff    mov    rax,QWORD PTR [rbp-0xa8]
    2450:       48 01 d0                add    rax,rdx
    2453:       ba 07 00 00 00          mov    edx,0x7
    2458:       be 00 10 00 00          mov    esi,0x1000
    245d:       48 89 c7                mov    rdi,rax
    2460:       e8 fb ec ff ff          call   1160 <mprotect@plt>
    2465:       85 c0                   test   eax,eax
    2467:       74 cb                   je     2434 <main+0x10f>
    2469:       c7 85 44 ff ff ff 00    mov    DWORD PTR [rbp-0xbc],0x0
    2470:       00 00 00 
    2473:       e9 ce 00 00 00          jmp    2546 <main+0x221>
    2478:       8b 85 44 ff ff ff       mov    eax,DWORD PTR [rbp-0xbc]
    247e:       83 c0 01                add    eax,0x1
    2481:       89 c6                   mov    esi,eax
    2483:       48 8d 3d a5 0e 00 00    lea    rdi,[rip+0xea5]        # 332f <_IO_stdin_used+0x32f>
    248a:       b8 00 00 00 00          mov    eax,0x0
    248f:       e8 dc ec ff ff          call   1170 <printf@plt>
    2494:       48 8d 3d a9 0e 00 00    lea    rdi,[rip+0xea9]        # 3344 <_IO_stdin_used+0x344>
    249b:       b8 00 00 00 00          mov    eax,0x0
    24a0:       e8 cb ec ff ff          call   1170 <printf@plt>
    24a5:       48 8d 85 3e ff ff ff    lea    rax,[rbp-0xc2]
    24ac:       48 89 c6                mov    rsi,rax
    24af:       48 8d 3d a7 0e 00 00    lea    rdi,[rip+0xea7]        # 335d <_IO_stdin_used+0x35d>
    24b6:       b8 00 00 00 00          mov    eax,0x0
    24bb:       e8 80 ed ff ff          call   1240 <__isoc99_scanf@plt>
    24c0:       48 8d 3d 9a 0e 00 00    lea    rdi,[rip+0xe9a]        # 3361 <_IO_stdin_used+0x361>
    24c7:       b8 00 00 00 00          mov    eax,0x0
    24cc:       e8 9f ec ff ff          call   1170 <printf@plt>
    24d1:       48 8d 85 3d ff ff ff    lea    rax,[rbp-0xc3]
    24d8:       48 89 c6                mov    rsi,rax
    24db:       48 8d 3d 91 0e 00 00    lea    rdi,[rip+0xe91]        # 3373 <_IO_stdin_used+0x373>
    24e2:       b8 00 00 00 00          mov    eax,0x0
    24e7:       e8 54 ed ff ff          call   1240 <__isoc99_scanf@plt>
    24ec:       0f b6 8d 3d ff ff ff    movzx  ecx,BYTE PTR [rbp-0xc3]
    24f3:       0f b7 85 3e ff ff ff    movzx  eax,WORD PTR [rbp-0xc2]
    24fa:       0f b7 d0                movzx  edx,ax
    24fd:       48 8b 85 58 ff ff ff    mov    rax,QWORD PTR [rbp-0xa8]
    2504:       48 01 d0                add    rax,rdx
    2507:       89 ca                   mov    edx,ecx
    2509:       88 10                   mov    BYTE PTR [rax],dl
    250b:       0f b6 85 3d ff ff ff    movzx  eax,BYTE PTR [rbp-0xc3]
    2512:       0f b6 c0                movzx  eax,al
    2515:       0f b7 95 3e ff ff ff    movzx  edx,WORD PTR [rbp-0xc2]
    251c:       0f b7 ca                movzx  ecx,dx
    251f:       48 8b 95 58 ff ff ff    mov    rdx,QWORD PTR [rbp-0xa8]
    2526:       48 01 d1                add    rcx,rdx
    2529:       89 c2                   mov    edx,eax
    252b:       48 89 ce                mov    rsi,rcx
    252e:       48 8d 3d 43 0e 00 00    lea    rdi,[rip+0xe43]        # 3378 <_IO_stdin_used+0x378>
    2535:       b8 00 00 00 00          mov    eax,0x0
    253a:       e8 31 ec ff ff          call   1170 <printf@plt>
    253f:       83 85 44 ff ff ff 01    add    DWORD PTR [rbp-0xbc],0x1
    2546:       83 bd 44 ff ff ff 04    cmp    DWORD PTR [rbp-0xbc],0x4
    254d:       0f 8e 25 ff ff ff       jle    2478 <main+0x153>
    2553:       48 c7 45 d0 00 00 00    mov    QWORD PTR [rbp-0x30],0x0
    255a:       00 
    255b:       48 c7 45 d8 00 00 00    mov    QWORD PTR [rbp-0x28],0x0
    2562:       00 
    2563:       48 c7 45 e0 00 00 00    mov    QWORD PTR [rbp-0x20],0x0
    256a:       00 
    256b:       66 c7 45 e8 00 00       mov    WORD PTR [rbp-0x18],0x0
    2571:       48 8d 3d 28 0e 00 00    lea    rdi,[rip+0xe28]        # 33a0 <_IO_stdin_used+0x3a0>
    2578:       e8 13 ec ff ff          call   1190 <puts@plt>
    257d:       48 8d 45 d0             lea    rax,[rbp-0x30]
    2581:       ba 19 00 00 00          mov    edx,0x19
    2586:       48 89 c6                mov    rsi,rax
    2589:       bf 00 00 00 00          mov    edi,0x0
    258e:       e8 3d ec ff ff          call   11d0 <read@plt>
    2593:       48 8d 3d 2a 0e 00 00    lea    rdi,[rip+0xe2a]        # 33c4 <_IO_stdin_used+0x3c4>
    259a:       e8 f1 eb ff ff          call   1190 <puts@plt>
    259f:       bf 09 00 00 00          mov    edi,0x9
    25a4:       e8 17 ec ff ff          call   11c0 <putchar@plt>
    25a9:       c7 85 48 ff ff ff 00    mov    DWORD PTR [rbp-0xb8],0x0
    25b0:       00 00 00 
    25b3:       eb 2a                   jmp    25df <main+0x2ba>
    25b5:       8b 85 48 ff ff ff       mov    eax,DWORD PTR [rbp-0xb8]
    25bb:       48 98                   cdqe
    25bd:       0f b6 44 05 d0          movzx  eax,BYTE PTR [rbp+rax*1-0x30]
    25c2:       0f b6 c0                movzx  eax,al
    25c5:       89 c6                   mov    esi,eax
    25c7:       48 8d 3d 06 0e 00 00    lea    rdi,[rip+0xe06]        # 33d4 <_IO_stdin_used+0x3d4>
    25ce:       b8 00 00 00 00          mov    eax,0x0
    25d3:       e8 98 eb ff ff          call   1170 <printf@plt>
    25d8:       83 85 48 ff ff ff 01    add    DWORD PTR [rbp-0xb8],0x1
    25df:       83 bd 48 ff ff ff 18    cmp    DWORD PTR [rbp-0xb8],0x18
    25e6:       7e cd                   jle    25b5 <main+0x290>
    25e8:       48 8d 3d 1b 0b 00 00    lea    rdi,[rip+0xb1b]        # 310a <_IO_stdin_used+0x10a>
    25ef:       e8 9c eb ff ff          call   1190 <puts@plt>
    25f4:       48 8d 3d e5 0d 00 00    lea    rdi,[rip+0xde5]        # 33e0 <_IO_stdin_used+0x3e0>
    25fb:       e8 90 eb ff ff          call   1190 <puts@plt>
    2600:       48 8d 85 60 ff ff ff    lea    rax,[rbp-0xa0]
    2607:       48 89 c7                mov    rdi,rax
    260a:       e8 21 ec ff ff          call   1230 <MD5_Init@plt>
    260f:       48 8d 4d d0             lea    rcx,[rbp-0x30]
    2613:       48 8d 85 60 ff ff ff    lea    rax,[rbp-0xa0]
    261a:       ba 19 00 00 00          mov    edx,0x19
    261f:       48 89 ce                mov    rsi,rcx
    2622:       48 89 c7                mov    rdi,rax
    2625:       e8 d6 eb ff ff          call   1200 <MD5_Update@plt>
    262a:       48 8d 95 60 ff ff ff    lea    rdx,[rbp-0xa0]
    2631:       48 8d 45 c0             lea    rax,[rbp-0x40]
    2635:       48 89 d6                mov    rsi,rdx
    2638:       48 89 c7                mov    rdi,rax
    263b:       e8 b0 eb ff ff          call   11f0 <MD5_Final@plt>
    2640:       48 8d 45 d0             lea    rax,[rbp-0x30]
    2644:       ba 19 00 00 00          mov    edx,0x19
    2649:       be 00 00 00 00          mov    esi,0x0
    264e:       48 89 c7                mov    rdi,rax
    2651:       e8 2a eb ff ff          call   1180 <memset@plt>
    2656:       48 8b 45 c0             mov    rax,QWORD PTR [rbp-0x40]
    265a:       48 8b 55 c8             mov    rdx,QWORD PTR [rbp-0x38]
    265e:       48 89 45 d0             mov    QWORD PTR [rbp-0x30],rax
    2662:       48 89 55 d8             mov    QWORD PTR [rbp-0x28],rdx
    2666:       48 8d 3d db 0d 00 00    lea    rdi,[rip+0xddb]        # 3448 <_IO_stdin_used+0x448>
    266d:       e8 1e eb ff ff          call   1190 <puts@plt>
    2672:       bf 09 00 00 00          mov    edi,0x9
    2677:       e8 44 eb ff ff          call   11c0 <putchar@plt>
    267c:       c7 85 4c ff ff ff 00    mov    DWORD PTR [rbp-0xb4],0x0
    2683:       00 00 00 
    2686:       eb 2a                   jmp    26b2 <main+0x38d>
    2688:       8b 85 4c ff ff ff       mov    eax,DWORD PTR [rbp-0xb4]
    268e:       48 98                   cdqe
    2690:       0f b6 44 05 d0          movzx  eax,BYTE PTR [rbp+rax*1-0x30]
    2695:       0f b6 c0                movzx  eax,al
    2698:       89 c6                   mov    esi,eax
    269a:       48 8d 3d 33 0d 00 00    lea    rdi,[rip+0xd33]        # 33d4 <_IO_stdin_used+0x3d4>
    26a1:       b8 00 00 00 00          mov    eax,0x0
    26a6:       e8 c5 ea ff ff          call   1170 <printf@plt>
    26ab:       83 85 4c ff ff ff 01    add    DWORD PTR [rbp-0xb4],0x1
    26b2:       83 bd 4c ff ff ff 18    cmp    DWORD PTR [rbp-0xb4],0x18
    26b9:       7e cd                   jle    2688 <main+0x363>
    26bb:       48 8d 3d 48 0a 00 00    lea    rdi,[rip+0xa48]        # 310a <_IO_stdin_used+0x10a>
    26c2:       e8 c9 ea ff ff          call   1190 <puts@plt>
    26c7:       48 8d 3d a2 0d 00 00    lea    rdi,[rip+0xda2]        # 3470 <_IO_stdin_used+0x470>
    26ce:       e8 bd ea ff ff          call   1190 <puts@plt>
    26d3:       48 8d 3d ee 0d 00 00    lea    rdi,[rip+0xdee]        # 34c8 <_IO_stdin_used+0x4c8>
    26da:       e8 b1 ea ff ff          call   1190 <puts@plt>
    26df:       bf 09 00 00 00          mov    edi,0x9
    26e4:       e8 d7 ea ff ff          call   11c0 <putchar@plt>
    26e9:       c7 85 50 ff ff ff 00    mov    DWORD PTR [rbp-0xb0],0x0
    26f0:       00 00 00 
    26f3:       eb 2a                   jmp    271f <main+0x3fa>
    26f5:       8b 85 50 ff ff ff       mov    eax,DWORD PTR [rbp-0xb0]
    26fb:       48 98                   cdqe
    26fd:       0f b6 44 05 d0          movzx  eax,BYTE PTR [rbp+rax*1-0x30]
    2702:       0f b6 c0                movzx  eax,al
    2705:       89 c6                   mov    esi,eax
    2707:       48 8d 3d c6 0c 00 00    lea    rdi,[rip+0xcc6]        # 33d4 <_IO_stdin_used+0x3d4>
    270e:       b8 00 00 00 00          mov    eax,0x0
    2713:       e8 58 ea ff ff          call   1170 <printf@plt>
    2718:       83 85 50 ff ff ff 01    add    DWORD PTR [rbp-0xb0],0x1
    271f:       83 bd 50 ff ff ff 18    cmp    DWORD PTR [rbp-0xb0],0x18
    2726:       7e cd                   jle    26f5 <main+0x3d0>
    2728:       48 8d 3d db 09 00 00    lea    rdi,[rip+0x9db]        # 310a <_IO_stdin_used+0x10a>
    272f:       e8 5c ea ff ff          call   1190 <puts@plt>
    2734:       48 8d 3d ae 0d 00 00    lea    rdi,[rip+0xdae]        # 34e9 <_IO_stdin_used+0x4e9>
    273b:       e8 50 ea ff ff          call   1190 <puts@plt>
    2740:       bf 09 00 00 00          mov    edi,0x9
    2745:       e8 76 ea ff ff          call   11c0 <putchar@plt>
    274a:       c7 85 54 ff ff ff 00    mov    DWORD PTR [rbp-0xac],0x0
    2751:       00 00 00 
    2754:       eb 30                   jmp    2786 <main+0x461>
    2756:       8b 85 54 ff ff ff       mov    eax,DWORD PTR [rbp-0xac]
    275c:       48 98                   cdqe
    275e:       48 8d 15 ab 28 00 00    lea    rdx,[rip+0x28ab]        # 5010 <EXPECTED_RESULT>
    2765:       0f b6 04 10             movzx  eax,BYTE PTR [rax+rdx*1]
    2769:       0f b6 c0                movzx  eax,al
    276c:       89 c6                   mov    esi,eax
    276e:       48 8d 3d 5f 0c 00 00    lea    rdi,[rip+0xc5f]        # 33d4 <_IO_stdin_used+0x3d4>
    2775:       b8 00 00 00 00          mov    eax,0x0
    277a:       e8 f1 e9 ff ff          call   1170 <printf@plt>
    277f:       83 85 54 ff ff ff 01    add    DWORD PTR [rbp-0xac],0x1
    2786:       83 bd 54 ff ff ff 18    cmp    DWORD PTR [rbp-0xac],0x18
    278d:       7e c7                   jle    2756 <main+0x431>
    278f:       48 8d 3d 74 09 00 00    lea    rdi,[rip+0x974]        # 310a <_IO_stdin_used+0x10a>
    2796:       e8 f5 e9 ff ff          call   1190 <puts@plt>
    279b:       48 8d 3d 5e 0d 00 00    lea    rdi,[rip+0xd5e]        # 3500 <_IO_stdin_used+0x500>
    27a2:       e8 e9 e9 ff ff          call   1190 <puts@plt>
    27a7:       48 8d 45 d0             lea    rax,[rbp-0x30]
    27ab:       ba 19 00 00 00          mov    edx,0x19
    27b0:       48 8d 35 59 28 00 00    lea    rsi,[rip+0x2859]        # 5010 <EXPECTED_RESULT>
    27b7:       48 89 c7                mov    rdi,rax
    27ba:       e8 91 ea ff ff          call   1250 <memcmp@plt>
    27bf:       85 c0                   test   eax,eax
    27c1:       75 14                   jne    27d7 <main+0x4b2>
    27c3:       b8 00 00 00 00          mov    eax,0x0
    27c8:       e8 51 fa ff ff          call   221e <win>
    27cd:       bf 00 00 00 00          mov    edi,0x0
    27d2:       e8 c9 e9 ff ff          call   11a0 <exit@plt>
    27d7:       48 8d 3d 46 0d 00 00    lea    rdi,[rip+0xd46]        # 3524 <_IO_stdin_used+0x524>
    27de:       e8 ad e9 ff ff          call   1190 <puts@plt>
    27e3:       bf 01 00 00 00          mov    edi,0x1
    27e8:       e8 b3 e9 ff ff          call   11a0 <exit@plt>
    27ed:       0f 1f 00                nop    DWORD PTR [rax]

00000000000027f0 <__libc_csu_init>:
    27f0:       f3 0f 1e fa             endbr64
    27f4:       41 57                   push   r15
    27f6:       4c 8d 3d 23 25 00 00    lea    r15,[rip+0x2523]        # 4d20 <__frame_dummy_init_array_entry>
    27fd:       41 56                   push   r14
    27ff:       49 89 d6                mov    r14,rdx
    2802:       41 55                   push   r13
    2804:       49 89 f5                mov    r13,rsi
    2807:       41 54                   push   r12
    2809:       41 89 fc                mov    r12d,edi
    280c:       55                      push   rbp
    280d:       48 8d 2d 14 25 00 00    lea    rbp,[rip+0x2514]        # 4d28 <__do_global_dtors_aux_fini_array_entry>
    2814:       53                      push   rbx
    2815:       4c 29 fd                sub    rbp,r15
    2818:       48 83 ec 08             sub    rsp,0x8
    281c:       e8 df e7 ff ff          call   1000 <_init>
    2821:       48 c1 fd 03             sar    rbp,0x3
    2825:       74 1f                   je     2846 <__libc_csu_init+0x56>
    2827:       31 db                   xor    ebx,ebx
    2829:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]
    2830:       4c 89 f2                mov    rdx,r14
    2833:       4c 89 ee                mov    rsi,r13
    2836:       44 89 e7                mov    edi,r12d
    2839:       41 ff 14 df             call   QWORD PTR [r15+rbx*8]
    283d:       48 83 c3 01             add    rbx,0x1
    2841:       48 39 dd                cmp    rbp,rbx
    2844:       75 ea                   jne    2830 <__libc_csu_init+0x40>
    2846:       48 83 c4 08             add    rsp,0x8
    284a:       5b                      pop    rbx
    284b:       5d                      pop    rbp
    284c:       41 5c                   pop    r12
    284e:       41 5d                   pop    r13
    2850:       41 5e                   pop    r14
    2852:       41 5f                   pop    r15
    2854:       c3                      ret
    2855:       66 66 2e 0f 1f 84 00    data16 cs nop WORD PTR [rax+rax*1+0x0]
    285c:       00 00 00 00 

0000000000002860 <__libc_csu_fini>:
    2860:       f3 0f 1e fa             endbr64
    2864:       c3                      ret

Disassembly of section .fini:

0000000000002868 <_fini>:
    2868:       f3 0f 1e fa             endbr64
    286c:       48 83 ec 08             sub    rsp,0x8
    2870:       48 83 c4 08             add    rsp,0x8
    2874:       c3                      ret
```
- The expected key is located at `0x5010`. 
- `memcmp` is used to compare the expected key with the user input. If the result is 0 (the keys match), the program will call the `win` function, which will give us the flag.
- These lines are of our interest:
```
    27ba:       e8 91 ea ff ff          call   1250 <memcmp@plt>
    27bf:       85 c0                   test   eax,eax
    27c1:       75 14                   jne    27d7 <main+0x4b2>
    27c3:       b8 00 00 00 00          mov    eax,0x0
    27c8:       e8 51 fa ff ff          call   221e <win>
```
- If we bypass the `jne` instruction, the `win` function will be called (even if the keys don't match) and we will get the flag.
- I chatted a bit with an LLM, and figured out a way to patch the binary to bypass the `jne` instruction:
  - `27c1` has `75` which is the opcode for `jne`.
  - `27c2` has `14` which is the offset for the `jne` instruction (0x14 is 20. The `jne` instruction will go to `27d7` if the keys don't match. The `jne` instruction jumps an offset from the **next** instruction. So `27d7 - 27c3 = 0x14 or 20 bytes jump`).
  - As can be seen in the disassembly: `2322:       90                      nop`, the opcode for `nop` is `90`.
  - So if I replace the `jne` instruction and the offset with the opcode for `nop` (90), this will make the `jne` instruction do nothing and the program will call the `win` function regardless of the keys matching or not.
- I ran the program with these patches:
```
###
### Welcome to ./babyrev-level-9-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Unfortunately for you, the license key cannot be reversed. You'll have to crack this program.

Changing byte 1/5.
Offset (hex) to change: 27c1
New value (hex): 90
The byte has been changed: *0x56d914bb07c1 = 90.
Changing byte 2/5.
Offset (hex) to change: 27c2
New value (hex): 90
The byte has been changed: *0x56d914bb07c2 = 90.
Changing byte 3/5.
Offset (hex) to change: .
New value (hex): The byte has been changed: *0x56d914bb07c2 = 90.
Changing byte 4/5.
Offset (hex) to change: New value (hex): The byte has been changed: *0x56d914bb07c2 = 90.
Changing byte 5/5.
Offset (hex) to change: New value (hex): The byte has been changed: *0x56d914bb07c2 = 90.
Ready to receive your license key!

Initial input:

        0a 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

This challenge is now mangling your input using the `md5` mangler. This mangler cannot be reversed.

This mangled your input, resulting in:

        29 e5 52 84 34 07 75 cf b6 eb 07 18 f6 4f 73 b9 00 00 00 00 00 00 00 00 00 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        29 e5 52 84 34 07 75 cf b6 eb 07 18 f6 4f 73 b9 00 00 00 00 00 00 00 00 00 

Expected result:

        0f c8 33 ac 53 52 fe e2 94 2e a4 5b 27 4e d1 a5 00 00 00 00 00 00 00 00 00 

Checking the received license key!

You win! Here is your flag:
pwn.college{UaYoWFbo_PLMiDcS36tx3vUX3rK.01N2IDL5QTO0czW}
```
- (I just gave a `.` as the offset for the 3rd byte change, because patching 2 bytes was sufficient to bypass the `jne` instruction and get the flag. Had this resulted in an error, I could've also just given `nop` opcodes to already existing `nop` instructions or something.)
- Flag: `pwn.college{UaYoWFbo_PLMiDcS36tx3vUX3rK.01N2IDL5QTO0czW}`