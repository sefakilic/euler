import Data.Char
sumOfDigits n = sum [digitToInt c | c <- show n]
euler16 = sumOfDigits (floor (2**1000))
