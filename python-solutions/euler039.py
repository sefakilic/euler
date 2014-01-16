def how_many(p):
    sols = 0
    for a in xrange(1,p):
        for b in xrange(a, p):
            c = p - a - b
            if c < b:
                break
            if a**2 + b**2 == c**2:
                sols += 1
    return sols

max_p = 0
max_sols = 0

for i in xrange(1001):
    t = how_many(i)
    if t > max_sols:
        max_p, max_sols = i, t

print max_p


