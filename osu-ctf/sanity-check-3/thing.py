from pwn import *
import base64

# Function to read and encode the replay file to base64
def encode_replay_to_base64(file_path):
    with open(file_path, "rb") as f:
        replay_data = f.read()
    return base64.b64encode(replay_data).decode("utf-8")

# Define the server details
server_address = 'chal.osugaming.lol'
server_port = 7278

# Path to the replay file
replay_file_path = 'replay.osr'  # Replace with the actual path to your replay file

# Encode the replay file to base64
replay_base64 = encode_replay_to_base64(replay_file_path)

# Connect to the server and send the base64 encoded replay
conn = remote(server_address, server_port)
conn.sendline(replay_base64)

# Receive and print the server response
response = conn.recvline().decode().strip()
print("Server response:", response)

# Close the connection
conn.close()
