"""
Diagonals go like this (first one is 1) (side length=1)
diagonals 3 5 7 9 (2)           - side length = 3
         13 17 21 25 (4)        - side length = 5
         31 37 43 49 (6)        - side length = 7
         55 ..       (8)        - side length = 9
"""

import math

def is_prime(n):
    for i in xrange(2, int(math.sqrt(n))+2):
        if n % i == 0:
            return False
    return True

def prime_ratio(primes, not_primes):
    return float(len(primes)) / (len(primes) + len(not_primes))

diag_primes = [3, 5, 7]
diag_not_primes = [1, 9]
side_length = 3

while prime_ratio(diag_primes, diag_not_primes) >= 0.1:
    side_length += 2

    diags = [side_length**2,
             side_length**2 - (side_length-1),
             side_length**2 - 2*(side_length-1),
             side_length**2 - 3*(side_length-1)]

    for d in diags:
        if is_prime(d):
            diag_primes.append(d)
        else:
            diag_not_primes.append(d)


print side_length    
