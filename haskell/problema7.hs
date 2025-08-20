evaluacion :: Float -> (Int, Int)
evaluacion p
    | p < 3     = (1,100)
    | p <= 6    = (2,500)
    | otherwise = (3,1000)
