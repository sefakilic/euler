
def slow():
    max_steps = 0
    which = 0
    for i in xrange(2,1000000):
        steps = 1
        n = i
        while n>1:
            n = n/2 if n%2==0 else 3*n+1
            steps += 1
        if max_steps < steps:
            max_steps = steps
            which = i

    print which, max_steps

slow()

