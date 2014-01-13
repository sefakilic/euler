import math

def is_prime(n):
    sq = int(math.sqrt(n))
    for i in xrange(2, sq+1):
        if n%i == 0:
            return False
    return True

def how_many_helper(n, max_available):
    if n == 0:
        return 1
    if n < 0 or max_available < 2:
        return 0

    prev_prime = max_available-1
    while not is_prime(prev_prime):
        if prev_prime < 2:
            break
        prev_prime -= 1
    return how_many_helper(n-max_available, max_available) + \
           how_many_helper(n, prev_prime) 




def how_many_ways():
    # return the first value between min and max that can be written as the sum
    # of primes in over 5000 ways
    n = 3
    while True:
        ways = how_many_helper(n, n-1)
        print 'n:', n, 'ways:', ways
        if ways > 5000:
            print n
            break

        n +=1
