# Initial hex array
buf = [0xc8, 0xe2, 0x20, 0xcc, 0xe2, 0x28, 0xc4, 0xfa, 0x26, 0xc7, 0xfb, 0xf9, 
       0xc8, 0xe4, 0x38, 0xcb, 0xf5, 0x21, 0xc3, 0xef, 0x3d, 0xde, 0xe5, 0x2a,
       0xd7, 0x25, 0x33, 0xc9, 0xe6]

# First XOR operations
for i in range(len(buf)):
    if i % 3 == 0:
        buf[i] ^= 0xEC
    elif i % 3 == 1:
        buf[i] ^= 0xCB
    elif i % 3 == 2:
        buf[i] ^= 3

# Swap buf[6] and buf[11]
buf[6], buf[11] = buf[11], buf[6]

# Second XOR operations
for i in range(len(buf)):
    if i % 2 == 0:
        buf[i] ^= 0xD7
    else:
        buf[i] ^= 0x1F

# Swap buf[6] and buf[25]
buf[6], buf[25] = buf[25], buf[6]

# Final XOR operations
for i in range(len(buf)):
    if i % 2 == 0:
        buf[i] ^= 0x9D
    else:
        buf[i] ^= 0x5C

# Convert buf to string
result = ''.join([chr(x) for x in buf])
print(result)