def is_palindrome(n):
    return str(n) == str(n)[::-1]

def euler_125(n=10000):
    interestings = []
    squares = [x**2 for x in xrange(1, n)]
    for i in xrange(0, len(squares)):
        for j in xrange(i+2, len(squares)):
            s = sum(squares[i:j])
            if s >= n**2:
                break
            if  is_palindrome(s):
                interestings.append(s)

    return list(set(interestings))
