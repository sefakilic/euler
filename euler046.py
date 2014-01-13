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

def main():
    # p + 2 * x^2, since 2*x^2 is even, p must be odd. Therefore,
    # we don't need 2 in prime numbers list
    primes = [3, 5, 7]
    
    n = 1
    while True:
        n += 2
        if is_prime(n): continue

        # check number can be written as p + 2 * x^2, where p is prime
        i = 0
        while primes[i] < n:
            if int(math.sqrt((n - primes[i]) / 2)) ** 2 == (n-primes[i])/2:
                break
            i += 1
            if i >= len(primes):
                primes = gen_some_primes(primes)
        else:
            print n
            break
    


