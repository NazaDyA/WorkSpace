def laxStr(x:str,y:str):
    x = x.lower().strip().replace(" ","")
    y = y.lower().strip().replace(" ","")
    
    mx = max(len(x),len(y))
    
    return float(len(set(x).difference(set(y)))/mx)
