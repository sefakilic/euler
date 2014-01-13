import System.IO

maxPath curMax [] = maximum curMax
maxPath
  
main = do
  x <- readFile "euler018.txt"
  let triangle = map (\line -> map (\wd -> read wd :: Int) (words line)) (lines x)
  print $ maxPath [] triangle