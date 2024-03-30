with open("flag.osu.enc", 'rb') as f:
    encrypted_data = f.read()

known_plaintext = b"osu file format "

xor_key = bytes([encrypted_data[i] ^ known_plaintext[i % len(known_plaintext)] for i in range(len(known_plaintext))])

decrypted_data = bytes([encrypted_data[i] ^ xor_key[i % len(xor_key)] for i in range(len(encrypted_data))])

with open("flag.osu", 'wb') as f:
    f.write(decrypted_data)
