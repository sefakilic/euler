import Data.Set

triangleNums = tr [1..] where
  tr (x:x':xs) = x : tr ((x+x') : xs)
  
factors n = [x | x <- [1..n], n `mod` x == 0]

squareRoot = floor . sqrt . (fromIntegral :: Integer -> Double)

tupleListToList xs = [fst x | x <- xs] ++ [snd x | x <- xs]

makeUnique lst = toList $ fromList lst

factors' n = makeUnique $ tupleListToList $ [(x,y) | let sq = squareRoot n,
                                             x <- [1..sq], n `mod` x == 0,
                                             let y = n `div` x]

  
euler12 = head [x | x <- triangleNums, (length $ factors' x) > 500]

