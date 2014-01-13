import math

def is_prime(n):
    if n<2: return False
    sq = int(math.sqrt(n))
    for i in xrange(2, sq+1):
        if n%i == 0:
            return False
    return True

max_consec_prime = 0
max_a, max_b = -1000, -1000

for a in xrange(-999, 1000):
    for b in xrange(-999, 1000):
        n = 0
        while is_prime(n**2 + a*n + b):
            n += 1
        if max_consec_prime < n+1:
            max_consec_prime = n+1
            max_a, max_b = a, b


print max_a * max_b
