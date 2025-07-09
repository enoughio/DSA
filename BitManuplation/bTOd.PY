def BtoD(st) :
    st  =  str(st) 
    d = 0
    i = len(st)-1
    p = 1

    while i >= 0 :
        d += int(st[i]) * p
        p = p*2
        i-= 1
    
    return d

print(BtoD('101'))