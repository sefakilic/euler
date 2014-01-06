modpow a b m 
  | b == 0    = 1 `mod` m
  | b == 1    = a `mod` m
  | odd b     = (x * x * a) `mod` m
  | otherwise = (x * x) `mod` m
  where x = modpow a (b `quot` 2) m
        
euler97 = (28433 * (modpow 2 7830457 (10^10)) + 1) `mod` (10^10)