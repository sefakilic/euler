fibs = 1 : 1 : zipWith (+) fibs (tail fibs)

numDigits n = length (show n)

euler25 = head [x | x <- zip fibs [1..], (numDigits $ fst x) == 1000]
