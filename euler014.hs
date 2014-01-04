collatzSeqLen 1 = 1
collatzSeqLen n
  | odd n = 1 + collatzSeqLen (3*n + 1)
  | otherwise = 1 + collatzSeqLen (n `div` 2)
                
euler14 = maximum [(collatzSeqLen x, x) | x <- [1..1000000]]