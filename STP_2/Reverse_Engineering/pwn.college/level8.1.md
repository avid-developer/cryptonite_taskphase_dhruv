# level8.1
## Description
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
## Solution
- The executable program's name is `babyrev-level-8-1`
- By this time, the graph in IDA is getting very complex, so I used the Pseudo C option in Binary Ninja to make it easier to follow
- Analysing the main function:
```c
000013b0  int32_t main(int32_t argc, char** argv, char** envp)

000013b0  {
000013bc      int32_t argc_1 = argc;
000013c3      char** envp_1 = envp;
000013d0      void* fsbase;
000013d0      int64_t var_10 = *(uint64_t*)((char*)fsbase + 0x28);
000013ef      setvbuf(stdin, nullptr, 2, 0);
0000140d      setvbuf(stdout, nullptr, 2, 0);
00001419      puts(&data_210c);
00001434      printf("### Welcome to %s!\n", *(uint64_t*)argv);
00001440      puts(&data_210c);
0000144a      putchar(0xa);
00001456      puts("This license verifier software w…");
00001462      puts("are licensed to read flag files!…");
0000146e      puts("different operations on that inp…");
0000147a      puts("Providing the correct license ke…");
0000147f      int64_t var_38;
0000147f      __builtin_memset(&var_38, 0, 0x1f);
0000149f      int32_t var_18 = 0;
000014a6      int16_t var_14 = 0;
000014b3      puts("Ready to receive your license ke…");
000014c9      read(0, &var_38, 0x25);
000014e0      int56_t var_20;
000014e0      *(uint8_t*)((char*)var_38)[2] = *(uint8_t*)((char*)var_20)[6];
000014e7      *(uint8_t*)((char*)var_20)[6] = *(uint8_t*)((char*)var_38)[2];
0000156a      for (int32_t i = 0; i <= 0x23; i = (i + 1))
0000156a      {
00001560          for (int32_t j = 0; j < (0x24 - i); j = (j + 1))
00001560          {
00001515              if (*(uint8_t*)(&var_38 + ((int64_t)j)) > *(uint8_t*)(&var_38 + ((int64_t)(j + 1))))
00001515              {
0000151c                  char rax_16 = *(uint8_t*)(&var_38 + ((int64_t)j));
0000153d                  *(uint8_t*)(&var_38 + ((int64_t)j)) = *(uint8_t*)(&var_38 + ((int64_t)(j + 1)));
0000154d                  *(uint8_t*)(&var_38 + ((int64_t)(j + 1))) = rax_16;
00001515              }
00001560          }
0000156a      }
00001596      for (int32_t i_1 = 0; i_1 <= 0x24; i_1 = (i_1 + 1))
00001596      {
00001589          *(uint8_t*)(&var_38 + ((int64_t)i_1)) = (*(uint8_t*)(&var_38 + ((int64_t)i_1)) ^ 0x98);
00001596      }
000015e7      for (int32_t i_2 = 0; i_2 <= 0x11; i_2 = (i_2 + 1))
000015e7      {
000015a6          char rax_35 = *(uint8_t*)(&var_38 + ((int64_t)i_2));
000015c9          *(uint8_t*)(&var_38 + ((int64_t)i_2)) = *(uint8_t*)(&var_38 + ((int64_t)(0x24 - i_2)));
000015db          *(uint8_t*)(&var_38 + ((int64_t)(0x24 - i_2))) = rax_35;
000015e7      }
00001688      for (int32_t i_3 = 0; i_3 <= 0x24; i_3 = (i_3 + 1))
00001688      {
0000161c          int32_t rax_50 = (i_3 % 3);
00001621          if (rax_50 == 2)
00001621          {
0000167b              *(uint8_t*)(&var_38 + ((int64_t)i_3)) = (*(uint8_t*)(&var_38 + ((int64_t)i_3)) ^ 0x86);
00001621          }
00001621          else if (rax_50 == 0)
0000162a          {
00001647              *(uint8_t*)(&var_38 + ((int64_t)i_3)) = (*(uint8_t*)(&var_38 + ((int64_t)i_3)) ^ 0x6f);
0000162a          }
0000162a          else if (rax_50 == 1)
0000162f          {
00001661              *(uint8_t*)(&var_38 + ((int64_t)i_3)) = (*(uint8_t*)(&var_38 + ((int64_t)i_3)) ^ 0x90);
0000162f          }
00001688      }
000016dd      for (int32_t i_4 = 0; i_4 <= 0x11; i_4 = (i_4 + 1))
000016dd      {
0000169c          char rax_71 = *(uint8_t*)(&var_38 + ((int64_t)i_4));
000016bf          *(uint8_t*)(&var_38 + ((int64_t)i_4)) = *(uint8_t*)(&var_38 + ((int64_t)(0x24 - i_4)));
000016d1          *(uint8_t*)(&var_38 + ((int64_t)(0x24 - i_4))) = rax_71;
000016dd      }
000017e4      for (int32_t i_5 = 0; i_5 <= 0x24; i_5 = (i_5 + 1))
000017e4      {
00001715          switch ((i_5 % 6))
00001715          {
00001752              case 0:
00001752              {
00001752                  *(uint8_t*)(&var_38 + ((int64_t)i_5)) = (*(uint8_t*)(&var_38 + ((int64_t)i_5)) ^ 0x65);
00001752                  break;
00001752              }
0000176f              case 1:
0000176f              {
0000176f                  *(uint8_t*)(&var_38 + ((int64_t)i_5)) = (*(uint8_t*)(&var_38 + ((int64_t)i_5)) ^ 5);
0000176f                  break;
0000176f              }
00001789              case 2:
00001789              {
00001789                  *(uint8_t*)(&var_38 + ((int64_t)i_5)) = (*(uint8_t*)(&var_38 + ((int64_t)i_5)) ^ 0xdf);
00001789                  break;
00001789              }
000017a3              case 3:
000017a3              {
000017a3                  *(uint8_t*)(&var_38 + ((int64_t)i_5)) = (*(uint8_t*)(&var_38 + ((int64_t)i_5)) ^ 0x36);
000017a3                  break;
000017a3              }
000017bd              case 4:
000017bd              {
000017bd                  *(uint8_t*)(&var_38 + ((int64_t)i_5)) = (*(uint8_t*)(&var_38 + ((int64_t)i_5)) ^ 0x10);
000017bd                  break;
000017bd              }
000017d7              case 5:
000017d7              {
000017d7                  *(uint8_t*)(&var_38 + ((int64_t)i_5)) = (*(uint8_t*)(&var_38 + ((int64_t)i_5)) ^ 0xdf);
000017d7                  break;
000017d7              }
00001715          }
000017e4      }
000017f1      puts("Checking the received license ke…");
00001810      if (memcmp(&var_38, &data_4020, 0x25) != 0)
00001810      {
0000182d          puts("Wrong! No flag for you!");
00001837          exit(1);
00001837          /* no return */
00001810      }
00001817      sub_12a9();
00001821      exit(0);
00001821      /* no return */
000013b0  }
```
- Similar to [level8.0](./level8.0.md), the input is being mangled a bunch of times before being compared to the correct key.
- The key at memory address `0x4020` is `f3 79 b5 a2 6a b3 f7 7d b0 a6 69 bc fe 77 ba ae 7e a7 e0 68 a4 b2 7a a2 e7 6e a1 b7 79 af ea 63 ae b8 74 ad e8`
- We just need to reverse the mangling process to get the correct key.
- Our input `buf` is being stored at `var_38` (which is `rbp-0x38`).
- In the first step, it is swapping `var_38[2]` (which is the 3rd byte of our input) with `var_20[6]` (which is `rbp-0x20[6]`).
- `var_20[6]` can be expressed as `0x38 - 0x20 + 6 = 24+6 = 30` bytes from the start of our input or `var_38[30]`.
- So the first step is swapping `var_38[2]` with `var_38[30]`.
- I reversed the entire mangling process with the help of the following [script](./level8.1.py) and got the correct key:
```python
# Initial hex array
buf = [0xf3, 0x79, 0xb5, 0xa2, 0x6a, 0xb3, 0xf7, 0x7d, 0xb0, 0xa6, 0x69, 0xbc,
       0xfe, 0x77, 0xba, 0xae, 0x7e, 0xa7, 0xe0, 0x68, 0xa4, 0xb2, 0x7a, 0xa2,
       0xe7, 0x6e, 0xa1, 0xb7, 0x79, 0xaf, 0xea, 0x63, 0xae, 0xb8, 0x74, 0xad, 0xe8]

# First XOR operations
key1 = [0x65, 0x05, 0xdf, 0x36, 0x10, 0xdf]
for i in range(len(buf)):
    buf[i] ^= key1[i % 6]

# First reverse
buf = buf[::-1]

# Second XOR operations
key2 = [0x6f, 0x90, 0x86]
for i in range(len(buf)):
    buf[i] ^= key2[i % 3]

# Second reverse
buf = buf[::-1]

# XOR with 0x98
for i in range(len(buf)):
    buf[i] ^= 0x98

# Sort descending
buf.sort(reverse=True)

# Swap indexes 2 and 30
buf[2], buf[30] = buf[30], buf[2]

# Format output
echo_command = 'echo -ne "' + ''.join('\\x{:02x}'.format(x) for x in buf) + '" | ./babyrev-level-8-1'
print(echo_command)
```
- Got the output: `echo -ne "\xdd\xd7\x66\xc9\xc6\xc3\x7a\x7a\x7a\x79\x78\x78\x78\x77\x76\x75\x75\x75\x74\x73\x73\x72\x70\x70\x6f\x6c\x6c\x6b\x67\x67\xd2\x65\x64\x64\x63\x62\x61" | ./babyrev-level-8-1`
- Ran the program with the output and got the flag: `pwn.college{oJd_XKAm9d9mSD_imVD6cxWviiq.0lN2IDL5QTO0czW}`