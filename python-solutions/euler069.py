gd = {}

def gcd(a,b):
    global gd
    if (a,b) in gd:
        return gd[(a,b)]
    
    if b == 0:
        return a

    gd[a,b] = gcd(b, a - b*(a/b))
    return gd[a,b]

def totient(n):
    cnt = 0
    for x in xrange(2,n):
        if gcd(n,x) == 1:
            cnt += 1
    return cnt + 1


def euler_69(n):
    max_n = 2
    max_to = 2
    for x in xrange(2,n):
        if x % 1000 == 0:
            print x
        t = totient(x)
        if max_to < x / float(t) :
            max_to = t
            max_n = x
            

    return max_n
