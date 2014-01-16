memorize = {}

def how_many(n, max_num):
    """Return how many ways can n be written as sum of numbers which are <max_num>
    at most.
    """
    global memorize
    if (n, max_num) in memorize:
        return memorize[(n, max_num)]
    
    if max_num < 1:
        return 0
    if n <= 1:
        return 1
    if n < max_num:
        memorize[(n, max_num)] = how_many(n, max_num-1)
        return memorize[(n, max_num)]

    memorize[(n, max_num)] = how_many(n - max_num, max_num) + how_many(n, max_num-1)
    return memorize[(n, max_num)]


        
    
    
