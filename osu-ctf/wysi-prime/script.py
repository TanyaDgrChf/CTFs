from Crypto.Util.number import isPrime, bytes_to_long
import random
import os

def getWYSIprime():
    while True:
        digits = [random.choice("727") for _ in range(272)]
        prime = int("".join(digits))
        if isPrime(prime):
            return prime
        
def getNthWYSIprime(n):
    count = 0
    while True:
        digits = [random.choice("727") for _ in range(272)]
        prime = int("".join(digits))
        if isPrime(prime):
            count += 1
            if count == n:
                return prime


if __name__ == '__main__':
    # RSA encryption using the WYSI primes
    p = getWYSIprime()
    q = getWYSIprime()
    n = p * q
    e = 65537
    flag = bytes_to_long(os.getenv("FLAG", b"osu{fake_flag_for_testing}"))
    ciphertext = pow(flag, e, n)
    print(f"{n = }")
    print(f"{e = }")
    print(f"{ciphertext = }")