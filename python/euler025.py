fiba = 1
fibb = 1
term = 2 # second fibonacci so far
while len(str(fibb)) < 1000:
    fiba,fibb = fibb, fiba+fibb
    term += 1

print term
