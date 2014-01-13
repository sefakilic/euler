import math
def sum_divisors(n):
    divisors = [1] #1 is divisor, don't forget
    for i in xrange(2,int(math.sqrt(n))+1):
        if n%i==0:
            divisors.append(i)
            divisors.append(n/i)
    return sum(divisors)

def is_amicable(n):
    p = sum_divisors(n)
    if p == n: return False
    else:
        return n == sum_divisors(p)

print sum(x for x in xrange(10000) if is_amicable(x))

            
