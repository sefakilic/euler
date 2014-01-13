import itertools
import math

def is_prime(n):
    sq = math.sqrt(n)
    for i in xrange(2, int(sq)+1):
        if n%i == 0:
            return False
    return True

def largest_pandigital():
    n = 9
    while n>0:
        digs = range(n,0,-1)
        for p in itertools.permutations(digs):
            x = reduce(lambda x,y: x*10+y, p)
            if is_prime(x):
                return x
        n -= 1


