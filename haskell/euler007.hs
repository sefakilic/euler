-- from http://stackoverflow.com/questions/3596502/lazy-list-of-prime-numbers
primes = sieve [2..] where
  sieve (p:xs) = p : sieve [x | x <- xs, x `mod` p > 0]
  
euler007 = primes !! 10000