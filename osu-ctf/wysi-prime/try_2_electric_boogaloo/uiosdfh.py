def largest_smallest_divisors(n):
    # Find the largest prime factor of n
    largest_prime_divisor = 1
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            largest_prime_divisor = divisor
            break

    # Largest divisor is n divided by the largest prime factor
    largest_divisor = n // largest_prime_divisor

    # Find the smallest divisor
    smallest_divisor = 1
    for divisor in range(2, largest_divisor + 1):
        if n % divisor == 0:
            smallest_divisor = divisor
            break

    return largest_divisor, smallest_divisor

# Example usage
with open('output.txt', 'r') as f:
    n = f.readline()
    n = int(n.strip().split('=')[1])
largest_divisor, smallest_divisor = largest_smallest_divisors(n)

print("Largest divisor:", largest_divisor)
print("Smallest divisor:", smallest_divisor)
