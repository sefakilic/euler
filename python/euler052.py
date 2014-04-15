def check(n):
    return (sorted(str(n)) == sorted(str(2*n)) ==
            sorted(str(3*n)) == sorted(str(4*n)) == 
            sorted(str(5*n)) == sorted(str(6*n)))

x = 1
while True:
    if check(x): break
    x += 1

print x

    
