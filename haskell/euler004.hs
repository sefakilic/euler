-- http://projecteuler.net/problem=4
palindrome = maximum [x | a <- [10..99], b <- [10..99], let x = a*b,
                      show x == reverse (show x)]
             
palindrome' = maximum [x | a <- [100..999], b <- [100..999], let x = a*b,
                       show x == reverse (show x)]
              
euler004 = palindrome'