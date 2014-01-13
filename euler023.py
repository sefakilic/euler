# all numbers greater than 28123 can be written as sum of two abundant numbers

def is_abundant(n):
    if n <= 1: return False
    
    sum_divisors = 1
    for i in xrange(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            sum_divisors += (i + n/i)
    if int(math.sqrt(n))**2 == n:
        # means we added that number twice
        sum_divisors -= int(math.sqrt(n))
        
    return sum_divisors > n

abundants = filter(is_abundant, xrange(28124))

can_written = [False for x in xrange(28124)]

can_written[0] = True
for a in abundants:
    for b in abundants:
        if a+b < len(can_written):
            can_written[a+b] = True

print sum(i for i,b in enumerate(can_written) if not b)
#print abundants[:10]
