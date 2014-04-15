-- http://projecteuler.net/problem=6

sumSquares xs = sum [x*x | x <- xs]
squareSum xs = (sum xs)**2
firstHundredNums = [1..100]
euler006 = squareSum firstHundredNums - sumSquares firstHundredNums
