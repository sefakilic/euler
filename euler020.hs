import Data.Char
sumOfDigits n = sum [digitToInt c | c <- show n]

fac 0 = 1
fac n = n * fac (n-1)

euler20 = sumOfDigits $ fac 100