# Open the file and read the lines
f = open('data.txt').readlines()

# Open a binary file for writing
with open('data.latm', 'wb') as ff:
    for i in f:
        # Remove colons from the hex string
        clean_hex = i.strip().replace(':', '')
        
        # Convert the cleaned hex string to bytes
        data = bytes.fromhex("FFF1108052DFFD") + bytes.fromhex(clean_hex)
        
        # Write the bytes to the output file
        ff.write(data)

# Close the file
ff.close()
