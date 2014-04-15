import math
def is_prime(n):
    sq = int(math.sqrt(n))
    for i in xrange(2, sq+1):
        if n%i == 0:
            return False
    return True

def get_primes(below=1000000):
    p = [2]
    for x in xrange(3, below, 2):
        if is_prime(x):
            p.append(x)

    return p

primes = get_primes()

max_consec = 0
max_p = 0
for i in xrange(0, len(primes)):
    for j in xrange(i+1, len(primes)):
        s = sum(primes[i:j])
        if s >= 10**6: break
        if is_prime(s) and j-i > max_consec:
            max_consec = j-i
            max_p = s
        
print max_p
            
        
