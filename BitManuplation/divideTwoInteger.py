class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAXI = ( 1 << 31 )- 1
        MINI = -(1 << 31 )

        q = 0
        flag = True 
        if(dividend < 0 and divisor > 0 ) : flag = False
        if(dividend > 0 and divisor < 0 ) : flag = False

        n = abs(dividend)
        d = abs(divisor)

        while n >= d : 
            i = 0 
            while (n - (d * 1<< i + 1)) >= 0 : 
                i+= 1

            q += 1 << i
            n -= d * 1 << i
        
        if not flag :  q = q * -1

        if ( q > MAXI ) : return MAXI
        return q