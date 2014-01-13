def fact(n):
    return reduce(lambda x,y: x*y, xrange(1,n+1))

# the answer to question is C(40,20).
# the number of total moves is 80 (40 right, 40 down)
# the answer is how to choose 40 right(down) out of 80.
print fact(40) / fact(20) / fact(20)
