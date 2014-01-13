fibs = [1, 2]
while fibs[-1] <= 4000000:
    fibs.append(fibs[-1]+fibs[-2])
print sum((x for x in fibs if x%2==0))

