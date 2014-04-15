import math

def how_many_divisors(n):
    num_divisors = 0
    sq = int(math.sqrt(n))
    for i in xrange(1,sq):
        if n%i == 0:
            num_divisors += 2
    if n%sq == 0:
        num_divisors += 1
    return num_divisors

n = 1
while True:
    tr = n * (n+1) / 2
    if how_many_divisors(tr) > 500:
        print tr
        break
    n = n+1

