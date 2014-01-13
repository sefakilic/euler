for a in xrange(10,100):
    for b in xrange(a+1, 100):
        if a%10 == b//10 and b%10 != 0 and ((a//10)*1.0) / (b%10) == (a*1.0) /b:
            print a,b
            
"""
Only 4 such fractions exist.
16/64
19/95
26/65
49/98

Multiplication of them in lowest common term is 2/200 = 1/100
"""
