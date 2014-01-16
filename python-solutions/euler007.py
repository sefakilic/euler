primes = [2, 3, 5, 7, 11, 13] #first few primes
n = primes[-1] # last prime

while len(primes) < 10001:
    n = n+2
    for p in (pr for pr in primes if pr**2 <= n):
        if n%p==0:
            break
    else:
        primes.append(n)
        
print primes[-1]
