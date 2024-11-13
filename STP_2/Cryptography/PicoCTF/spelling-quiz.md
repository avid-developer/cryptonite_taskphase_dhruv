# spelling-quiz
## Descriotion
I found the flag, but my brother wrote a program to encrypt all his text files. He has a spelling quiz study guide too, but I don't know if that helps.
## Downloads
- [public.zip](./public.zip)
## Solution
- Extracting the zip file the folder [public](./public) is created which contains 3 files: [study-guide.txt](./public/study-guide.txt), [encrypt.py](./public/encrypt.py) and [flag.txt](./public/flag.txt).
- The [study-guide.txt](./public/study-guide.txt) file contains a lot of encrypted text.
```bash
Dhruv1@MacBook-Air public % head study-guide.txt
gocnfwnwtr
sxlyrxaic
dcrrtfrxcv
uxbvwavcq
lwvicwtiwm
pwtmwnxvicq
avingciisa
ylwtmrcawx
mwaxdcrrxuwlwvq
yciflwnf
Dhruv1@MacBook-Air public % wc -l study-guide.txt 
  272543 study-guide.txt
```
- The [encrypt.py](./public/encrypt.py) file contains the code to encrypt the text.
```python
import random
import os

files = [
    os.path.join(path, file)
    for path, dirs, files in os.walk('.')
    for file in files
    if file.split('.')[-1] == 'txt'
]

alphabet = list('abcdefghijklmnopqrstuvwxyz')
random.shuffle(shuffled := alphabet[:])
dictionary = dict(zip(alphabet, shuffled))

for filename in files:
    text = open(filename, 'r').read()
    encrypted = ''.join([
        dictionary[c]
        if c in dictionary else c
        for c in text
    ])
    open(filename, 'w').write(encrypted)
```
- The [flag.txt](./public/flag.txt) file contains the encrypted flag.
```plaintext
brcfxba_vfr_mid_hosbrm_iprc_exa_hoav_vwcrm
```
- Upon analysing the code we can see that the code is implementing a simple substitution cipher. The code is shuffling the alphabets and then creating a dictionary with the shuffled alphabets. Then it is reading the text from the file and encrypting it using the dictionary.
- I used [this](https://www.guballa.de/substitution-solver) online tool to decrypt the text.
- Flag: `picoCTF{perhaps_the_dog_jumped_over_was_just_tired}`
- Key: 
```
abcdefghijklmnopqrstuvwxyz     This clear text ...
sprgwhkjoqzldcuvyemnbtiafx     ... maps to this cipher text
```