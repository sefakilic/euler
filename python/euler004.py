all_products = (x*y for x in xrange(100,1000) for y in xrange(100,1000))
palindromes = (p for p in all_products if str(p)==(str(p)[::-1]))
print max(palindromes)

