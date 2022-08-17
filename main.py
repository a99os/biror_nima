def Tub(son):
    if son<2:
        return True
    for i in range(2,son//2):
        if not son%i:
            return False
    return True