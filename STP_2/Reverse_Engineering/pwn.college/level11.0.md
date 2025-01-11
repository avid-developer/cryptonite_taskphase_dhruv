# level11.0
## Description
- Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key. This challenge allows you to patch 2 bytes in the binary, but performs an integrity check afterwards.
## Solution
- The executable program's name is `babyrev-level-11-0`
- I ran `objdump -d -M intel babyrev-level-11-0` to disassemble the binary and got the following:
```

babyrev-level-11-0:     file format elf64-x86-64


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
    1293:       4c 8d 05 d6 15 00 00    lea    r8,[rip+0x15d6]        # 2870 <__libc_csu_fini>
    129a:       48 8d 0d 5f 15 00 00    lea    rcx,[rip+0x155f]        # 2800 <__libc_csu_init>
    12a1:       48 8d 3d 91 0e 00 00    lea    rdi,[rip+0xe91]        # 2139 <main>
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
    1373:       90                      nop
    ...
    202d:       90                      nop
    202e:       90                      nop
    202f:       90                      nop
    2030:       5d                      pop    rbp
    2031:       c3                      ret

0000000000002032 <win>:
    2032:       f3 0f 1e fa             endbr64
    2036:       55                      push   rbp
    2037:       48 89 e5                mov    rbp,rsp
    203a:       48 8d 3d c7 0f 00 00    lea    rdi,[rip+0xfc7]        # 3008 <_IO_stdin_used+0x8>
    2041:       e8 4a f1 ff ff          call   1190 <puts@plt>
    2046:       be 00 00 00 00          mov    esi,0x0
    204b:       48 8d 3d d2 0f 00 00    lea    rdi,[rip+0xfd2]        # 3024 <_IO_stdin_used+0x24>
    2052:       b8 00 00 00 00          mov    eax,0x0
    2057:       e8 14 f2 ff ff          call   1270 <open@plt>
    205c:       89 05 fe 2f 00 00       mov    DWORD PTR [rip+0x2ffe],eax        # 5060 <flag_fd.5757>
    2062:       8b 05 f8 2f 00 00       mov    eax,DWORD PTR [rip+0x2ff8]        # 5060 <flag_fd.5757>
    2068:       85 c0                   test   eax,eax
    206a:       79 4d                   jns    20b9 <win+0x87>
    206c:       e8 af f1 ff ff          call   1220 <__errno_location@plt>
    2071:       8b 00                   mov    eax,DWORD PTR [rax]
    2073:       89 c7                   mov    edi,eax
    2075:       e8 96 f1 ff ff          call   1210 <strerror@plt>
    207a:       48 89 c6                mov    rsi,rax
    207d:       48 8d 3d ac 0f 00 00    lea    rdi,[rip+0xfac]        # 3030 <_IO_stdin_used+0x30>
    2084:       b8 00 00 00 00          mov    eax,0x0
    2089:       e8 e2 f0 ff ff          call   1170 <printf@plt>
    208e:       e8 4d f1 ff ff          call   11e0 <geteuid@plt>
    2093:       85 c0                   test   eax,eax
    2095:       74 18                   je     20af <win+0x7d>
    2097:       48 8d 3d c2 0f 00 00    lea    rdi,[rip+0xfc2]        # 3060 <_IO_stdin_used+0x60>
    209e:       e8 ed f0 ff ff          call   1190 <puts@plt>
    20a3:       48 8d 3d de 0f 00 00    lea    rdi,[rip+0xfde]        # 3088 <_IO_stdin_used+0x88>
    20aa:       e8 e1 f0 ff ff          call   1190 <puts@plt>
    20af:       bf ff ff ff ff          mov    edi,0xffffffff
    20b4:       e8 e7 f0 ff ff          call   11a0 <exit@plt>
    20b9:       8b 05 a1 2f 00 00       mov    eax,DWORD PTR [rip+0x2fa1]        # 5060 <flag_fd.5757>
    20bf:       ba 00 01 00 00          mov    edx,0x100
    20c4:       48 8d 35 b5 2f 00 00    lea    rsi,[rip+0x2fb5]        # 5080 <flag.5756>
    20cb:       89 c7                   mov    edi,eax
    20cd:       e8 fe f0 ff ff          call   11d0 <read@plt>
    20d2:       89 05 a8 30 00 00       mov    DWORD PTR [rip+0x30a8],eax        # 5180 <flag_length.5758>
    20d8:       8b 05 a2 30 00 00       mov    eax,DWORD PTR [rip+0x30a2]        # 5180 <flag_length.5758>
    20de:       85 c0                   test   eax,eax
    20e0:       7f 2c                   jg     210e <win+0xdc>
    20e2:       e8 39 f1 ff ff          call   1220 <__errno_location@plt>
    20e7:       8b 00                   mov    eax,DWORD PTR [rax]
    20e9:       89 c7                   mov    edi,eax
    20eb:       e8 20 f1 ff ff          call   1210 <strerror@plt>
    20f0:       48 89 c6                mov    rsi,rax
    20f3:       48 8d 3d e6 0f 00 00    lea    rdi,[rip+0xfe6]        # 30e0 <_IO_stdin_used+0xe0>
    20fa:       b8 00 00 00 00          mov    eax,0x0
    20ff:       e8 6c f0 ff ff          call   1170 <printf@plt>
    2104:       bf ff ff ff ff          mov    edi,0xffffffff
    2109:       e8 92 f0 ff ff          call   11a0 <exit@plt>
    210e:       8b 05 6c 30 00 00       mov    eax,DWORD PTR [rip+0x306c]        # 5180 <flag_length.5758>
    2114:       48 98                   cdqe
    2116:       48 89 c2                mov    rdx,rax
    2119:       48 8d 35 60 2f 00 00    lea    rsi,[rip+0x2f60]        # 5080 <flag.5756>
    2120:       bf 01 00 00 00          mov    edi,0x1
    2125:       e8 36 f1 ff ff          call   1260 <write@plt>
    212a:       48 8d 3d d9 0f 00 00    lea    rdi,[rip+0xfd9]        # 310a <_IO_stdin_used+0x10a>
    2131:       e8 5a f0 ff ff          call   1190 <puts@plt>
    2136:       90                      nop
    2137:       5d                      pop    rbp
    2138:       c3                      ret

0000000000002139 <main>:
    2139:       f3 0f 1e fa             endbr64
    213d:       55                      push   rbp
    213e:       48 89 e5                mov    rbp,rsp
    2141:       48 81 ec 20 01 00 00    sub    rsp,0x120
    2148:       89 bd fc fe ff ff       mov    DWORD PTR [rbp-0x104],edi
    214e:       48 89 b5 f0 fe ff ff    mov    QWORD PTR [rbp-0x110],rsi
    2155:       48 89 95 e8 fe ff ff    mov    QWORD PTR [rbp-0x118],rdx
    215c:       64 48 8b 04 25 28 00    mov    rax,QWORD PTR fs:0x28
    2163:       00 00 
    2165:       48 89 45 f8             mov    QWORD PTR [rbp-0x8],rax
    2169:       31 c0                   xor    eax,eax
    216b:       48 8b 05 ce 2e 00 00    mov    rax,QWORD PTR [rip+0x2ece]        # 5040 <stdin@GLIBC_2.2.5>
    2172:       b9 00 00 00 00          mov    ecx,0x0
    2177:       ba 02 00 00 00          mov    edx,0x2
    217c:       be 00 00 00 00          mov    esi,0x0
    2181:       48 89 c7                mov    rdi,rax
    2184:       e8 27 f0 ff ff          call   11b0 <setvbuf@plt>
    2189:       48 8b 05 b8 2e 00 00    mov    rax,QWORD PTR [rip+0x2eb8]        # 5048 <stdout@GLIBC_2.2.5>
    2190:       b9 00 00 00 00          mov    ecx,0x0
    2195:       ba 02 00 00 00          mov    edx,0x2
    219a:       be 00 00 00 00          mov    esi,0x0
    219f:       48 89 c7                mov    rdi,rax
    21a2:       e8 09 f0 ff ff          call   11b0 <setvbuf@plt>
    21a7:       48 8d 3d 5e 0f 00 00    lea    rdi,[rip+0xf5e]        # 310c <_IO_stdin_used+0x10c>
    21ae:       e8 dd ef ff ff          call   1190 <puts@plt>
    21b3:       48 8b 85 f0 fe ff ff    mov    rax,QWORD PTR [rbp-0x110]
    21ba:       48 8b 00                mov    rax,QWORD PTR [rax]
    21bd:       48 89 c6                mov    rsi,rax
    21c0:       48 8d 3d 49 0f 00 00    lea    rdi,[rip+0xf49]        # 3110 <_IO_stdin_used+0x110>
    21c7:       b8 00 00 00 00          mov    eax,0x0
    21cc:       e8 9f ef ff ff          call   1170 <printf@plt>
    21d1:       48 8d 3d 34 0f 00 00    lea    rdi,[rip+0xf34]        # 310c <_IO_stdin_used+0x10c>
    21d8:       e8 b3 ef ff ff          call   1190 <puts@plt>
    21dd:       bf 0a 00 00 00          mov    edi,0xa
    21e2:       e8 d9 ef ff ff          call   11c0 <putchar@plt>
    21e7:       48 8d 3d 3a 0f 00 00    lea    rdi,[rip+0xf3a]        # 3128 <_IO_stdin_used+0x128>
    21ee:       e8 9d ef ff ff          call   1190 <puts@plt>
    21f3:       48 8d 3d a6 0f 00 00    lea    rdi,[rip+0xfa6]        # 31a0 <_IO_stdin_used+0x1a0>
    21fa:       e8 91 ef ff ff          call   1190 <puts@plt>
    21ff:       48 8d 3d 12 10 00 00    lea    rdi,[rip+0x1012]        # 3218 <_IO_stdin_used+0x218>
    2206:       e8 85 ef ff ff          call   1190 <puts@plt>
    220b:       48 8d 3d 7e 10 00 00    lea    rdi,[rip+0x107e]        # 3290 <_IO_stdin_used+0x290>
    2212:       e8 79 ef ff ff          call   1190 <puts@plt>
    2217:       48 8d 3d b2 10 00 00    lea    rdi,[rip+0x10b2]        # 32d0 <_IO_stdin_used+0x2d0>
    221e:       e8 6d ef ff ff          call   1190 <puts@plt>
    2223:       c7 85 10 ff ff ff 00    mov    DWORD PTR [rbp-0xf0],0x0
    222a:       00 00 00 
    222d:       48 8d 05 35 f1 ff ff    lea    rax,[rip+0xfffffffffffff135]        # 1369 <bin_padding>
    2234:       48 25 00 f0 ff ff       and    rax,0xfffffffffffff000
    223a:       48 2d 00 10 00 00       sub    rax,0x1000
    2240:       48 89 85 38 ff ff ff    mov    QWORD PTR [rbp-0xc8],rax
    2247:       90                      nop
    2248:       8b 85 10 ff ff ff       mov    eax,DWORD PTR [rbp-0xf0]
    224e:       8d 50 01                lea    edx,[rax+0x1]
    2251:       89 95 10 ff ff ff       mov    DWORD PTR [rbp-0xf0],edx
    2257:       c1 e0 0c                shl    eax,0xc
    225a:       48 63 d0                movsxd rdx,eax
    225d:       48 8b 85 38 ff ff ff    mov    rax,QWORD PTR [rbp-0xc8]
    2264:       48 01 d0                add    rax,rdx
    2267:       ba 07 00 00 00          mov    edx,0x7
    226c:       be 00 10 00 00          mov    esi,0x1000
    2271:       48 89 c7                mov    rdi,rax
    2274:       e8 e7 ee ff ff          call   1160 <mprotect@plt>
    2279:       85 c0                   test   eax,eax
    227b:       74 cb                   je     2248 <main+0x10f>
    227d:       48 8d 3d ac 10 00 00    lea    rdi,[rip+0x10ac]        # 3330 <_IO_stdin_used+0x330>
    2284:       e8 07 ef ff ff          call   1190 <puts@plt>
    2289:       48 8d 85 40 ff ff ff    lea    rax,[rbp-0xc0]
    2290:       48 89 c7                mov    rdi,rax
    2293:       e8 98 ef ff ff          call   1230 <MD5_Init@plt>
    2298:       c7 85 14 ff ff ff 00    mov    DWORD PTR [rbp-0xec],0x0
    229f:       00 00 00 
    22a2:       eb 35                   jmp    22d9 <main+0x1a0>
    22a4:       8b 85 14 ff ff ff       mov    eax,DWORD PTR [rbp-0xec]
    22aa:       c1 e0 0c                shl    eax,0xc
    22ad:       48 63 d0                movsxd rdx,eax
    22b0:       48 8b 85 38 ff ff ff    mov    rax,QWORD PTR [rbp-0xc8]
    22b7:       48 8d 0c 02             lea    rcx,[rdx+rax*1]
    22bb:       48 8d 85 40 ff ff ff    lea    rax,[rbp-0xc0]
    22c2:       ba 00 10 00 00          mov    edx,0x1000
    22c7:       48 89 ce                mov    rsi,rcx
    22ca:       48 89 c7                mov    rdi,rax
    22cd:       e8 2e ef ff ff          call   1200 <MD5_Update@plt>
    22d2:       83 85 14 ff ff ff 01    add    DWORD PTR [rbp-0xec],0x1
    22d9:       8b 85 10 ff ff ff       mov    eax,DWORD PTR [rbp-0xf0]
    22df:       83 e8 01                sub    eax,0x1
    22e2:       39 85 14 ff ff ff       cmp    DWORD PTR [rbp-0xec],eax
    22e8:       7c ba                   jl     22a4 <main+0x16b>
    22ea:       48 8d 95 40 ff ff ff    lea    rdx,[rbp-0xc0]
    22f1:       48 8d 45 a0             lea    rax,[rbp-0x60]
    22f5:       48 89 d6                mov    rsi,rdx
    22f8:       48 89 c7                mov    rdi,rax
    22fb:       e8 f0 ee ff ff          call   11f0 <MD5_Final@plt>
    2300:       48 8d 3d 79 10 00 00    lea    rdi,[rip+0x1079]        # 3380 <_IO_stdin_used+0x380>
    2307:       e8 84 ee ff ff          call   1190 <puts@plt>
    230c:       bf 09 00 00 00          mov    edi,0x9
    2311:       e8 aa ee ff ff          call   11c0 <putchar@plt>
    2316:       c7 85 18 ff ff ff 00    mov    DWORD PTR [rbp-0xe8],0x0
    231d:       00 00 00 
    2320:       eb 2a                   jmp    234c <main+0x213>
    2322:       8b 85 18 ff ff ff       mov    eax,DWORD PTR [rbp-0xe8]
    2328:       48 98                   cdqe
    232a:       0f b6 44 05 a0          movzx  eax,BYTE PTR [rbp+rax*1-0x60]
    232f:       0f b6 c0                movzx  eax,al
    2332:       89 c6                   mov    esi,eax
    2334:       48 8d 3d 6c 10 00 00    lea    rdi,[rip+0x106c]        # 33a7 <_IO_stdin_used+0x3a7>
    233b:       b8 00 00 00 00          mov    eax,0x0
    2340:       e8 2b ee ff ff          call   1170 <printf@plt>
    2345:       83 85 18 ff ff ff 01    add    DWORD PTR [rbp-0xe8],0x1
    234c:       83 bd 18 ff ff ff 18    cmp    DWORD PTR [rbp-0xe8],0x18
    2353:       7e cd                   jle    2322 <main+0x1e9>
    2355:       48 8d 3d ae 0d 00 00    lea    rdi,[rip+0xdae]        # 310a <_IO_stdin_used+0x10a>
    235c:       e8 2f ee ff ff          call   1190 <puts@plt>
    2361:       c7 85 1c ff ff ff 00    mov    DWORD PTR [rbp-0xe4],0x0
    2368:       00 00 00 
    236b:       e9 ce 00 00 00          jmp    243e <main+0x305>
    2370:       8b 85 1c ff ff ff       mov    eax,DWORD PTR [rbp-0xe4]
    2376:       83 c0 01                add    eax,0x1
    2379:       89 c6                   mov    esi,eax
    237b:       48 8d 3d 2b 10 00 00    lea    rdi,[rip+0x102b]        # 33ad <_IO_stdin_used+0x3ad>
    2382:       b8 00 00 00 00          mov    eax,0x0
    2387:       e8 e4 ed ff ff          call   1170 <printf@plt>
    238c:       48 8d 3d 2f 10 00 00    lea    rdi,[rip+0x102f]        # 33c2 <_IO_stdin_used+0x3c2>
    2393:       b8 00 00 00 00          mov    eax,0x0
    2398:       e8 d3 ed ff ff          call   1170 <printf@plt>
    239d:       48 8d 85 0e ff ff ff    lea    rax,[rbp-0xf2]
    23a4:       48 89 c6                mov    rsi,rax
    23a7:       48 8d 3d 2d 10 00 00    lea    rdi,[rip+0x102d]        # 33db <_IO_stdin_used+0x3db>
    23ae:       b8 00 00 00 00          mov    eax,0x0
    23b3:       e8 88 ee ff ff          call   1240 <__isoc99_scanf@plt>
    23b8:       48 8d 3d 20 10 00 00    lea    rdi,[rip+0x1020]        # 33df <_IO_stdin_used+0x3df>
    23bf:       b8 00 00 00 00          mov    eax,0x0
    23c4:       e8 a7 ed ff ff          call   1170 <printf@plt>
    23c9:       48 8d 85 0d ff ff ff    lea    rax,[rbp-0xf3]
    23d0:       48 89 c6                mov    rsi,rax
    23d3:       48 8d 3d 17 10 00 00    lea    rdi,[rip+0x1017]        # 33f1 <_IO_stdin_used+0x3f1>
    23da:       b8 00 00 00 00          mov    eax,0x0
    23df:       e8 5c ee ff ff          call   1240 <__isoc99_scanf@plt>
    23e4:       0f b6 8d 0d ff ff ff    movzx  ecx,BYTE PTR [rbp-0xf3]
    23eb:       0f b7 85 0e ff ff ff    movzx  eax,WORD PTR [rbp-0xf2]
    23f2:       0f b7 d0                movzx  edx,ax
    23f5:       48 8b 85 38 ff ff ff    mov    rax,QWORD PTR [rbp-0xc8]
    23fc:       48 01 d0                add    rax,rdx
    23ff:       89 ca                   mov    edx,ecx
    2401:       88 10                   mov    BYTE PTR [rax],dl
    2403:       0f b6 85 0d ff ff ff    movzx  eax,BYTE PTR [rbp-0xf3]
    240a:       0f b6 c0                movzx  eax,al
    240d:       0f b7 95 0e ff ff ff    movzx  edx,WORD PTR [rbp-0xf2]
    2414:       0f b7 ca                movzx  ecx,dx
    2417:       48 8b 95 38 ff ff ff    mov    rdx,QWORD PTR [rbp-0xc8]
    241e:       48 01 d1                add    rcx,rdx
    2421:       89 c2                   mov    edx,eax
    2423:       48 89 ce                mov    rsi,rcx
    2426:       48 8d 3d cb 0f 00 00    lea    rdi,[rip+0xfcb]        # 33f8 <_IO_stdin_used+0x3f8>
    242d:       b8 00 00 00 00          mov    eax,0x0
    2432:       e8 39 ed ff ff          call   1170 <printf@plt>
    2437:       83 85 1c ff ff ff 01    add    DWORD PTR [rbp-0xe4],0x1
    243e:       83 bd 1c ff ff ff 01    cmp    DWORD PTR [rbp-0xe4],0x1
    2445:       0f 8e 25 ff ff ff       jle    2370 <main+0x237>
    244b:       48 8d 85 40 ff ff ff    lea    rax,[rbp-0xc0]
    2452:       48 89 c7                mov    rdi,rax
    2455:       e8 d6 ed ff ff          call   1230 <MD5_Init@plt>
    245a:       c7 85 20 ff ff ff 00    mov    DWORD PTR [rbp-0xe0],0x0
    2461:       00 00 00 
    2464:       eb 35                   jmp    249b <main+0x362>
    2466:       8b 85 20 ff ff ff       mov    eax,DWORD PTR [rbp-0xe0]
    246c:       c1 e0 0c                shl    eax,0xc
    246f:       48 63 d0                movsxd rdx,eax
    2472:       48 8b 85 38 ff ff ff    mov    rax,QWORD PTR [rbp-0xc8]
    2479:       48 8d 0c 02             lea    rcx,[rdx+rax*1]
    247d:       48 8d 85 40 ff ff ff    lea    rax,[rbp-0xc0]
    2484:       ba 00 10 00 00          mov    edx,0x1000
    2489:       48 89 ce                mov    rsi,rcx
    248c:       48 89 c7                mov    rdi,rax
    248f:       e8 6c ed ff ff          call   1200 <MD5_Update@plt>
    2494:       83 85 20 ff ff ff 01    add    DWORD PTR [rbp-0xe0],0x1
    249b:       8b 85 10 ff ff ff       mov    eax,DWORD PTR [rbp-0xf0]
    24a1:       83 e8 01                sub    eax,0x1
    24a4:       39 85 20 ff ff ff       cmp    DWORD PTR [rbp-0xe0],eax
    24aa:       7c ba                   jl     2466 <main+0x32d>
    24ac:       48 8d 95 40 ff ff ff    lea    rdx,[rbp-0xc0]
    24b3:       48 8d 45 b0             lea    rax,[rbp-0x50]
    24b7:       48 89 d6                mov    rsi,rdx
    24ba:       48 89 c7                mov    rdi,rax
    24bd:       e8 2e ed ff ff          call   11f0 <MD5_Final@plt>
    24c2:       48 8d 3d 57 0f 00 00    lea    rdi,[rip+0xf57]        # 3420 <_IO_stdin_used+0x420>
    24c9:       e8 c2 ec ff ff          call   1190 <puts@plt>
    24ce:       bf 09 00 00 00          mov    edi,0x9
    24d3:       e8 e8 ec ff ff          call   11c0 <putchar@plt>
    24d8:       c7 85 24 ff ff ff 00    mov    DWORD PTR [rbp-0xdc],0x0
    24df:       00 00 00 
    24e2:       eb 2a                   jmp    250e <main+0x3d5>
    24e4:       8b 85 24 ff ff ff       mov    eax,DWORD PTR [rbp-0xdc]
    24ea:       48 98                   cdqe
    24ec:       0f b6 44 05 b0          movzx  eax,BYTE PTR [rbp+rax*1-0x50]
    24f1:       0f b6 c0                movzx  eax,al
    24f4:       89 c6                   mov    esi,eax
    24f6:       48 8d 3d aa 0e 00 00    lea    rdi,[rip+0xeaa]        # 33a7 <_IO_stdin_used+0x3a7>
    24fd:       b8 00 00 00 00          mov    eax,0x0
    2502:       e8 69 ec ff ff          call   1170 <printf@plt>
    2507:       83 85 24 ff ff ff 01    add    DWORD PTR [rbp-0xdc],0x1
    250e:       83 bd 24 ff ff ff 18    cmp    DWORD PTR [rbp-0xdc],0x18
    2515:       7e cd                   jle    24e4 <main+0x3ab>
    2517:       48 8d 3d ec 0b 00 00    lea    rdi,[rip+0xbec]        # 310a <_IO_stdin_used+0x10a>
    251e:       e8 6d ec ff ff          call   1190 <puts@plt>
    2523:       48 8d 4d b0             lea    rcx,[rbp-0x50]
    2527:       48 8d 45 a0             lea    rax,[rbp-0x60]
    252b:       ba 10 00 00 00          mov    edx,0x10
    2530:       48 89 ce                mov    rsi,rcx
    2533:       48 89 c7                mov    rdi,rax
    2536:       e8 15 ed ff ff          call   1250 <memcmp@plt>
    253b:       85 c0                   test   eax,eax
    253d:       75 6e                   jne    25ad <main+0x474>
    253f:       48 8d 3d 02 0f 00 00    lea    rdi,[rip+0xf02]        # 3448 <_IO_stdin_used+0x448>
    2546:       e8 45 ec ff ff          call   1190 <puts@plt>
    254b:       48 c7 45 d0 00 00 00    mov    QWORD PTR [rbp-0x30],0x0
    2552:       00 
    2553:       48 c7 45 d8 00 00 00    mov    QWORD PTR [rbp-0x28],0x0
    255a:       00 
    255b:       48 c7 45 e0 00 00 00    mov    QWORD PTR [rbp-0x20],0x0
    2562:       00 
    2563:       66 c7 45 e8 00 00       mov    WORD PTR [rbp-0x18],0x0
    2569:       48 8d 3d 38 0f 00 00    lea    rdi,[rip+0xf38]        # 34a8 <_IO_stdin_used+0x4a8>
    2570:       e8 1b ec ff ff          call   1190 <puts@plt>
    2575:       48 8d 45 d0             lea    rax,[rbp-0x30]
    2579:       ba 19 00 00 00          mov    edx,0x19
    257e:       48 89 c6                mov    rsi,rax
    2581:       bf 00 00 00 00          mov    edi,0x0
    2586:       e8 45 ec ff ff          call   11d0 <read@plt>
    258b:       48 8d 3d 3a 0f 00 00    lea    rdi,[rip+0xf3a]        # 34cc <_IO_stdin_used+0x4cc>
    2592:       e8 f9 eb ff ff          call   1190 <puts@plt>
    2597:       bf 09 00 00 00          mov    edi,0x9
    259c:       e8 1f ec ff ff          call   11c0 <putchar@plt>
    25a1:       c7 85 28 ff ff ff 00    mov    DWORD PTR [rbp-0xd8],0x0
    25a8:       00 00 00 
    25ab:       eb 40                   jmp    25ed <main+0x4b4>
    25ad:       48 8d 3d bc 0e 00 00    lea    rdi,[rip+0xebc]        # 3470 <_IO_stdin_used+0x470>
    25b4:       e8 d7 eb ff ff          call   1190 <puts@plt>
    25b9:       bf 01 00 00 00          mov    edi,0x1
    25be:       e8 dd eb ff ff          call   11a0 <exit@plt>
    25c3:       8b 85 28 ff ff ff       mov    eax,DWORD PTR [rbp-0xd8]
    25c9:       48 98                   cdqe
    25cb:       0f b6 44 05 d0          movzx  eax,BYTE PTR [rbp+rax*1-0x30]
    25d0:       0f b6 c0                movzx  eax,al
    25d3:       89 c6                   mov    esi,eax
    25d5:       48 8d 3d cb 0d 00 00    lea    rdi,[rip+0xdcb]        # 33a7 <_IO_stdin_used+0x3a7>
    25dc:       b8 00 00 00 00          mov    eax,0x0
    25e1:       e8 8a eb ff ff          call   1170 <printf@plt>
    25e6:       83 85 28 ff ff ff 01    add    DWORD PTR [rbp-0xd8],0x1
    25ed:       83 bd 28 ff ff ff 18    cmp    DWORD PTR [rbp-0xd8],0x18
    25f4:       7e cd                   jle    25c3 <main+0x48a>
    25f6:       48 8d 3d 0d 0b 00 00    lea    rdi,[rip+0xb0d]        # 310a <_IO_stdin_used+0x10a>
    25fd:       e8 8e eb ff ff          call   1190 <puts@plt>
    2602:       48 8d 3d d7 0e 00 00    lea    rdi,[rip+0xed7]        # 34e0 <_IO_stdin_used+0x4e0>
    2609:       e8 82 eb ff ff          call   1190 <puts@plt>
    260e:       48 8d 85 40 ff ff ff    lea    rax,[rbp-0xc0]
    2615:       48 89 c7                mov    rdi,rax
    2618:       e8 13 ec ff ff          call   1230 <MD5_Init@plt>
    261d:       48 8d 4d d0             lea    rcx,[rbp-0x30]
    2621:       48 8d 85 40 ff ff ff    lea    rax,[rbp-0xc0]
    2628:       ba 19 00 00 00          mov    edx,0x19
    262d:       48 89 ce                mov    rsi,rcx
    2630:       48 89 c7                mov    rdi,rax
    2633:       e8 c8 eb ff ff          call   1200 <MD5_Update@plt>
    2638:       48 8d 95 40 ff ff ff    lea    rdx,[rbp-0xc0]
    263f:       48 8d 45 c0             lea    rax,[rbp-0x40]
    2643:       48 89 d6                mov    rsi,rdx
    2646:       48 89 c7                mov    rdi,rax
    2649:       e8 a2 eb ff ff          call   11f0 <MD5_Final@plt>
    264e:       48 8d 45 d0             lea    rax,[rbp-0x30]
    2652:       ba 19 00 00 00          mov    edx,0x19
    2657:       be 00 00 00 00          mov    esi,0x0
    265c:       48 89 c7                mov    rdi,rax
    265f:       e8 1c eb ff ff          call   1180 <memset@plt>
    2664:       48 8b 45 c0             mov    rax,QWORD PTR [rbp-0x40]
    2668:       48 8b 55 c8             mov    rdx,QWORD PTR [rbp-0x38]
    266c:       48 89 45 d0             mov    QWORD PTR [rbp-0x30],rax
    2670:       48 89 55 d8             mov    QWORD PTR [rbp-0x28],rdx
    2674:       48 8d 3d cd 0e 00 00    lea    rdi,[rip+0xecd]        # 3548 <_IO_stdin_used+0x548>
    267b:       e8 10 eb ff ff          call   1190 <puts@plt>
    2680:       bf 09 00 00 00          mov    edi,0x9
    2685:       e8 36 eb ff ff          call   11c0 <putchar@plt>
    268a:       c7 85 2c ff ff ff 00    mov    DWORD PTR [rbp-0xd4],0x0
    2691:       00 00 00 
    2694:       eb 2a                   jmp    26c0 <main+0x587>
    2696:       8b 85 2c ff ff ff       mov    eax,DWORD PTR [rbp-0xd4]
    269c:       48 98                   cdqe
    269e:       0f b6 44 05 d0          movzx  eax,BYTE PTR [rbp+rax*1-0x30]
    26a3:       0f b6 c0                movzx  eax,al
    26a6:       89 c6                   mov    esi,eax
    26a8:       48 8d 3d f8 0c 00 00    lea    rdi,[rip+0xcf8]        # 33a7 <_IO_stdin_used+0x3a7>
    26af:       b8 00 00 00 00          mov    eax,0x0
    26b4:       e8 b7 ea ff ff          call   1170 <printf@plt>
    26b9:       83 85 2c ff ff ff 01    add    DWORD PTR [rbp-0xd4],0x1
    26c0:       83 bd 2c ff ff ff 18    cmp    DWORD PTR [rbp-0xd4],0x18
    26c7:       7e cd                   jle    2696 <main+0x55d>
    26c9:       48 8d 3d 3a 0a 00 00    lea    rdi,[rip+0xa3a]        # 310a <_IO_stdin_used+0x10a>
    26d0:       e8 bb ea ff ff          call   1190 <puts@plt>
    26d5:       48 8d 3d 94 0e 00 00    lea    rdi,[rip+0xe94]        # 3570 <_IO_stdin_used+0x570>
    26dc:       e8 af ea ff ff          call   1190 <puts@plt>
    26e1:       48 8d 3d e0 0e 00 00    lea    rdi,[rip+0xee0]        # 35c8 <_IO_stdin_used+0x5c8>
    26e8:       e8 a3 ea ff ff          call   1190 <puts@plt>
    26ed:       bf 09 00 00 00          mov    edi,0x9
    26f2:       e8 c9 ea ff ff          call   11c0 <putchar@plt>
    26f7:       c7 85 30 ff ff ff 00    mov    DWORD PTR [rbp-0xd0],0x0
    26fe:       00 00 00 
    2701:       eb 2a                   jmp    272d <main+0x5f4>
    2703:       8b 85 30 ff ff ff       mov    eax,DWORD PTR [rbp-0xd0]
    2709:       48 98                   cdqe
    270b:       0f b6 44 05 d0          movzx  eax,BYTE PTR [rbp+rax*1-0x30]
    2710:       0f b6 c0                movzx  eax,al
    2713:       89 c6                   mov    esi,eax
    2715:       48 8d 3d 8b 0c 00 00    lea    rdi,[rip+0xc8b]        # 33a7 <_IO_stdin_used+0x3a7>
    271c:       b8 00 00 00 00          mov    eax,0x0
    2721:       e8 4a ea ff ff          call   1170 <printf@plt>
    2726:       83 85 30 ff ff ff 01    add    DWORD PTR [rbp-0xd0],0x1
    272d:       83 bd 30 ff ff ff 18    cmp    DWORD PTR [rbp-0xd0],0x18
    2734:       7e cd                   jle    2703 <main+0x5ca>
    2736:       48 8d 3d cd 09 00 00    lea    rdi,[rip+0x9cd]        # 310a <_IO_stdin_used+0x10a>
    273d:       e8 4e ea ff ff          call   1190 <puts@plt>
    2742:       48 8d 3d a0 0e 00 00    lea    rdi,[rip+0xea0]        # 35e9 <_IO_stdin_used+0x5e9>
    2749:       e8 42 ea ff ff          call   1190 <puts@plt>
    274e:       bf 09 00 00 00          mov    edi,0x9
    2753:       e8 68 ea ff ff          call   11c0 <putchar@plt>
    2758:       c7 85 34 ff ff ff 00    mov    DWORD PTR [rbp-0xcc],0x0
    275f:       00 00 00 
    2762:       eb 30                   jmp    2794 <main+0x65b>
    2764:       8b 85 34 ff ff ff       mov    eax,DWORD PTR [rbp-0xcc]
    276a:       48 98                   cdqe
    276c:       48 8d 15 9d 28 00 00    lea    rdx,[rip+0x289d]        # 5010 <EXPECTED_RESULT>
    2773:       0f b6 04 10             movzx  eax,BYTE PTR [rax+rdx*1]
    2777:       0f b6 c0                movzx  eax,al
    277a:       89 c6                   mov    esi,eax
    277c:       48 8d 3d 24 0c 00 00    lea    rdi,[rip+0xc24]        # 33a7 <_IO_stdin_used+0x3a7>
    2783:       b8 00 00 00 00          mov    eax,0x0
    2788:       e8 e3 e9 ff ff          call   1170 <printf@plt>
    278d:       83 85 34 ff ff ff 01    add    DWORD PTR [rbp-0xcc],0x1
    2794:       83 bd 34 ff ff ff 18    cmp    DWORD PTR [rbp-0xcc],0x18
    279b:       7e c7                   jle    2764 <main+0x62b>
    279d:       48 8d 3d 66 09 00 00    lea    rdi,[rip+0x966]        # 310a <_IO_stdin_used+0x10a>
    27a4:       e8 e7 e9 ff ff          call   1190 <puts@plt>
    27a9:       48 8d 3d 50 0e 00 00    lea    rdi,[rip+0xe50]        # 3600 <_IO_stdin_used+0x600>
    27b0:       e8 db e9 ff ff          call   1190 <puts@plt>
    27b5:       48 8d 45 d0             lea    rax,[rbp-0x30]
    27b9:       ba 19 00 00 00          mov    edx,0x19
    27be:       48 8d 35 4b 28 00 00    lea    rsi,[rip+0x284b]        # 5010 <EXPECTED_RESULT>
    27c5:       48 89 c7                mov    rdi,rax
    27c8:       e8 83 ea ff ff          call   1250 <memcmp@plt>
    27cd:       85 c0                   test   eax,eax
    27cf:       75 14                   jne    27e5 <main+0x6ac>
    27d1:       b8 00 00 00 00          mov    eax,0x0
    27d6:       e8 57 f8 ff ff          call   2032 <win>
    27db:       bf 00 00 00 00          mov    edi,0x0
    27e0:       e8 bb e9 ff ff          call   11a0 <exit@plt>
    27e5:       48 8d 3d 38 0e 00 00    lea    rdi,[rip+0xe38]        # 3624 <_IO_stdin_used+0x624>
    27ec:       e8 9f e9 ff ff          call   1190 <puts@plt>
    27f1:       bf 01 00 00 00          mov    edi,0x1
    27f6:       e8 a5 e9 ff ff          call   11a0 <exit@plt>
    27fb:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000002800 <__libc_csu_init>:
    2800:       f3 0f 1e fa             endbr64
    2804:       41 57                   push   r15
    2806:       4c 8d 3d 13 25 00 00    lea    r15,[rip+0x2513]        # 4d20 <__frame_dummy_init_array_entry>
    280d:       41 56                   push   r14
    280f:       49 89 d6                mov    r14,rdx
    2812:       41 55                   push   r13
    2814:       49 89 f5                mov    r13,rsi
    2817:       41 54                   push   r12
    2819:       41 89 fc                mov    r12d,edi
    281c:       55                      push   rbp
    281d:       48 8d 2d 04 25 00 00    lea    rbp,[rip+0x2504]        # 4d28 <__do_global_dtors_aux_fini_array_entry>
    2824:       53                      push   rbx
    2825:       4c 29 fd                sub    rbp,r15
    2828:       48 83 ec 08             sub    rsp,0x8
    282c:       e8 cf e7 ff ff          call   1000 <_init>
    2831:       48 c1 fd 03             sar    rbp,0x3
    2835:       74 1f                   je     2856 <__libc_csu_init+0x56>
    2837:       31 db                   xor    ebx,ebx
    2839:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]
    2840:       4c 89 f2                mov    rdx,r14
    2843:       4c 89 ee                mov    rsi,r13
    2846:       44 89 e7                mov    edi,r12d
    2849:       41 ff 14 df             call   QWORD PTR [r15+rbx*8]
    284d:       48 83 c3 01             add    rbx,0x1
    2851:       48 39 dd                cmp    rbp,rbx
    2854:       75 ea                   jne    2840 <__libc_csu_init+0x40>
    2856:       48 83 c4 08             add    rsp,0x8
    285a:       5b                      pop    rbx
    285b:       5d                      pop    rbp
    285c:       41 5c                   pop    r12
    285e:       41 5d                   pop    r13
    2860:       41 5e                   pop    r14
    2862:       41 5f                   pop    r15
    2864:       c3                      ret
    2865:       66 66 2e 0f 1f 84 00    data16 cs nop WORD PTR [rax+rax*1+0x0]
    286c:       00 00 00 00 

0000000000002870 <__libc_csu_fini>:
    2870:       f3 0f 1e fa             endbr64
    2874:       c3                      ret

Disassembly of section .fini:

0000000000002878 <_fini>:
    2878:       f3 0f 1e fa             endbr64
    287c:       48 83 ec 08             sub    rsp,0x8
    2880:       48 83 c4 08             add    rsp,0x8
    2884:       c3                      ret
```
- Here is `main`'s pseudocode from IDA:
```c
int __fastcall __noreturn main(int argc, const char **argv, const char **envp)
{
  int v3; // eax
  unsigned __int8 v4; // [rsp+2Dh] [rbp-F3h] BYREF
  unsigned __int16 v5; // [rsp+2Eh] [rbp-F2h] BYREF
  int v6; // [rsp+30h] [rbp-F0h]
  int i; // [rsp+34h] [rbp-ECh]
  int j; // [rsp+38h] [rbp-E8h]
  int k; // [rsp+3Ch] [rbp-E4h]
  int m; // [rsp+40h] [rbp-E0h]
  int n; // [rsp+44h] [rbp-DCh]
  int ii; // [rsp+48h] [rbp-D8h]
  int jj; // [rsp+4Ch] [rbp-D4h]
  int kk; // [rsp+50h] [rbp-D0h]
  int mm; // [rsp+54h] [rbp-CCh]
  unsigned __int64 v16; // [rsp+58h] [rbp-C8h]
  char v17[96]; // [rsp+60h] [rbp-C0h] BYREF
  char s1[16]; // [rsp+C0h] [rbp-60h] BYREF
  char s2[16]; // [rsp+D0h] [rbp-50h] BYREF
  __int64 v20[2]; // [rsp+E0h] [rbp-40h] BYREF
  __int64 buf; // [rsp+F0h] [rbp-30h] BYREF
  __int64 v22; // [rsp+F8h] [rbp-28h]
  __int64 v23; // [rsp+100h] [rbp-20h]
  __int16 v24; // [rsp+108h] [rbp-18h]
  unsigned __int64 v25; // [rsp+118h] [rbp-8h]

  v25 = __readfsqword(0x28u);
  setvbuf(stdin, 0LL, 2, 0LL);
  setvbuf(stdout, 0LL, 2, 0LL);
  puts("###");
  printf("### Welcome to %s!\n", *argv);
  puts("###");
  putchar(10);
  puts(
    "This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you");
  puts("are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely");
  puts(
    "different operations on that input! You must figure out (by reverse engineering this program) what that license key is.");
  puts("Providing the correct license key will net you the flag!\n");
  puts("Unfortunately for you, the license key cannot be reversed. You'll have to crack this program.\n");
  v6 = 0;
  v16 = ((unsigned __int64)bin_padding & 0xFFFFFFFFFFFFF000LL) - 4096;
  do
    v3 = v6++;
  while ( !mprotect((void *)((v3 << 12) + v16), 0x1000uLL, 7) );
  puts("In order to ensure code integrity, the code will be hashed and verified.\n");
  MD5_Init(v17);
  for ( i = 0; i < v6 - 1; ++i )
    MD5_Update(v17, (i << 12) + v16, 4096LL);
  MD5_Final(s1, v17);
  puts("The pre-crack code integrity hash is:\n");
  putchar(9);
  for ( j = 0; j <= 24; ++j )
    printf("%02x ", (unsigned __int8)s1[j]);
  puts("\n");
  for ( k = 0; k <= 1; ++k )
  {
    printf("Changing byte %d/2.\n", (unsigned int)(k + 1));
    printf("Offset (hex) to change: ");
    __isoc99_scanf("%hx", &v5);
    printf("New value (hex): ");
    __isoc99_scanf("%hhx", &v4);
    *(_BYTE *)(v5 + v16) = v4;
    printf("The byte has been changed: *%p = %hhx.\n", (const void *)(v16 + v5), v4);
  }
  MD5_Init(v17);
  for ( m = 0; m < v6 - 1; ++m )
    MD5_Update(v17, (m << 12) + v16, 4096LL);
  MD5_Final(s2, v17);
  puts("The post-crack code integrity hash is:\n");
  putchar(9);
  for ( n = 0; n <= 24; ++n )
    printf("%02x ", (unsigned __int8)s2[n]);
  puts("\n");
  if ( !memcmp(s1, s2, 0x10uLL) )
  {
    puts("The code's integrity is secure!\n");
    buf = 0LL;
    v22 = 0LL;
    v23 = 0LL;
    v24 = 0;
    puts("Ready to receive your license key!\n");
    read(0, &buf, 0x19uLL);
    puts("Initial input:\n");
    putchar(9);
    for ( ii = 0; ii <= 24; ++ii )
      printf("%02x ", *((unsigned __int8 *)&buf + ii));
    puts("\n");
    puts("This challenge is now mangling your input using the `md5` mangler. This mangler cannot be reversed.\n");
    MD5_Init(v17);
    MD5_Update(v17, &buf, 25LL);
    MD5_Final(v20, v17);
    memset(&buf, 0, 0x19uLL);
    buf = v20[0];
    v22 = v20[1];
    puts("This mangled your input, resulting in:\n");
    putchar(9);
    for ( jj = 0; jj <= 24; ++jj )
      printf("%02x ", *((unsigned __int8 *)&buf + jj));
    puts("\n");
    puts("The mangling is done! The resulting bytes will be used for the final comparison.\n");
    puts("Final result of mangling input:\n");
    putchar(9);
    for ( kk = 0; kk <= 24; ++kk )
      printf("%02x ", *((unsigned __int8 *)&buf + kk));
    puts("\n");
    puts("Expected result:\n");
    putchar(9);
    for ( mm = 0; mm <= 24; ++mm )
      printf("%02x ", EXPECTED_RESULT[mm]);
    puts("\n");
    puts("Checking the received license key!\n");
    if ( !memcmp(&buf, EXPECTED_RESULT, 0x19uLL) )
    {
      win();
      exit(0);
    }
    puts("Wrong! No flag for you!");
    exit(1);
  }
  puts("The code's integrity has been breached, aborting!\n");
  exit(1);
}
```
- The program uses `mprotect` to make the code segment writable, then hashes the code segment using `MD5` and prints the hash. It then allows the user to change 2 bytes in the code segment, hashes the code segment again, and prints the new hash. If the hashes match, the program reads 25 bytes from `stdin`, hashes them using `MD5`, and compares the hash to the expected hash. If they match, the program calls `win` and exits.
- If we don't change any bytes, then the first `memcmp` will pass, but we can't crack the `MD5` hash of the `EXPECTED_RESULT` because the mangler is not reversible.
- So we need to find a way of bypassing the `memcmp` checks. 
- I observed that there are 2 `jne` instructions in `main`:
  - `   253d:       75 6e                   jne    25ad <main+0x474>`
  - `    27cf:       75 14                   jne    27e5 <main+0x6ac>`
