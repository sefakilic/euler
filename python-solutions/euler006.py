sum1 = sum((x**2 for x in xrange(101)))
sum2 = sum(x for x in xrange(101))**2
print abs(sum1-sum2)
