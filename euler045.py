t_last = 285 # last index for triangle number
p_last = 1 # last index for pentagonal
h_last = 1 # last index for hexagonal

pentagonal = 1
hexagonal = 1

while True:
    t_last += 1
    triangle = t_last * (t_last+1) / 2
    while triangle > pentagonal: # generate some pentagonal numbers
        p_last += 1
        pentagonal = p_last * (3*p_last - 1) / 2
    while triangle > hexagonal: # generate some hexagonal numbers
        h_last += 1
        hexagonal = h_last * (2*h_last - 1)
    if triangle == pentagonal and triangle  == hexagonal:
        print triangle
        break
