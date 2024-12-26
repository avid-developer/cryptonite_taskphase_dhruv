# ARMssembly 2
## Description
What integer does this program print with argument `2403814618`? File: [chall_2.S](./chall_2.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## Hint
Loops
## Solution
- The file contains the following code:
```assembly
	.arch armv8-a
	.file	"chall_2.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
func1:
	sub	sp, sp, #32
	str	w0, [sp, 12]
	str	wzr, [sp, 24]
	str	wzr, [sp, 28]
	b	.L2
.L3:
	ldr	w0, [sp, 24]
	add	w0, w0, 3
	str	w0, [sp, 24]
	ldr	w0, [sp, 28]
	add	w0, w0, 1
	str	w0, [sp, 28]
.L2:
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 12]
	cmp	w1, w0
	bcc	.L3
	ldr	w0, [sp, 24]
	add	sp, sp, 32
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
	str	w0, [x29, 28]
	str	x1, [x29, 16]
	ldr	x0, [x29, 16]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	bl	func1
	str	w0, [x29, 44]
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	ldr	w1, [x29, 44]
	bl	printf
	nop
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
```
- Running the code with the argument `2403814618` will give us the required integer:
```bash
as -o chall_2.o chall_2.S
gcc -o chall_2 chall_2.o -lc
./chall_2 2403814618
Result: 2916476558
```
- We convert the result to hex and get our flag: `picoCTF{add5e68e}`
- Looking back at the code, the code basically multiplies the argument with 3 and returns it. 
- But that is not reflected in the result, 2916476558 is clearly not 2403814618 * 3.
- I deduced that since the code is using `w0` to store our result, which is a 32-bit register, the result wraps around when it exceeds the maximum value of a 32-bit integer.
- To check this, I subtracted the maximum value of a 32-bit integer, which is `4294967295`, from `2403814618 * 3`. And voila, I got `2916476558`, the same number that executing the program gave me.