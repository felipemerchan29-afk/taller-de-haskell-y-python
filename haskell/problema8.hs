precioArcade :: Int -> Int
precioArcade edad
    | edad < 5  = 0
    | edad <=12 = 10
    | edad <=17 = 15
    | otherwise = 20

