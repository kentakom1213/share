-- 平方剰余記号を計算

import Data.Numbers.Primes (primeFactors)
import Data.Foldable (Foldable(product))

main :: IO ()
main = do
  m <- readLn
  n <- readLn
  print $ qmod m n

-- 平方剰余記号を計算する関数
qmod :: Int -> Int -> Int
qmod m n
  | gcd m n /= 1 = 0
  | m == 1       = 1
  | even m       = (-1) ^ div (n^2 - 1) 8 * qmod (m `div` 2) n
  | otherwise    = (^) (-1) $ ((m-1) `mod` 2) * (-1) ^ ((n-1) `mod` 2) * qmod (n `mod` m) m
