import math

def primes(n=1000000):
    n = 1000000
    arr = [True for x in xrange(0,n+1)]
    arr[0] = False # not prime
    arr[1] = False # not prime

    for i in xrange(2, int(math.sqrt(n))+1):
        pr = i # this is prime
        for j in xrange(2*pr, n+1, pr):
            arr[j] = False

    return (i for i in xrange(n+1) if arr[i] == True)

def is_circular(n, primes):
    """Find all rotations of n and check if prime"""
    strn = str(n)
    for i in xrange(len(strn)):
        strn = strn[-1]+strn[:-1]
        if int(strn) not in primes:
            return False
    return True

all_primes = list(primes())
print len(all_primes)

circular_primes = [x for x in all_primes if is_circular(x, all_primes)]
print len(circular_primes)
