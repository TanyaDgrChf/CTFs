# Load the known plaintext and corresponding ciphertext
with open("flag.osu", 'rb') as f:
    known_plaintext = f.read()
with open("flag.osu.enc", 'rb') as f:
    ciphertext = f.read()

# Perform XOR operation between known plaintext and ciphertext to recover the key
key = bytes([known_plaintext[i] ^ ciphertext[i] for i in range(len(known_plaintext))])

print("Recovered XOR key:", key)

# Use the recovered key to decrypt other ciphertexts
# (Assuming they were encrypted with the same key)
