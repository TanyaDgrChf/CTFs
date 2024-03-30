from Crypto.Util.number import isPrime, bytes_to_long
import random
import os
import script

with open('output.txt', 'r') as f:
    n = f.readline()
    n = int(n.strip().split('=')[1])

checked = []

found = False
num_prime = 1  # Start from the 1st prime
while not found:
    curr = script.getNthWYSIprime(num_prime)
    if n % curr == 0:
        potential = n // curr
        s_potential = str(potential)
        if all(digit in '27' for digit in s_potential):
            found = True
    num_prime += 1
    if len(str(curr)) > 544:
        print('bro you suck')
        break
    print(curr)

print("The WYSI prime that divides n evenly is:", curr)

