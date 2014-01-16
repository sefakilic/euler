def bouncy(n):
    str_n = str(n)
    sorted_str = ''.join(sorted(list(str_n)))
    return not(str_n == sorted_str or str_n == sorted_str[::-1])


num_bouncy = 0
num_not_bouncy = 99 # all 2 digit numbers are not bouncy

i = 99
while float(num_bouncy)/(num_not_bouncy + num_bouncy) < 0.99:
    i += 1
    if bouncy(i):
        num_bouncy += 1
    else:
        num_not_bouncy += 1

print i # least number 

