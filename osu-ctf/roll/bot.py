import time
import threading
import keyboard

# Function to type "!start" followed by Enter
def type_start():
    keyboard.write("!start")
    keyboard.send("enter")

# Function to type "!roll" followed by Enter
def type_roll():
    keyboard.write("!roll")
    keyboard.send("enter")

# Function to perform typing actions at specified intervals
def perform_actions(interval):
    while True:
        type_start()
        time.sleep(interval)
        type_roll()
        time.sleep(interval)

# Main function
def main():
    interval = 30  # Set the interval in seconds
    perform_actions(interval)

if __name__ == "__main__":
    main()
