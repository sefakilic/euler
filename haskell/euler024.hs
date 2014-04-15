import Data.List

test = permutations [0,1,2]

euler24 = (sort $ permutations "0123456789") !! 999999
