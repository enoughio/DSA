class Solution:
    def myPow(self, x: float, n: int) -> float:

        if( n > 0):
            res = self.rec( x, abs(n))
        else : 
            res = self.rec( x, abs(n))
            res = 1/res
        return res

    def rec( self, x, n): 
        if( n == 0 ):
            return 1
        if ( n == 1 ):
            return x
    
        if( n%2 == 0):
            res = self.rec( x, n//2)
            return res * res 
        else :
            res = self.rec( x, n//2)
            return  res * res * x

        