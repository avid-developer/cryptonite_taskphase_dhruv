myBytes = [106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0o0142, 0o0131, 0o0164, 0o063 , 0o0163, 0o0137, 0o070 , 0o0146,
            '4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b']
flag = ""
for i in range(24):
    flag += chr(myBytes[i])
for i in range(24,32):
    flag += myBytes[i]
print("picoCTF{" + flag + "}")