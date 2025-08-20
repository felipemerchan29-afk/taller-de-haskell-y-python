grupo :: String -> String -> Char
grupo nombre genero =
    if (genero == "F" && nombre < "m") || (genero == "M" && nombre >= "n")
        then 'A'
        else 'B'
