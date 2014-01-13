def is_pandigital(s):
    return len(s)==9 and all(str(d) in s for d in xrange(1,10))

num = 1

while num<10**4: # if num >= 10**4, since n>1 concat product will be more than 9 digits
    concat = ""
    n = 0
    while len(concat) < 9:
        n += 1
        concat += str(num*n)
    if is_pandigital(concat):
        print concat

    num += 1
