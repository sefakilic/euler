word 1 = "one"
word 2 = "two"
word 3 = "three"
word 4 = "four"
word 5 = "five"
word 6 = "six"
word 7 = "seven"
word 8 = "eight"
word 9 = "nine"
word 10 = "ten"
word 11 = "eleven"
word 12 = "twelve"
word 13 = "thirteen"
word 14 = "fourteen"
word 15 = "fifteen"
word 16 = "sixteen"
word 17 = "seventeen"
word 18 = "eighteen"
word 19 = "nineteen"
word 20 = "twenty"
word 30 = "thirty"
word 40 = "forty"
word 50 = "fifty"
word 60 = "sixty"
word 70 = "seventy"
word 80 = "eighty"
word 90 = "ninety"
word 1000 = "onethousand"


word n
  | n `mod` 100 == 0 = word (n `div` 100) ++ "hundred"
  | n > 100 = word (n `div` 100) ++ "hundred" ++ "and" ++ word (n `rem` 100)
  | n >= 20 = word ((n `div` 10) * 10) ++ word (n `rem` 10)

euler17 = sum $ map length [word n | n <- [1..1000]]
