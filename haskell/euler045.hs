triangle = [n*(n+1) `div` 2 | n <- [1..]]
pentagonal = [n*(3*n-1) `div` 2 | n <- [1..]]
hexagonal = [n*(2*n-1) | n <- [1..]]

intersect' (x:xs) (y:ys) (z:zs)
  | (x == y) && (y == z) = x : (intersect' xs ys zs)
  | smallest == x = intersect' xs (y:ys) (z:zs)
  | smallest == y = intersect' (x:xs) ys (z:zs)
  | smallest == z = intersect' (x:xs) (y:ys) zs
  where smallest = minimum [x,y,z]
        
euler45 = take 3 $ intersect' triangle pentagonal hexagonal