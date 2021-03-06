#!python3
import sys

PRIMES = [2,]

def get_the_prime(n):
    if n < 1 or type(n) != int:
        raise ValueError("n must be a positive integer")
    global PRIMES
    while n > len(PRIMES):
        get_a_prime()
    return PRIMES[int(n)-1]

def get_a_prime():
    last_prime = PRIMES[-1]
    a_number = (last_prime + last_prime % 2) // 2 * 2 + 1
    while True:
        for prime in PRIMES:
            if a_number // 2 < prime:
                PRIMES.append(int(a_number))
                return
            if a_number % prime == 0:
                a_number += 2
                break

if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            count = int(sys.argv[1])
        except ValueError:
            print("Usage: python3 main.py [a positive INTEGER]")
            count = 9
        if count < 1:
            print("Usage: python3 main.py [a POSITIVE integer]")
            count = 9
    else:
        print("Usage: python3 main.py [A positive integer]")
        count = 9
    print(get_the_prime(count))
