def is_lychrel(n):
    # lychrel if less than 50 iterations
    for i in xrange(50):
        n = int(str(n)[::-1]) + n
        if str(n) == str(n)[::-1]:
            return False
    return True

print sum(1 for i in xrange(10000) if is_lychrel(i))
    
