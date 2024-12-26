# vault-door-3
## Description
This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](./VaultDoor3.java)
## Hint
Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.
## Solution
- Looking at the code [VaultDoor3.java](./VaultDoor3.java):
```java
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18gb41_u_4_mfr340");
    }
}
```
- We can see that the program takes the input from the user and performs some operations on it using for loops and stores the characters in the `buffer` array. The `buffer` array is then converted to a string and compared with the string `jU5t_a_sna_3lpm18gb41_u_4_mfr340`. If the strings match, the program prints `Access granted.` otherwise it prints `Access denied!`.
- To get the flag, we can just reverse the operations performed using a script.
- Wrote a python script [vault-door-3_solve.py](./vault-door-3_solve.py) to get the flag:
```python
p = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"
buffer = [None] * 32
for i in range (31,16,-2):
    buffer[i] = p[i]
for i in range (16,32,2):
    buffer[i] = p[46-i]
for i in range (8,16):
    buffer[i] = p[23-i]
for i in range (0,8):
    buffer[i] = p[i]
print("picoCTF{" + "".join(buffer) + "}")
```
- Running the script gets us the flag: `picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_1fb380}`
```bash
java VaultDoor3
Enter vault password: picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_1fb380}
Access granted.
```