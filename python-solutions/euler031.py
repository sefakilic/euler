coins = [1, 2, 5, 10, 20, 50, 100, 200]

def ways(n, i):
    """Return how many ways to make up n, not using coins larger than coins[i]"""
    #print n, coins[i]
    if n == 0:
        return 1
    if i < 0:
        return 0
    
    if coins[i] > n:
        return ways(n, i-1)
    else:
        return ways(n-coins[i], i) +  ways(n, i-1)
    

print ways(200, len(coins)-1)
    
    
