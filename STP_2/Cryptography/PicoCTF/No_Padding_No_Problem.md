# No Padding, No Problem
## Description
Oracles can be your best friend, they will decrypt anything, except the flag's ciphertext. How will you break it? Connect with `nc mercury.picoctf.net 2671`.
## Hint
What can you do with a different pair of ciphertext and plaintext? What if it is not so different after all...
## Solution 
- Connecting with the server and sending some test data:
```
Welcome to the Padding Oracle Challenge
This oracle will take anything you give it and decrypt using RSA. It will not accept the ciphertext with the secret message... Good Luck!


n: 97520836411547065507997325976160016056255539981240838514633722100578554237958761569137431311065762769163000984198687462048439870481973456611024411253656496727731714786545308721658512908810030806253888703593313870688695004268603287622492597683268815685146045370326340612504399066851775984371792763665128053111
e: 65537
ciphertext: 95516799456191931069996464229349071617558662985683420286968677211962962586076024461753095512302456478162426927024465965258833849091935435517931167438382286562852046865086765876135383513281648326312724389455523782691580416727607276350982891021050282776263875707867896741619873188631455609070662317332764233938


Give me ciphertext to decrypt: 1
Here you go: 1
Give me ciphertext to decrypt: 0
Here you go: 0
Give me ciphertext to decrypt: 2
Here you go: 29943634396768922586901152771854419904237213433429283410428636041935839059514796153985986295949975834592002692218664834150204906543552939763387719018464774237555337552263155675828267196288408714751742617784785286190930023241077677140793091148909131072799645191780133420468928265612165157700904359594969054204
Give me ciphertext to decrypt: 95516799456191931069996464229349071617558662985683420286968677211962962586076024461753095512302456478162426927024465965258833849091935435517931167438382286562852046865086765876135383513281648326312724389455523782691580416727607276350982891021050282776263875707867896741619873188631455609070662317332764233938
Will not decrypt the ciphertext. Try Again!
```
- The oracle seems to be performing textbook RSA. As expected, it will not decrypt the flag's ciphertext.
- we can exploit the fact that `c^d mod N` is the same as `(c+N)^d mod N` and use it to get the flag.
- wrote the following script to get the flag:
```python
from pwn import remote
from Crypto.Util.number import long_to_bytes

# Connect to the server
HOST = 'mercury.picoctf.net'
PORT = 2671 
conn = remote(HOST, PORT)

print(conn.recvuntil('n: ').decode())
n = int(conn.recvline().decode().strip())
print(n)

print(conn.recvuntil('ciphertext: ').decode())
ciphertext = int(conn.recvline().decode().strip())
print(ciphertext)

print(conn.recvuntil(': ').decode())
conn.sendline(str(n+ciphertext).encode())

print(conn.recvuntil(': ').decode())
flag = conn.recvline().decode().strip()
print(long_to_bytes(int(flag)).decode())

conn.close()
```
- The script sends the server `n+ciphertext` and receives the decrypted flag.
- Running the script gives us the flag:
```
[+] Opening connection to mercury.picoctf.net on port 2671: Done
/Users/Dhruv1/Desktop/playground/SP/Taskphase/Cryptonite/cryptonite_taskphase_dhruv/STP_2/Cryptography/PicoCTF/No_Padding_No_Problem.py:9: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  print(conn.recvuntil('n: ').decode())
Welcome to the Padding Oracle Challenge
This oracle will take anything you give it and decrypt using RSA. It will not accept the ciphertext with the secret message... Good Luck!


n: 
74380671579845226599917321643106099798931784447793202222204065545033009588004165058120904715976360388585459966267901526893646880614274979352086136263519253791422797744400857628204047628560393478274072911390178982277704307175177800572223889189068898517857870414166635911354954343216720775233565649971976528053
/Users/Dhruv1/Desktop/playground/SP/Taskphase/Cryptonite/cryptonite_taskphase_dhruv/STP_2/Cryptography/PicoCTF/No_Padding_No_Problem.py:13: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  print(conn.recvuntil('ciphertext: ').decode())
e: 65537
ciphertext: 
41991921350588777214449768500593896218553826577986340419583643468677254219427641904726776871686038037863261740582737681004753056528535479922830983895300817071167651397897730899633082506417561036429759295916285847256638126650240575917070221190882417072641462019441377828756518345246166923910049742891591674260
/Users/Dhruv1/Desktop/playground/SP/Taskphase/Cryptonite/cryptonite_taskphase_dhruv/STP_2/Cryptography/PicoCTF/No_Padding_No_Problem.py:17: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  print(conn.recvuntil(': ').decode())


Give me ciphertext to decrypt: 
/Users/Dhruv1/Desktop/playground/SP/Taskphase/Cryptonite/cryptonite_taskphase_dhruv/STP_2/Cryptography/PicoCTF/No_Padding_No_Problem.py:20: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  print(conn.recvuntil(': ').decode())
Here you go: 
picoCTF{m4yb3_Th0se_m3s54g3s_4r3_difurrent_5814368}
[*] Closed connection to mercury.picoctf.net port 2671
```