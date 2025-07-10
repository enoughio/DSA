

def countNum(n) : 



    cnt  =  0 
    while( n > 1 ) : 
        cnt += n & 1
        n = n >> 1

    if n == 1 : cnt = cnt + 1
    return cnt 

print(countNum(1))