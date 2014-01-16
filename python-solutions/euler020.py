
fact = reduce(lambda x,y: x*y, xrange(1,101))
print sum(int(c) for c in str(fact))
