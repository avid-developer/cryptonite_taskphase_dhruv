# vault-door-7
## Description
This vault uses bit shifts to convert a password string into an array of integers. Hurry, agent, we are running out of time to stop Dr. Evil's nefarious plans! The source code for this vault is here: [VaultDoor7.java](./VaultDoor7.java)
## Hints
- Use a decimal/hexadecimal converter such as this one: https://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html
- You will also need to consult an ASCII table such as this one: https://www.asciitable.com/
## Solution
- Looking at the source code [VaultDoor7.java](./VaultDoor7.java):
```java
import java.util.*;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.*;

class VaultDoor7 {
    public static void main(String args[]) {
        VaultDoor7 vaultDoor = new VaultDoor7();
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

    // Each character can be represented as a byte value using its
    // ASCII encoding. Each byte contains 8 bits, and an int contains
    // 32 bits, so we can "pack" 4 bytes into a single int. Here's an
    // example: if the hex string is "01ab", then those can be
    // represented as the bytes {0x30, 0x31, 0x61, 0x62}. When those
    // bytes are represented as binary, they are:
    //
    // 0x30: 00110000
    // 0x31: 00110001
    // 0x61: 01100001
    // 0x62: 01100010
    //
    // If we put those 4 binary numbers end to end, we end up with 32
    // bits that can be interpreted as an int.
    //
    // 00110000001100010110000101100010 -> 808542562
    //
    // Since 4 chars can be represented as 1 int, the 32 character password can
    // be represented as an array of 8 ints.
    //
    // - Minion #7816
    public int[] passwordToIntArray(String hex) {
        int[] x = new int[8];
        byte[] hexBytes = hex.getBytes();
        for (int i=0; i<8; i++) {
            x[i] = hexBytes[i*4]   << 24
                 | hexBytes[i*4+1] << 16
                 | hexBytes[i*4+2] << 8
                 | hexBytes[i*4+3];
        }
        return x;
    }

    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        int[] x = passwordToIntArray(password);
        return x[0] == 1096770097
            && x[1] == 1952395366
            && x[2] == 1600270708
            && x[3] == 1601398833
            && x[4] == 1716808014
            && x[5] == 1734304867
            && x[6] == 942695730
            && x[7] == 942748212;
    }
}
```
- the code first converts the entered string into a hex byte array.
- it then "packs" 4 bytes into a single int (which has 32 bits) using bit shifts and stores it in an array of 8 ints.
- it then compares the 8 ints with the following values:
  - 1096770097
  - 1952395366
  - 1600270708
  - 1601398833
  - 1716808014
  - 1734304867
  - 942695730
  - 942748212
- if it matches, then our entered string is the correct password.
- we can get the password by converting the above values to hex and then to ascii.
- i used [this](https://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html) tool to convert the values to hex, and then put the hex values in [this](https://www.rapidtables.com/convert/number/hex-to-ascii.html) tool one-by-one to get the password.
- the final hex string is `415F6231745F30665F6231745F7368316654694E675F64633830653238313234` which converts to `A_b1t_0f_b1t_sh1fTiNg_dc80e28124`.
- the flag is `picoCTF{A_b1t_0f_b1t_sh1fTiNg_dc80e28124}`.
```
java VaultDoor7
Enter vault password: picoCTF{A_b1t_0f_b1t_sh1fTiNg_dc80e28124}
Access granted.
```