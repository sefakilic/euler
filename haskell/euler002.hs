-- http://projecteuler.net/problem=2
fib xs
  | lastFib > 4000000 = xs
  | otherwise = fib (lastFib:xs)
  where lastFib = head xs + head (tail xs)
        
euler002 = sum [x | x <- fib [2,1], x `rem` 2 == 0]


