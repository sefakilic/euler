def is_pali(n):
    decstr = str(n)
    binstr = bin(n)[2:]
    return decstr == decstr[::-1] and binstr == binstr[::-1]

print sum(n for n in xrange(1000000) if is_pali(n))
