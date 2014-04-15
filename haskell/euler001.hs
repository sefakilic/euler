-- http://projecteuler.net/problem=1
euler001 = sum [x | x <- [1..999], x `rem` 3 == 0 || x `rem` 5 == 0]