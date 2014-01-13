"""The product can't be 5 or more digits.
If the product is at least 5 digits, the multiplicand and multiplier
would be at least 3 digits each, it would be more than 9 digits.
Therefore, product is less than 10^4
"""

def is_pandigital(a,b,c):
    s = str(a) + str(b) + str(c)
    return len(s) == 9 and all(str(x) in s for x in range(1,10))

s = set()
for p in xrange(2, 10**4):
    sq = int(math.sqrt(p))
    for m in xrange(1,sq+1):
        if p%m == 0:
            if is_pandigital(m, p/m, p):
                print m, p/m, p
                s.add(p)

print sum(s)
        
