modpow a b m 
  | b == 0    = 1 `mod` m
  | b == 1    = a `mod` m
  | odd b     = (x * x * a) `mod` m
  | otherwise = (x * x) `mod` m
  where x = modpow a (b `quot` 2) m
        
test = sum [x^x | x <- [1..10]]
euler48 = (sum [modpow x x (10^10) | x <- [1..1000]]) `mod` (10^10)
