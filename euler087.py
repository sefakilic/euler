import math
import itertools


# primes
def is_prime(n):
    sq = int(math.sqrt(n) + 1)
    return not any(x for x in xrange(3, sq+1) if n % x ==0)
def primes(below):
    return [2, 3, 5] + [x for x in xrange(7, below, 2) if is_prime(x)]

def euler_87(max_num=50000000):
    pr = primes(int(math.pow(max_num, .5) + 1))

    weird_nums = set()

    for x in pr:
        for y in pr:
            for z in pr:
                n =x**2 + y**3 + z**4
                if n > max_num:
                    break
                weird_nums.add(n)
                #print "%d^2 + %d^3 + %d^4 = %d" % (x, y, z, n)
                    
    return len(weird_nums)

        
            
