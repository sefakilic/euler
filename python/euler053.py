def fac(x):
    if x == 0: return 1
    else:
        return reduce(lambda a,b: a*b, xrange(1,x+1))
def comb(n, r):
    return fac(n) / fac(r) / fac(n-r)

how_many = 0
for n in xrange(1, 101):
    for r in xrange(n+1):
        if comb(n, r) > 1000000:
            how_many += 1

print how_many
