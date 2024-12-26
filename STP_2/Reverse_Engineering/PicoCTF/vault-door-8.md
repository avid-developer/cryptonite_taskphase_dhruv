# vault-door-8
## Description
Apparently Dr. Evil's minions knew that our agency was making copies of their source code, because they intentionally sabotaged this source code in order to make it harder for our agents to analyze and crack into! The result is a quite mess, but I trust that my best special agent will find a way to solve it. The source code for this vault is here: [VaultDoor8.java](./VaultDoor8.java)
## Hints
- Clean up the source code so that you can read it and understand what is going on.
- Draw a diagram to illustrate which bits are being switched in the scramble() method, then figure out a sequence of bit switches to undo it. You should be able to reuse the switchBits() method as is.
## Solution
- Looking at the source code [VaultDoor8.java](./VaultDoor8.java):
```java
// These pesky special agents keep reverse engineering our source code and then
// breaking into our secret vaults. THIS will teach those sneaky sneaks a
// lesson.
//
// -Minion #0891
import java.util.*; import javax.crypto.Cipher; import javax.crypto.spec.SecretKeySpec;
import java.security.*; class VaultDoor8 {public static void main(String args[]) {
Scanner b = new Scanner(System.in); System.out.print("Enter vault password: ");
String c = b.next(); String f = c.substring(8,c.length()-1); VaultDoor8 a = new VaultDoor8(); if (a.checkPassword(f)) {System.out.println("Access granted."); }
else {System.out.println("Access denied!"); } } public char[] scramble(String password) {/* Scramble a password by transposing pairs of bits. */
char[] a = password.toCharArray(); for (int b=0; b<a.length; b++) {char c = a[b]; c = switchBits(c,1,2); c = switchBits(c,0,3); /* c = switchBits(c,14,3); c = switchBits(c, 2, 0); */ c = switchBits(c,5,6); c = switchBits(c,4,7);
c = switchBits(c,0,1); /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */ c = switchBits(c,3,4); c = switchBits(c,2,5); c = switchBits(c,6,7); a[b] = c; } return a;
} public char switchBits(char c, int p1, int p2) {/* Move the bit in position p1 to position p2, and move the bit
that was in position p2 to position p1. Precondition: p1 < p2 */ char mask1 = (char)(1 << p1);
char mask2 = (char)(1 << p2); /* char mask3 = (char)(1<<p1<<p2); mask1++; mask1--; */ char bit1 = (char)(c & mask1); char bit2 = (char)(c & mask2); /* System.out.println("bit1 " + Integer.toBinaryString(bit1));
System.out.println("bit2 " + Integer.toBinaryString(bit2)); */ char rest = (char)(c & ~(mask1 | mask2)); char shift = (char)(p2 - p1); char result = (char)((bit1<<shift) | (bit2>>shift) | rest); return result;
} public boolean checkPassword(String password) {char[] scrambled = scramble(password); char[] expected = {
0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xD2, 0xD0, 0xB4, 0xE1, 0xC1, 0xE0, 0xD0, 0xD0, 0xE0 }; return Arrays.equals(scrambled, expected); } }
```
- I cleaned up the source code using [this](https://www.tutorialspoint.com/online_java_formatter.htm) online formatter and saved it in a new file [VaultDoor8_formatted.java](./VaultDoor8_formatted.java):
```java
// These pesky special agents keep reverse engineering our source code and then
// breaking into our secret vaults. THIS will teach those sneaky sneaks a
// lesson.
//
// -Minion #0891
import java.util.*;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.*;
class VaultDoor8_formatted {
    public static void main(String args[]) {
        Scanner b = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String c = b.next();
        String f = c.substring(8, c.length() - 1);
        VaultDoor8 a = new VaultDoor8();
        if (a.checkPassword(f)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }
    public char[] scramble(String password) { /* Scramble a password by transposing pairs of bits. */
        char[] a = password.toCharArray();
        for (int b = 0; b < a.length; b++) {
            char c = a[b];
            c = switchBits(c, 1, 2);
            c = switchBits(c, 0, 3); /* c = switchBits(c,14,3); c = switchBits(c, 2, 0); */
            c = switchBits(c, 5, 6);
            c = switchBits(c, 4, 7);
            c = switchBits(c, 0, 1); /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */
            c = switchBits(c, 3, 4);
            c = switchBits(c, 2, 5);
            c = switchBits(c, 6, 7);
            a[b] = c;
        }
        return a;
    }
    public char switchBits(char c, int p1, int p2) {
        /* Move the bit in position p1 to position p2, and move the bit
        that was in position p2 to position p1. Precondition: p1 < p2 */
        char mask1 = (char)(1 << p1);
        char mask2 = (char)(1 << p2); /* char mask3 = (char)(1<<p1<<p2); mask1++; mask1--; */
        char bit1 = (char)(c & mask1);
        char bit2 = (char)(c & mask2);
        /* System.out.println("bit1 " + Integer.toBinaryString(bit1));
        System.out.println("bit2 " + Integer.toBinaryString(bit2)); */
        char rest = (char)(c & ~(mask1 | mask2));
        char shift = (char)(p2 - p1);
        char result = (char)((bit1 << shift) | (bit2 >> shift) | rest);
        return result;
    }
    public boolean checkPassword(String password) {
        char[] scrambled = scramble(password);
        char[] expected = {
            0xF4,
            0xC0,
            0x97,
            0xF0,
            0x77,
            0x97,
            0xC0,
            0xE4,
            0xF0,
            0x77,
            0xA4,
            0xD0,
            0xC5,
            0x77,
            0xF4,
            0x86,
            0xD0,
            0xA5,
            0x45,
            0x96,
            0x27,
            0xB5,
            0x77,
            0xD2,
            0xD0,
            0xB4,
            0xE1,
            0xC1,
            0xE0,
            0xD0,
            0xD0,
            0xE0
        };
        return Arrays.equals(scrambled, expected);
    }
}
```
- the `scramble()` method passes each character of the password to multiple `switchBits()` calls. The `switchBits()` method takes a character and two positions `p1` and `p2` and swaps the bits at those positions. The `checkPassword()` method compares the scrambled password with the expected password.
- to get the password, we need to reverse the scrambling process. We can do this by reversing the order of the `switchBits()` calls in the `scramble()` method.
- wrote the following script [VaultDoor8_solve.java](./VaultDoor8_solve.java) to get the password:
```java
public class VaultDoor8_solve
{
    public static void main(String[] args)
    {
        char[] expected = {
            0xF4,
            0xC0,
            0x97,
            0xF0,
            0x77,
            0x97,
            0xC0,
            0xE4,
            0xF0,
            0x77,
            0xA4,
            0xD0,
            0xC5,
            0x77,
            0xF4,
            0x86,
            0xD0,
            0xA5,
            0x45,
            0x96,
            0x27,
            0xB5,
            0x77,
            0xD2,
            0xD0,
            0xB4,
            0xE1,
            0xC1,
            0xE0,
            0xD0,
            0xD0,
            0xE0
        };
        for (int b = 0; b < expected.length; b++) {
            char c = expected[b];
            c = switchBits(c, 6, 7);
            c = switchBits(c, 2, 5);
            c = switchBits(c, 3, 4);
            c = switchBits(c, 0, 1);
            c = switchBits(c, 4, 7);
            c = switchBits(c, 5, 6);
            c = switchBits(c, 0, 3);
            c = switchBits(c, 1, 2);
            expected[b] = c;
        }
        System.out.println(new String(expected));
    }
    public static char switchBits(char c, int p1, int p2) {
        /* Move the bit in position p1 to position p2, and move the bit
        that was in position p2 to position p1. Precondition: p1 < p2 */
        char mask1 = (char)(1 << p1);
        char mask2 = (char)(1 << p2); /* char mask3 = (char)(1<<p1<<p2); mask1++; mask1--; */
        char bit1 = (char)(c & mask1);
        char bit2 = (char)(c & mask2);
        /* System.out.println("bit1 " + Integer.toBinaryString(bit1));
        System.out.println("bit2 " + Integer.toBinaryString(bit2)); */
        char rest = (char)(c & ~(mask1 | mask2));
        char shift = (char)(p2 - p1);
        char result = (char)((bit1 << shift) | (bit2 >> shift) | rest);
        return result;
    }
}
```
- Running the script gives the password: `s0m3_m0r3_b1t_sh1fTiNg_91c642112`. Hence, the flag is: `picoCTF{s0m3_m0r3_b1t_sh1fTiNg_91c642112}`
```bash
java VaultDoor8
Enter vault password: picoCTF{s0m3_m0r3_b1t_sh1fTiNg_91c642112}
Access granted.
```