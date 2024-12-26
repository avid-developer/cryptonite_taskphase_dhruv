# level10.0
## Description
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key. This challenge allows you to patch 1 byte in the binary.
## Solution
- The executable program's name is `babyrev-level-10-0`
- I ran `objdump -d -M intel babyrev-level-10-0` to disassemble the binary and got the following:
```
babyrev-level-10-0:     file format elf64-x86-64


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
    1293:       4c 8d 05 56 0e 00 00    lea    r8,[rip+0xe56]        # 20f0 <__libc_csu_fini>
    129a:       48 8d 0d df 0d 00 00    lea    rcx,[rip+0xddf]        # 2080 <__libc_csu_init>
    12a1:       48 8d 3d 06 09 00 00    lea    rdi,[rip+0x906]        # 1bae <main>
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
...
    1aa3:       90                      nop
    1aa4:       90                      nop
    1aa5:       5d                      pop    rbp
    1aa6:       c3                      ret

0000000000001aa7 <win>:
    1aa7:       f3 0f 1e fa             endbr64
    1aab:       55                      push   rbp
    1aac:       48 89 e5                mov    rbp,rsp
    1aaf:       48 8d 3d 52 15 00 00    lea    rdi,[rip+0x1552]        # 3008 <_IO_stdin_used+0x8>
    1ab6:       e8 d5 f6 ff ff          call   1190 <puts@plt>
    1abb:       be 00 00 00 00          mov    esi,0x0
    1ac0:       48 8d 3d 5d 15 00 00    lea    rdi,[rip+0x155d]        # 3024 <_IO_stdin_used+0x24>
    1ac7:       b8 00 00 00 00          mov    eax,0x0
    1acc:       e8 9f f7 ff ff          call   1270 <open@plt>
    1ad1:       89 05 89 35 00 00       mov    DWORD PTR [rip+0x3589],eax        # 5060 <flag_fd.5757>
    1ad7:       8b 05 83 35 00 00       mov    eax,DWORD PTR [rip+0x3583]        # 5060 <flag_fd.5757>
    1add:       85 c0                   test   eax,eax
    1adf:       79 4d                   jns    1b2e <win+0x87>
    1ae1:       e8 3a f7 ff ff          call   1220 <__errno_location@plt>
    1ae6:       8b 00                   mov    eax,DWORD PTR [rax]
    1ae8:       89 c7                   mov    edi,eax
    1aea:       e8 21 f7 ff ff          call   1210 <strerror@plt>
    1aef:       48 89 c6                mov    rsi,rax
    1af2:       48 8d 3d 37 15 00 00    lea    rdi,[rip+0x1537]        # 3030 <_IO_stdin_used+0x30>
    1af9:       b8 00 00 00 00          mov    eax,0x0
    1afe:       e8 6d f6 ff ff          call   1170 <printf@plt>
    1b03:       e8 d8 f6 ff ff          call   11e0 <geteuid@plt>
    1b08:       85 c0                   test   eax,eax
    1b0a:       74 18                   je     1b24 <win+0x7d>
    1b0c:       48 8d 3d 4d 15 00 00    lea    rdi,[rip+0x154d]        # 3060 <_IO_stdin_used+0x60>
    1b13:       e8 78 f6 ff ff          call   1190 <puts@plt>
    1b18:       48 8d 3d 69 15 00 00    lea    rdi,[rip+0x1569]        # 3088 <_IO_stdin_used+0x88>
    1b1f:       e8 6c f6 ff ff          call   1190 <puts@plt>
    1b24:       bf ff ff ff ff          mov    edi,0xffffffff
    1b29:       e8 72 f6 ff ff          call   11a0 <exit@plt>
    1b2e:       8b 05 2c 35 00 00       mov    eax,DWORD PTR [rip+0x352c]        # 5060 <flag_fd.5757>
    1b34:       ba 00 01 00 00          mov    edx,0x100
    1b39:       48 8d 35 40 35 00 00    lea    rsi,[rip+0x3540]        # 5080 <flag.5756>
    1b40:       89 c7                   mov    edi,eax
    1b42:       e8 89 f6 ff ff          call   11d0 <read@plt>
    1b47:       89 05 33 36 00 00       mov    DWORD PTR [rip+0x3633],eax        # 5180 <flag_length.5758>
    1b4d:       8b 05 2d 36 00 00       mov    eax,DWORD PTR [rip+0x362d]        # 5180 <flag_length.5758>
    1b53:       85 c0                   test   eax,eax
    1b55:       7f 2c                   jg     1b83 <win+0xdc>
    1b57:       e8 c4 f6 ff ff          call   1220 <__errno_location@plt>
    1b5c:       8b 00                   mov    eax,DWORD PTR [rax]
    1b5e:       89 c7                   mov    edi,eax
    1b60:       e8 ab f6 ff ff          call   1210 <strerror@plt>
    1b65:       48 89 c6                mov    rsi,rax
    1b68:       48 8d 3d 71 15 00 00    lea    rdi,[rip+0x1571]        # 30e0 <_IO_stdin_used+0xe0>
    1b6f:       b8 00 00 00 00          mov    eax,0x0
    1b74:       e8 f7 f5 ff ff          call   1170 <printf@plt>
    1b79:       bf ff ff ff ff          mov    edi,0xffffffff
    1b7e:       e8 1d f6 ff ff          call   11a0 <exit@plt>
    1b83:       8b 05 f7 35 00 00       mov    eax,DWORD PTR [rip+0x35f7]        # 5180 <flag_length.5758>
    1b89:       48 98                   cdqe
    1b8b:       48 89 c2                mov    rdx,rax
    1b8e:       48 8d 35 eb 34 00 00    lea    rsi,[rip+0x34eb]        # 5080 <flag.5756>
    1b95:       bf 01 00 00 00          mov    edi,0x1
    1b9a:       e8 c1 f6 ff ff          call   1260 <write@plt>
    1b9f:       48 8d 3d 64 15 00 00    lea    rdi,[rip+0x1564]        # 310a <_IO_stdin_used+0x10a>
    1ba6:       e8 e5 f5 ff ff          call   1190 <puts@plt>
    1bab:       90                      nop
    1bac:       5d                      pop    rbp
    1bad:       c3                      ret

0000000000001bae <main>:
    1bae:       f3 0f 1e fa             endbr64
    1bb2:       55                      push   rbp
    1bb3:       48 89 e5                mov    rbp,rsp
    1bb6:       48 81 ec f0 00 00 00    sub    rsp,0xf0
    1bbd:       89 bd 2c ff ff ff       mov    DWORD PTR [rbp-0xd4],edi
    1bc3:       48 89 b5 20 ff ff ff    mov    QWORD PTR [rbp-0xe0],rsi
    1bca:       48 89 95 18 ff ff ff    mov    QWORD PTR [rbp-0xe8],rdx
    1bd1:       64 48 8b 04 25 28 00    mov    rax,QWORD PTR fs:0x28
    1bd8:       00 00 
    1bda:       48 89 45 f8             mov    QWORD PTR [rbp-0x8],rax
    1bde:       31 c0                   xor    eax,eax
    1be0:       48 8b 05 59 34 00 00    mov    rax,QWORD PTR [rip+0x3459]        # 5040 <stdin@GLIBC_2.2.5>
    1be7:       b9 00 00 00 00          mov    ecx,0x0
    1bec:       ba 02 00 00 00          mov    edx,0x2
    1bf1:       be 00 00 00 00          mov    esi,0x0
    1bf6:       48 89 c7                mov    rdi,rax
    1bf9:       e8 b2 f5 ff ff          call   11b0 <setvbuf@plt>
    1bfe:       48 8b 05 43 34 00 00    mov    rax,QWORD PTR [rip+0x3443]        # 5048 <stdout@GLIBC_2.2.5>
    1c05:       b9 00 00 00 00          mov    ecx,0x0
    1c0a:       ba 02 00 00 00          mov    edx,0x2
    1c0f:       be 00 00 00 00          mov    esi,0x0
    1c14:       48 89 c7                mov    rdi,rax
    1c17:       e8 94 f5 ff ff          call   11b0 <setvbuf@plt>
    1c1c:       48 8d 3d e9 14 00 00    lea    rdi,[rip+0x14e9]        # 310c <_IO_stdin_used+0x10c>
    1c23:       e8 68 f5 ff ff          call   1190 <puts@plt>
    1c28:       48 8b 85 20 ff ff ff    mov    rax,QWORD PTR [rbp-0xe0]
    1c2f:       48 8b 00                mov    rax,QWORD PTR [rax]
    1c32:       48 89 c6                mov    rsi,rax
    1c35:       48 8d 3d d4 14 00 00    lea    rdi,[rip+0x14d4]        # 3110 <_IO_stdin_used+0x110>
    1c3c:       b8 00 00 00 00          mov    eax,0x0
    1c41:       e8 2a f5 ff ff          call   1170 <printf@plt>
    1c46:       48 8d 3d bf 14 00 00    lea    rdi,[rip+0x14bf]        # 310c <_IO_stdin_used+0x10c>
    1c4d:       e8 3e f5 ff ff          call   1190 <puts@plt>
    1c52:       bf 0a 00 00 00          mov    edi,0xa
    1c57:       e8 64 f5 ff ff          call   11c0 <putchar@plt>
    1c5c:       48 8d 3d c5 14 00 00    lea    rdi,[rip+0x14c5]        # 3128 <_IO_stdin_used+0x128>
    1c63:       e8 28 f5 ff ff          call   1190 <puts@plt>
    1c68:       48 8d 3d 31 15 00 00    lea    rdi,[rip+0x1531]        # 31a0 <_IO_stdin_used+0x1a0>
    1c6f:       e8 1c f5 ff ff          call   1190 <puts@plt>
    1c74:       48 8d 3d 9d 15 00 00    lea    rdi,[rip+0x159d]        # 3218 <_IO_stdin_used+0x218>
    1c7b:       e8 10 f5 ff ff          call   1190 <puts@plt>
    1c80:       48 8d 3d 09 16 00 00    lea    rdi,[rip+0x1609]        # 3290 <_IO_stdin_used+0x290>
    1c87:       e8 04 f5 ff ff          call   1190 <puts@plt>
    1c8c:       48 8d 3d 3d 16 00 00    lea    rdi,[rip+0x163d]        # 32d0 <_IO_stdin_used+0x2d0>
    1c93:       e8 f8 f4 ff ff          call   1190 <puts@plt>
    1c98:       c7 85 40 ff ff ff 00    mov    DWORD PTR [rbp-0xc0],0x0
    1c9f:       00 00 00 
    1ca2:       48 8d 05 c0 f6 ff ff    lea    rax,[rip+0xfffffffffffff6c0]        # 1369 <bin_padding>
    1ca9:       48 25 00 f0 ff ff       and    rax,0xfffffffffffff000
    1caf:       48 2d 00 10 00 00       sub    rax,0x1000
    1cb5:       48 89 85 58 ff ff ff    mov    QWORD PTR [rbp-0xa8],rax
    1cbc:       90                      nop
    1cbd:       8b 85 40 ff ff ff       mov    eax,DWORD PTR [rbp-0xc0]
    1cc3:       8d 50 01                lea    edx,[rax+0x1]
    1cc6:       89 95 40 ff ff ff       mov    DWORD PTR [rbp-0xc0],edx
    1ccc:       c1 e0 0c                shl    eax,0xc
    1ccf:       48 63 d0                movsxd rdx,eax
    1cd2:       48 8b 85 58 ff ff ff    mov    rax,QWORD PTR [rbp-0xa8]
    1cd9:       48 01 d0                add    rax,rdx
    1cdc:       ba 07 00 00 00          mov    edx,0x7
    1ce1:       be 00 10 00 00          mov    esi,0x1000
    1ce6:       48 89 c7                mov    rdi,rax
    1ce9:       e8 72 f4 ff ff          call   1160 <mprotect@plt>
    1cee:       85 c0                   test   eax,eax
    1cf0:       74 cb                   je     1cbd <main+0x10f>
    1cf2:       c7 85 44 ff ff ff 00    mov    DWORD PTR [rbp-0xbc],0x0
    1cf9:       00 00 00 
    1cfc:       e9 ce 00 00 00          jmp    1dcf <main+0x221>
    1d01:       8b 85 44 ff ff ff       mov    eax,DWORD PTR [rbp-0xbc]
    1d07:       83 c0 01                add    eax,0x1
    1d0a:       89 c6                   mov    esi,eax
    1d0c:       48 8d 3d 1c 16 00 00    lea    rdi,[rip+0x161c]        # 332f <_IO_stdin_used+0x32f>
    1d13:       b8 00 00 00 00          mov    eax,0x0
    1d18:       e8 53 f4 ff ff          call   1170 <printf@plt>
    1d1d:       48 8d 3d 20 16 00 00    lea    rdi,[rip+0x1620]        # 3344 <_IO_stdin_used+0x344>
    1d24:       b8 00 00 00 00          mov    eax,0x0
    1d29:       e8 42 f4 ff ff          call   1170 <printf@plt>
    1d2e:       48 8d 85 3e ff ff ff    lea    rax,[rbp-0xc2]
    1d35:       48 89 c6                mov    rsi,rax
    1d38:       48 8d 3d 1e 16 00 00    lea    rdi,[rip+0x161e]        # 335d <_IO_stdin_used+0x35d>
    1d3f:       b8 00 00 00 00          mov    eax,0x0
    1d44:       e8 f7 f4 ff ff          call   1240 <__isoc99_scanf@plt>
    1d49:       48 8d 3d 11 16 00 00    lea    rdi,[rip+0x1611]        # 3361 <_IO_stdin_used+0x361>
    1d50:       b8 00 00 00 00          mov    eax,0x0
    1d55:       e8 16 f4 ff ff          call   1170 <printf@plt>
    1d5a:       48 8d 85 3d ff ff ff    lea    rax,[rbp-0xc3]
    1d61:       48 89 c6                mov    rsi,rax
    1d64:       48 8d 3d 08 16 00 00    lea    rdi,[rip+0x1608]        # 3373 <_IO_stdin_used+0x373>
    1d6b:       b8 00 00 00 00          mov    eax,0x0
    1d70:       e8 cb f4 ff ff          call   1240 <__isoc99_scanf@plt>
    1d75:       0f b6 8d 3d ff ff ff    movzx  ecx,BYTE PTR [rbp-0xc3]
    1d7c:       0f b7 85 3e ff ff ff    movzx  eax,WORD PTR [rbp-0xc2]
    1d83:       0f b7 d0                movzx  edx,ax
    1d86:       48 8b 85 58 ff ff ff    mov    rax,QWORD PTR [rbp-0xa8]
    1d8d:       48 01 d0                add    rax,rdx
    1d90:       89 ca                   mov    edx,ecx
    1d92:       88 10                   mov    BYTE PTR [rax],dl
    1d94:       0f b6 85 3d ff ff ff    movzx  eax,BYTE PTR [rbp-0xc3]
    1d9b:       0f b6 c0                movzx  eax,al
    1d9e:       0f b7 95 3e ff ff ff    movzx  edx,WORD PTR [rbp-0xc2]
    1da5:       0f b7 ca                movzx  ecx,dx
    1da8:       48 8b 95 58 ff ff ff    mov    rdx,QWORD PTR [rbp-0xa8]
    1daf:       48 01 d1                add    rcx,rdx
    1db2:       89 c2                   mov    edx,eax
    1db4:       48 89 ce                mov    rsi,rcx
    1db7:       48 8d 3d ba 15 00 00    lea    rdi,[rip+0x15ba]        # 3378 <_IO_stdin_used+0x378>
    1dbe:       b8 00 00 00 00          mov    eax,0x0
    1dc3:       e8 a8 f3 ff ff          call   1170 <printf@plt>
    1dc8:       83 85 44 ff ff ff 01    add    DWORD PTR [rbp-0xbc],0x1
    1dcf:       83 bd 44 ff ff ff 00    cmp    DWORD PTR [rbp-0xbc],0x0
    1dd6:       0f 8e 25 ff ff ff       jle    1d01 <main+0x153>
    1ddc:       48 c7 45 d0 00 00 00    mov    QWORD PTR [rbp-0x30],0x0
    1de3:       00 
    1de4:       48 c7 45 d8 00 00 00    mov    QWORD PTR [rbp-0x28],0x0
    1deb:       00 
    1dec:       48 c7 45 e0 00 00 00    mov    QWORD PTR [rbp-0x20],0x0
    1df3:       00 
    1df4:       66 c7 45 e8 00 00       mov    WORD PTR [rbp-0x18],0x0
    1dfa:       c6 45 ea 00             mov    BYTE PTR [rbp-0x16],0x0
    1dfe:       48 8d 3d 9b 15 00 00    lea    rdi,[rip+0x159b]        # 33a0 <_IO_stdin_used+0x3a0>
    1e05:       e8 86 f3 ff ff          call   1190 <puts@plt>
    1e0a:       48 8d 45 d0             lea    rax,[rbp-0x30]
    1e0e:       ba 1a 00 00 00          mov    edx,0x1a
    1e13:       48 89 c6                mov    rsi,rax
    1e16:       bf 00 00 00 00          mov    edi,0x0
    1e1b:       e8 b0 f3 ff ff          call   11d0 <read@plt>
    1e20:       48 8d 3d 9d 15 00 00    lea    rdi,[rip+0x159d]        # 33c4 <_IO_stdin_used+0x3c4>
    1e27:       e8 64 f3 ff ff          call   1190 <puts@plt>
    1e2c:       bf 09 00 00 00          mov    edi,0x9
    1e31:       e8 8a f3 ff ff          call   11c0 <putchar@plt>
    1e36:       c7 85 48 ff ff ff 00    mov    DWORD PTR [rbp-0xb8],0x0
    1e3d:       00 00 00 
    1e40:       eb 2a                   jmp    1e6c <main+0x2be>
    1e42:       8b 85 48 ff ff ff       mov    eax,DWORD PTR [rbp-0xb8]
    1e48:       48 98                   cdqe
    1e4a:       0f b6 44 05 d0          movzx  eax,BYTE PTR [rbp+rax*1-0x30]
    1e4f:       0f b6 c0                movzx  eax,al
    1e52:       89 c6                   mov    esi,eax
    1e54:       48 8d 3d 79 15 00 00    lea    rdi,[rip+0x1579]        # 33d4 <_IO_stdin_used+0x3d4>
    1e5b:       b8 00 00 00 00          mov    eax,0x0
    1e60:       e8 0b f3 ff ff          call   1170 <printf@plt>
    1e65:       83 85 48 ff ff ff 01    add    DWORD PTR [rbp-0xb8],0x1
    1e6c:       83 bd 48 ff ff ff 19    cmp    DWORD PTR [rbp-0xb8],0x19
    1e73:       7e cd                   jle    1e42 <main+0x294>
    1e75:       48 8d 3d 8e 12 00 00    lea    rdi,[rip+0x128e]        # 310a <_IO_stdin_used+0x10a>
    1e7c:       e8 0f f3 ff ff          call   1190 <puts@plt>
    1e81:       48 8d 3d 58 15 00 00    lea    rdi,[rip+0x1558]        # 33e0 <_IO_stdin_used+0x3e0>
    1e88:       e8 03 f3 ff ff          call   1190 <puts@plt>
    1e8d:       48 8d 85 60 ff ff ff    lea    rax,[rbp-0xa0]
    1e94:       48 89 c7                mov    rdi,rax
    1e97:       e8 94 f3 ff ff          call   1230 <MD5_Init@plt>
    1e9c:       48 8d 4d d0             lea    rcx,[rbp-0x30]
    1ea0:       48 8d 85 60 ff ff ff    lea    rax,[rbp-0xa0]
    1ea7:       ba 1a 00 00 00          mov    edx,0x1a
    1eac:       48 89 ce                mov    rsi,rcx
    1eaf:       48 89 c7                mov    rdi,rax
    1eb2:       e8 49 f3 ff ff          call   1200 <MD5_Update@plt>
    1eb7:       48 8d 95 60 ff ff ff    lea    rdx,[rbp-0xa0]
    1ebe:       48 8d 45 c0             lea    rax,[rbp-0x40]
    1ec2:       48 89 d6                mov    rsi,rdx
    1ec5:       48 89 c7                mov    rdi,rax
    1ec8:       e8 23 f3 ff ff          call   11f0 <MD5_Final@plt>
    1ecd:       48 8d 45 d0             lea    rax,[rbp-0x30]
    1ed1:       ba 1a 00 00 00          mov    edx,0x1a
    1ed6:       be 00 00 00 00          mov    esi,0x0
    1edb:       48 89 c7                mov    rdi,rax
    1ede:       e8 9d f2 ff ff          call   1180 <memset@plt>
    1ee3:       48 8b 45 c0             mov    rax,QWORD PTR [rbp-0x40]
    1ee7:       48 8b 55 c8             mov    rdx,QWORD PTR [rbp-0x38]
    1eeb:       48 89 45 d0             mov    QWORD PTR [rbp-0x30],rax
    1eef:       48 89 55 d8             mov    QWORD PTR [rbp-0x28],rdx
    1ef3:       48 8d 3d 4e 15 00 00    lea    rdi,[rip+0x154e]        # 3448 <_IO_stdin_used+0x448>
    1efa:       e8 91 f2 ff ff          call   1190 <puts@plt>
    1eff:       bf 09 00 00 00          mov    edi,0x9
    1f04:       e8 b7 f2 ff ff          call   11c0 <putchar@plt>
    1f09:       c7 85 4c ff ff ff 00    mov    DWORD PTR [rbp-0xb4],0x0
    1f10:       00 00 00 
    1f13:       eb 2a                   jmp    1f3f <main+0x391>
    1f15:       8b 85 4c ff ff ff       mov    eax,DWORD PTR [rbp-0xb4]
    1f1b:       48 98                   cdqe
    1f1d:       0f b6 44 05 d0          movzx  eax,BYTE PTR [rbp+rax*1-0x30]
    1f22:       0f b6 c0                movzx  eax,al
    1f25:       89 c6                   mov    esi,eax
    1f27:       48 8d 3d a6 14 00 00    lea    rdi,[rip+0x14a6]        # 33d4 <_IO_stdin_used+0x3d4>
    1f2e:       b8 00 00 00 00          mov    eax,0x0
    1f33:       e8 38 f2 ff ff          call   1170 <printf@plt>
    1f38:       83 85 4c ff ff ff 01    add    DWORD PTR [rbp-0xb4],0x1
    1f3f:       83 bd 4c ff ff ff 19    cmp    DWORD PTR [rbp-0xb4],0x19
    1f46:       7e cd                   jle    1f15 <main+0x367>
    1f48:       48 8d 3d bb 11 00 00    lea    rdi,[rip+0x11bb]        # 310a <_IO_stdin_used+0x10a>
    1f4f:       e8 3c f2 ff ff          call   1190 <puts@plt>
    1f54:       48 8d 3d 15 15 00 00    lea    rdi,[rip+0x1515]        # 3470 <_IO_stdin_used+0x470>
    1f5b:       e8 30 f2 ff ff          call   1190 <puts@plt>
    1f60:       48 8d 3d 61 15 00 00    lea    rdi,[rip+0x1561]        # 34c8 <_IO_stdin_used+0x4c8>
    1f67:       e8 24 f2 ff ff          call   1190 <puts@plt>
    1f6c:       bf 09 00 00 00          mov    edi,0x9
    1f71:       e8 4a f2 ff ff          call   11c0 <putchar@plt>
    1f76:       c7 85 50 ff ff ff 00    mov    DWORD PTR [rbp-0xb0],0x0
    1f7d:       00 00 00 
    1f80:       eb 2a                   jmp    1fac <main+0x3fe>
    1f82:       8b 85 50 ff ff ff       mov    eax,DWORD PTR [rbp-0xb0]
    1f88:       48 98                   cdqe
    1f8a:       0f b6 44 05 d0          movzx  eax,BYTE PTR [rbp+rax*1-0x30]
    1f8f:       0f b6 c0                movzx  eax,al
    1f92:       89 c6                   mov    esi,eax
    1f94:       48 8d 3d 39 14 00 00    lea    rdi,[rip+0x1439]        # 33d4 <_IO_stdin_used+0x3d4>
    1f9b:       b8 00 00 00 00          mov    eax,0x0
    1fa0:       e8 cb f1 ff ff          call   1170 <printf@plt>
    1fa5:       83 85 50 ff ff ff 01    add    DWORD PTR [rbp-0xb0],0x1
    1fac:       83 bd 50 ff ff ff 19    cmp    DWORD PTR [rbp-0xb0],0x19
    1fb3:       7e cd                   jle    1f82 <main+0x3d4>
    1fb5:       48 8d 3d 4e 11 00 00    lea    rdi,[rip+0x114e]        # 310a <_IO_stdin_used+0x10a>
    1fbc:       e8 cf f1 ff ff          call   1190 <puts@plt>
    1fc1:       48 8d 3d 21 15 00 00    lea    rdi,[rip+0x1521]        # 34e9 <_IO_stdin_used+0x4e9>
    1fc8:       e8 c3 f1 ff ff          call   1190 <puts@plt>
    1fcd:       bf 09 00 00 00          mov    edi,0x9
    1fd2:       e8 e9 f1 ff ff          call   11c0 <putchar@plt>
    1fd7:       c7 85 54 ff ff ff 00    mov    DWORD PTR [rbp-0xac],0x0
    1fde:       00 00 00 
    1fe1:       eb 30                   jmp    2013 <main+0x465>
    1fe3:       8b 85 54 ff ff ff       mov    eax,DWORD PTR [rbp-0xac]
    1fe9:       48 98                   cdqe
    1feb:       48 8d 15 1e 30 00 00    lea    rdx,[rip+0x301e]        # 5010 <EXPECTED_RESULT>
    1ff2:       0f b6 04 10             movzx  eax,BYTE PTR [rax+rdx*1]
    1ff6:       0f b6 c0                movzx  eax,al
    1ff9:       89 c6                   mov    esi,eax
    1ffb:       48 8d 3d d2 13 00 00    lea    rdi,[rip+0x13d2]        # 33d4 <_IO_stdin_used+0x3d4>
    2002:       b8 00 00 00 00          mov    eax,0x0
    2007:       e8 64 f1 ff ff          call   1170 <printf@plt>
    200c:       83 85 54 ff ff ff 01    add    DWORD PTR [rbp-0xac],0x1
    2013:       83 bd 54 ff ff ff 19    cmp    DWORD PTR [rbp-0xac],0x19
    201a:       7e c7                   jle    1fe3 <main+0x435>
    201c:       48 8d 3d e7 10 00 00    lea    rdi,[rip+0x10e7]        # 310a <_IO_stdin_used+0x10a>
    2023:       e8 68 f1 ff ff          call   1190 <puts@plt>
    2028:       48 8d 3d d1 14 00 00    lea    rdi,[rip+0x14d1]        # 3500 <_IO_stdin_used+0x500>
    202f:       e8 5c f1 ff ff          call   1190 <puts@plt>
    2034:       48 8d 45 d0             lea    rax,[rbp-0x30]
    2038:       ba 1a 00 00 00          mov    edx,0x1a
    203d:       48 8d 35 cc 2f 00 00    lea    rsi,[rip+0x2fcc]        # 5010 <EXPECTED_RESULT>
    2044:       48 89 c7                mov    rdi,rax
    2047:       e8 04 f2 ff ff          call   1250 <memcmp@plt>
    204c:       85 c0                   test   eax,eax
    204e:       75 14                   jne    2064 <main+0x4b6>
    2050:       b8 00 00 00 00          mov    eax,0x0
    2055:       e8 4d fa ff ff          call   1aa7 <win>
    205a:       bf 00 00 00 00          mov    edi,0x0
    205f:       e8 3c f1 ff ff          call   11a0 <exit@plt>
    2064:       48 8d 3d b9 14 00 00    lea    rdi,[rip+0x14b9]        # 3524 <_IO_stdin_used+0x524>
    206b:       e8 20 f1 ff ff          call   1190 <puts@plt>
    2070:       bf 01 00 00 00          mov    edi,0x1
    2075:       e8 26 f1 ff ff          call   11a0 <exit@plt>
    207a:       66 0f 1f 44 00 00       nop    WORD PTR [rax+rax*1+0x0]

0000000000002080 <__libc_csu_init>:
    2080:       f3 0f 1e fa             endbr64
    2084:       41 57                   push   r15
    2086:       4c 8d 3d 93 2c 00 00    lea    r15,[rip+0x2c93]        # 4d20 <__frame_dummy_init_array_entry>
    208d:       41 56                   push   r14
    208f:       49 89 d6                mov    r14,rdx
    2092:       41 55                   push   r13
    2094:       49 89 f5                mov    r13,rsi
    2097:       41 54                   push   r12
    2099:       41 89 fc                mov    r12d,edi
    209c:       55                      push   rbp
    209d:       48 8d 2d 84 2c 00 00    lea    rbp,[rip+0x2c84]        # 4d28 <__do_global_dtors_aux_fini_array_entry>
    20a4:       53                      push   rbx
    20a5:       4c 29 fd                sub    rbp,r15
    20a8:       48 83 ec 08             sub    rsp,0x8
    20ac:       e8 4f ef ff ff          call   1000 <_init>
    20b1:       48 c1 fd 03             sar    rbp,0x3
    20b5:       74 1f                   je     20d6 <__libc_csu_init+0x56>
    20b7:       31 db                   xor    ebx,ebx
    20b9:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]
    20c0:       4c 89 f2                mov    rdx,r14
    20c3:       4c 89 ee                mov    rsi,r13
    20c6:       44 89 e7                mov    edi,r12d
    20c9:       41 ff 14 df             call   QWORD PTR [r15+rbx*8]
    20cd:       48 83 c3 01             add    rbx,0x1
    20d1:       48 39 dd                cmp    rbp,rbx
    20d4:       75 ea                   jne    20c0 <__libc_csu_init+0x40>
    20d6:       48 83 c4 08             add    rsp,0x8
    20da:       5b                      pop    rbx
    20db:       5d                      pop    rbp
    20dc:       41 5c                   pop    r12
    20de:       41 5d                   pop    r13
    20e0:       41 5e                   pop    r14
    20e2:       41 5f                   pop    r15
    20e4:       c3                      ret
    20e5:       66 66 2e 0f 1f 84 00    data16 cs nop WORD PTR [rax+rax*1+0x0]
    20ec:       00 00 00 00 

00000000000020f0 <__libc_csu_fini>:
    20f0:       f3 0f 1e fa             endbr64
    20f4:       c3                      ret

Disassembly of section .fini:

00000000000020f8 <_fini>:
    20f8:       f3 0f 1e fa             endbr64
    20fc:       48 83 ec 08             sub    rsp,0x8
    2100:       48 83 c4 08             add    rsp,0x8
    2104:       c3                      ret
```
- Since we can only patch 1 byte, I decided to patch the offset of the `jne` instruction to `0`, so the `jne` instruction effectively does nothing and the program will continue to execute the next instruction.
- `204e:       75 14                   jne    2064 <main+0x4b6>`. So I need to change the byte at `204f` to `0`.
- Running and patching the program:
```
###
### Welcome to ./babyrev-level-10-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Unfortunately for you, the license key cannot be reversed. You'll have to crack this program.

Changing byte 1/1.
Offset (hex) to change: 204f
New value (hex): 0
The byte has been changed: *0x64e2b5b5d04f = 0.
Ready to receive your license key!

test
Initial input:

        74 65 73 74 0a 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

This challenge is now mangling your input using the `md5` mangler. This mangler cannot be reversed.

This mangled your input, resulting in:

        bd 04 37 a7 df 4e 51 0d c8 61 dc 19 76 21 3e 1e 00 00 00 00 00 00 00 00 00 00 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        bd 04 37 a7 df 4e 51 0d c8 61 dc 19 76 21 3e 1e 00 00 00 00 00 00 00 00 00 00 

Expected result:

        bf db af 10 70 78 59 02 5d ac 08 a9 c2 18 59 f7 00 00 00 00 00 00 00 00 00 00 

Checking the received license key!

You win! Here is your flag:
pwn.college{cbqiH9tdTVshBv10OfgibwkcXcO.0VO2IDL5QTO0czW}
```
- Flag: `pwn.college{cbqiH9tdTVshBv10OfgibwkcXcO.0VO2IDL5QTO0czW}`