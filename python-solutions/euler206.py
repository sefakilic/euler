"""
I think this is not even close to the elegant solution, anyway.

n = 1_2_3_4_5_6_7_8_9_0

since last dig is 0, before that is 0 too
n = 1_2_3_4_5_6_7_8_900

and the numbr we are looking for is x

sqrt(1020304050607080900) <= x <= sqrt(1929394959697989900)

and since third dig from end is 9, last two digit of x should be either 30 or 70
"""

import math
s = int(math.sqrt(1020304050607080900)) / 100 * 100 + 30
l = int(math.sqrt(1929394959697989900))

x = s
while x < l:
    if str(x**2)[::2] == "1234567890":
        print x
        print x**2
        break
    if x % 100 == 30:
        x += 40
    else:
        x += 60

# well, after I solved it and looked at other solutions, mine is not that bad
# :D, same solution with Robert Gerbicz  
