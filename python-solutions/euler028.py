"""
the numbers on diagonals go in the following pattern
1 (inc by 2)
3 5 7 9  (inc by 4)
13 17 21 25 (inc by 6)
31 37 43 49 (inc by 8)
..
..
"""

#in 1001x1001 spiral, there are 501 rows of such numbers
last = 1 #last number in seq
s = 1    #summation of numbers
inc = 2  #increment by
for i in xrange(500):
    for j in range(4):
        last += inc
        s += last
    inc += 2
    

print s
