import math
def is_prime(n):
    if n < 2: return False
    sq = int(math.sqrt(n))
    for i in xrange(2, sq+1):
        if n%i == 0:
            return False
    return True

def is_truncatable_right(n):
    #right truncatable
    while n>0:
        if not is_prime(n): return False
        n = (n - n%10) / 10
    return True

def is_truncatable_left(n):
    n = str(n)
    while n:
        if not is_prime(int(n)): return False
        n = n[1:]
    return True

n = 11
ts = []
while len(ts) < 11:
    if is_truncatable_right(n) and is_truncatable_left(n):
        ts.append(n)
    n += 2

print ts
print sum(ts)
