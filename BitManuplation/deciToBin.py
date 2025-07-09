ans = ''

def decToBi(n) :
    global ans
    if n == 1 :
        ans = ans + '1'
        return

    
    r = n%2
    n = n//2

    decToBi(n)
    ans = f"{r}" + ans


decToBi(25)
print(ans)