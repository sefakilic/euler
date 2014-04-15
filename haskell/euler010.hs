squareRoot = floor . sqrt . (fromIntegral :: Integer -> Double)

isPrime n = and [n `mod` x > 0 | x <- 2:[3,5..(squareRoot n)]]

euler010 = sum (2:[x | x <- [3,5..2000000], isPrime x])

