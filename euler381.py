import math

fac = lambda x: math.factorial(x)

def euler_381(pmin, pmax):
    fac_list = [fac(pmin-1), fac(pmin-2), fac(pmin-3), fac(pmin-4), fac(pmin-5)]
    mod_sum = sum(fac_list) % pmin
    for x in xrange(pmin+1, pmax):
        fac_list = [x*fac_list[0]] + fac_list[:-1]
        print fac_list
        mod_sum += sum(fac_list) % x

    return mod_sum
        

    
