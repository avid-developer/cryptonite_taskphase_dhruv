# ARMssembly 0
## Description
What integer does this program print with arguments `182476535` and `3742084308`? File: [chall.S](./chall.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## Hint
Simple compare
## Solution
- This is what's inside the [chal.S](./chall.S) file:
```assembly
	.arch armv8-a
	.file	"chall.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
func1:
	sub	sp, sp, #16
	str	w0, [sp, 12]
	str	w1, [sp, 8]
	ldr	w1, [sp, 12]
	ldr	w0, [sp, 8]
	cmp	w1, w0
	bls	.L2
	ldr	w0, [sp, 12]
	b	.L3
.L2:
	ldr	w0, [sp, 8]
.L3:
	add	sp, sp, 16
	ret
	.size	func1, .-func1
	.section	.rodata
	.align	3
.LC0:
	.string	"Result: %ld\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	x19, [sp, 16]
	str	w0, [x29, 44]
	str	x1, [x29, 32]
	ldr	x0, [x29, 32]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	mov	w19, w0
	ldr	x0, [x29, 32]
	add	x0, x0, 16
	ldr	x0, [x0]
	bl	atoi
	mov	w1, w0
	mov	w0, w19
	bl	func1
	mov	w1, w0
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	printf
	mov	w0, 0
	ldr	x19, [sp, 16]
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
```
- It's ARM64 assembly code (as can be seen from the first line `.arch armv8-a`). I didn't have any experience working with assembly code before, so I had to learn a bit about it. 
- Since I have an ARM64 Ubuntu VM in my VMWare Fusion installed already, I decided to compile the code and run it to see what it does.
- I wasn't aware of the commands needed to compile this assembly code into an executable, so I had to search for it. 
- I first used `as -o chall.o chall.S` to assemble the code using the GNU assembler into an object file.
- I then tried to use `ld -o chall chall.o` which uses the GNU linker to create an executable from the object file. However, I got the following error:
```
ld: warning: cannot find entry symbol _start; defaulting to 00000000004000b0
ld: chall.o: in function `main':
chall.c:(.text+0x50): undefined reference to `atoi'
ld: chall.c:(.text+0x64): undefined reference to `atoi'
ld: chall.c:(.text+0x80): undefined reference to `printf'
```
- After a bit of troubleshooting, I found out that there are C functions like `printf` and `atoi` that are being used in the assembly code. So I need to link this code with the C standard library.
- I used `gcc -o chall chall.o -lc` to compile the code and link it with the C standard library.
- I then ran the code using `./chall 182476535 3742084308` and got the following output:
```
Result: 3742084308
```
- Since the challenge asks for the output in hexadecimal format, I converted the output to hexadecimal using an [online converter](https://www.rapidtables.com/convert/number/decimal-to-hex.html?x=3742084308) and got `DF0BACD4`.
- Cnverting this to the flag format, I got `picoCTF{df0bacd4}`.
- Looking back at the code, it seems like the program is comparing the two arguments passed to it and printing the larger one.
- Since I now know the commands needed to compile and run ARM64 assembly code, I can use them to get the flags of the other challenges in this series as well hopefully.