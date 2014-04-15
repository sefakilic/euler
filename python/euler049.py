import math
def is_prime(n):
    sq = int(math.sqrt(n))
    for i in xrange(2, sq+1):
        if n%i == 0:
            return False
    return True

def perm_each_other(a, b, c):
    return sorted(str(a)) == sorted(str(b)) == sorted(str(c))



for a in xrange(1000, 10000):
    b = a + 3330
    c = b + 3330
    if is_prime(a) and is_prime(b) and is_prime(c) and perm_each_other(a,b,c):
        print a, b, c
        



