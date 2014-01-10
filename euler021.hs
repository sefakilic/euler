sumProperDiv n = sum [x | x <- [1..(n-1)], n `mod` x == 0]

-- two numbers a and b are amicable numbers if d(a) = b and d(b) = a

euler21 = sum [x | x <- [1..10000], let d = sumProperDiv x, d /= x && d <= 10000 && sumProperDiv d == x]