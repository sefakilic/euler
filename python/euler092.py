to_89 = set([89])
to_1 = set([1])


for i in xrange(2, 10**7):
    t = i
    hist = []
    while t not in to_89 and t not in to_1:
        hist.append(t)
        tmp = t
        t = 0
        while tmp > 0:
            t += (tmp % 10)**2
            tmp = tmp // 10
    if t in to_89:
        for h in hist:
            to_89.add(h)
    if t in to_1:
        for h in hist:
            to_1.add(h)

        

print len(to_89)

assert len(to_89) == 8581146
