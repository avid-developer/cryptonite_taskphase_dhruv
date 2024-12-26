# ARMssembly 1
## Description
For what argument does this program print `win` with variables `83`, `0` and `3`? File: [chall_1.S](./chall_1.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## Hint
Shifts
## Solution
- This is what's present in the file [chall_1.S](./chall_1.S):
```assembly
	.arch armv8-a
	.file	"chall_1.c"
	.text
	.align	2
	.global	func
	.type	func, %function
func:
	sub	sp, sp, #32
	str	w0, [sp, 12]
	mov	w0, 83
	str	w0, [sp, 16]
	str	wzr, [sp, 20]
	mov	w0, 3
	str	w0, [sp, 24]
	ldr	w0, [sp, 20]
	ldr	w1, [sp, 16]
	lsl	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 24]
	sdiv	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 12]
	sub	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w0, [sp, 28]
	add	sp, sp, 32
	ret
	.size	func, .-func
	.section	.rodata
	.align	3
.LC0:
	.string	"You win!"
	.align	3
.LC1:
	.string	"You Lose :("
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
	str	w0, [x29, 44]
	ldr	w0, [x29, 44]
	bl	func
	cmp	w0, 0
	bne	.L4
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	puts
	b	.L6
.L4:
	adrp	x0, .LC1
	add	x0, x0, :lo12:.LC1
	bl	puts
.L6:
	nop
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
```
- The code takes one argument, converts it to an integer, and then calls the function `func` with the integer as an argument (I found out after researching a little that in ARM assembly, when a function is called, the first four arguments are passed in `w0`, `w1`, `w2`, and `w3` for 32-bit values and `x0`, `x1`, `x2`, and `x3` for 64-bit values).
- the function `func` does the following:
  - first the stack pointer is updated by subtracting 32 from it. This is done to allocate space for the local variables.
  - `w0` (which contains the argument entered by the user) is stored at `[sp, 12]`. `[sp, 12]` means that the value is stored at an offset of 12 from the stack pointer. I will denote this with the notation `sp+12` to keep stuff easy for me.
  - `mov	w0, 83`: this moves the value 83 to `w0`.
  - `str	w0, [sp, 16]`: this stores the value of `w0` (which is 83) at `sp+16`.
  - `str	wzr, [sp, 20]`: I had to look up what `wzr` meant, cuz I had no idea. It turns out that `wzr` is the zero register, which always contains the value 0. So this instruction stores 0 at `sp+20`.
  - `mov	w0, 3`: this moves the value 3 to `w0`.
  - `str	w0, [sp, 24]`: this stores the value of `w0` (which is 3) at `sp+24`.
  - `ldr	w0, [sp, 20]`: this loads the value at `sp+20` (which is `wzr` aka 0) into `w0`.
  - `ldr	w1, [sp, 16]`: this loads the value at `sp+16` (which is 83) into `w1`.
  - `lsl	w0, w1, w0`: `lsl` is the logical shift left operation. It shifts the bits of `w1` to the left by the number of bits specified in `w0`. So, `w1` is shifted left by 0 bits. This means that no operation is performed and the value of `w1` and this result is stored in `w0`. In other words, `w1`'s value is copied in `w0` which is 83.
  - `str	w0, [sp, 28]    ldr	w1, [sp, 28]`: These two instructions basically copy the value of `w0` (which is 83) to `w1` (which is already 83). This is a redundant operation.
  - `ldr	w0, [sp, 24]`: this loads the value at `sp+24` (which is 3) into `w0`.
  - `sdiv	w0, w1, w0`: `sdiv` is the signed division operation. It basically does `w1 // w0` and stores the result in `w0`. So 83 // 3 is 27 and this is stored in `w0`.
  - `str	w0, [sp, 28]    ldr	w1, [sp, 28]`: These two instructions basically copy the value of `w0` (which is 27) to `w1` (which was 83 earlier).
  - `ldr	w0, [sp, 12]`: this loads the value at `sp+12` (which is the argument entered by the user) into `w0`.
  - `sub	w0, w1, w0`: this subtracts the value of `w0` (which is 27) from the value of `w1` (which is the argument entered by the user) and stores the result in `w0`. So, `27 - argument` is stored in `w0`.
  - `str	w0, [sp, 28]    ldr	w0, [sp, 28]`: These operations are pretty much redundant. 
  - `add	sp, sp, 32  ret`: these two instructions basically deallocate the space allocated for the local variables and returns to the main function.
- Back in main:
  - `cmp	w0, 0   bne	.L4`: this compares the value of `w0` (which is the return value of the function `func`) with 0. If the value is not equal to 0, it jumps to `.L4`.
```assembly
.L4:
	adrp	x0, .LC1
	add	x0, x0, :lo12:.LC1
	bl	puts
```
- `.LC1` contains the string "You Lose :(". This string is printed if the return value of the function `func` is not 0.
```assembly
.LC0:
	.string	"You win!"
	.align	3
.LC1:
	.string	"You Lose :("
	.text
	.align	2
	.global	main
	.type	main, %function
```
- Continuing in main:
```assembly
adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
    bl	puts
    b	.L6
```
- `.LC0` contains the string "You win!". This string is printed if the return value of the function `func` is 0.
- Then the program jumps to `.L6`. `.L6` performs some cleanup operations and the program is terminated.
- So, to get the program to print "You win!", the expression `27 - argument` should be equal to 0. This means that `argument` should be equal to 27.
- Running the following commands to confirm that our analysis is correct:
```bash
as -o chall_1.o chall_1.S
gcc -o chall_1 chall_1.o -lc
./chall_1 27
You win!
```
- The flag is `picoCTF{0000001b}`.