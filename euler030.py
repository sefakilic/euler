"""
let $x$ be a $d$ digit number that can be written as sum of 5th power of their digits.

10^d > x >= 10^{d-1}
9^5 * d >= x
----------------------
9^5 * d >= 10^{d-1}

So, for any such number with $d$ digits the statement above should be true.
For small values of $d$, it is true, but as $d$ gets larger, the right side increases
faster and at some point it is larger than left side (9^5 * d)

For d = 7, 9^5 ** 7 > 10^6 is False. For d>7 it is false as well. Therefore, d <= 6.
"""
s = 0 # sum of all such numbers
for i in xrange(2,10**6):
    sum_digits = 0
    tmp = i
    while tmp > 0:
        sum_digits += (tmp % 10) ** 5
        tmp = (tmp - (tmp%10)) / 10
    if sum_digits == i:
        print i
        s += i

print 'sum:', s
        
