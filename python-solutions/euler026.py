def recurring_cycle(d):
    nominator = 1
    denominator = d
    hist = [] # previous nominators

    while nominator not in hist and nominator != 0:
        hist.append(nominator)
        while nominator < denominator:
            nominator *= 10
        nominator = nominator - (nominator // d) * d

    return hist, nominator

max_d = 2
max_recurring = 0
for d in xrange(2, 1000):
    hist, nom = recurring_cycle(d)
    if nom != 0:
        if max_recurring < len(hist) - hist.index(nom):
            max_recurring = len(hist) - hist.index(nom)
            max_d = d

print max_d, max_recurring


