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