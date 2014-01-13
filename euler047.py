import math

def is_prime(n):
    sq = int(math.sqrt(n))
    for i in xrange(2, sq+1):
        if n%i == 0:
            return False
    return True

def gen_some_primes(primes):
    l = len(primes)
    n = primes[-1]+2
    while len(primes) < 2*l:
        if is_prime(n):
            primes.append(n)
        n += 2
    return primes

def how_many_distinct(n):
    global primes
    dist = 0
    i = 0
    while n > 1:
        if i >= len(primes):
            primes = gen_some_primes(primes)

        if n % primes[i] == 0:
            dist += 1
            while n % primes[i] == 0:
                n /= primes[i]
        i += 1
    return dist


primes = [2,3,5,7]
n = 2
while (how_many_distinct(n) != 4 or
       how_many_distinct(n+1) != 4 or
       how_many_distinct(n+2) != 4 or
       how_many_distinct(n+3) != 4):
    n += 1

print n



