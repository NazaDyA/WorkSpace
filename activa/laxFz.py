from fuzzywuzzy import fuzz

def laxFz(x:str, y:str):

    x = x.lower().strip()
    y = y.lower().strip()

    p = fuzz.ratio(x, y)

    return p

