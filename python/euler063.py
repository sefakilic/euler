"""
lets n_d be d digit number. 10^(d-1) <= n_d < 10^d

Therefore if n_d is also a dth power, n_d < 10^d

Assume that, for some d (d = 22), 9^d is less than d digits.
9 * 9^d = 9^(d+1) must be less than d+1 digits. Because, even 
10 * 9^d is less than d+1 digits.

For d >= 22, 9^d < n_d < 10^d, therefore, no number with d digits
which is also a dth power.
"""

how_many = 0
for d in xrange(1, 22):
    for x in xrange(1,10):
        if len(str(x**d)) == d:
            print 'd = %d, n = %d' % (d, x**d)
            how_many += 1

print how_many

