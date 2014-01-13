sum_digits = lambda n: sum(ord(c)-ord('0') for c in str(n))
print max(sum_digits(a**b) for a in xrange(100) for b in xrange(100))