- We can change the jump offsets of these instructions to `0` so that the check is effectively nullified.
- Running the program:
```
###
### Welcome to ./babyrev-level-11-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Unfortunately for you, the license key cannot be reversed. You'll have to crack this program.

In order to ensure code integrity, the code will be hashed and verified.

The pre-crack code integrity hash is:

        6b 16 af 11 a7 54 a0 2e 65 8e 54 f5 68 a2 39 91 c2 00 00 00 00 00 00 00 a7 

Changing byte 1/2.
Offset (hex) to change: 253e
New value (hex): 0
The byte has been changed: *0x6100e33d653e = 0.
Changing byte 2/2.
Offset (hex) to change: 27d0
New value (hex): 0
The byte has been changed: *0x6100e33d67d0 = 0.
The post-crack code integrity hash is:

        ef a8 71 4d 1d 47 93 3f 45 67 e6 bc f3 79 e6 b3 a6 50 54 5c fd 7f 00 00 4d 

The code's integrity is secure!

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

        43 75 be 8b be a1 aa d6 a1 6c 3a 68 56 9e 0e 4f 00 00 00 00 00 00 00 00 00 

Checking the received license key!

You win! Here is your flag:
pwn.college{UA0KmWCWB9i9P4Q65DsJruWCfne.0VM3IDL5QTO0czW}
```
- The flag is `pwn.college{UA0KmWCWB9i9P4Q65DsJruWCfne.0VM3IDL5QTO0czW}`.