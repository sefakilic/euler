-- http://projecteuler.net/problem=3
factors 1 = []
factors n = fac : (factors (n `quot` fac)) where
  fac = head [x | x <- [2..], n `mod` x == 0]

euler003 = maximum $ factors 600851475143

  
