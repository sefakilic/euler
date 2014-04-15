import itertools

def has_property(n):
    s = str(n)
    primes = (2, 3, 5, 7, 11, 13, 17)
    for i in xrange(7):
        if int(s[i+1:i+4]) % primes[i] != 0:
            return False
    return True

digs = (0,1,2,3,4,5,6,7,8,9)
s = 0
for p in itertools.permutations(digs):
    num = reduce(lambda x,y: x*10+y, p)
    if has_property(num):
        print num
        s += num

print 'sum:', s

