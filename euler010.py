import math

n = 2000000
arr = [True for x in xrange(0,n+1)]
arr[0] = False # not prime
arr[1] = False # not prime

for i in xrange(2, int(math.sqrt(n))+1):
    pr = i # this is prime
    for j in xrange(2*pr, n+1, pr):
        arr[j] = False

print sum (i for i in xrange(n+1) if arr[i] == True)
