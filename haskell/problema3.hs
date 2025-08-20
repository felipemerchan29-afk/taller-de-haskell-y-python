division :: Float -> Float -> Maybe Float
division _ 0 = Nothing
division a b = Just (a / b)
