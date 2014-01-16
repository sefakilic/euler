def reverse(n):
    return int(str(n)[::-1])

def is_reversible(n):
    if not any(x in str(n + reverse(n)) for x in "24680"):
        return n

    
def euler_145(limit=10**9):
    reversibles = []
    for i in xrange(limit):
        if is_reversible(i):
            reversibles.append(i)
    print reversibles
    return len(set(reversibles))
