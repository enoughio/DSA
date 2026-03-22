class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
     
        MOD = (10 ** 9) + 7
        
        if n%2 == 0 : 
            even = n//2 
            odd = n//2
            ev = self.myPow(5, even, MOD) 
            od = self.myPow(4, odd, MOD) 
            return (ev * od)%MOD
        else : 
            even = (n//2) + 1 
            odd = (n//2) 
            ev = self.myPow(5, even, MOD) 
            od = self.myPow(4, odd, MOD) 
            return (ev * od)%MOD


    def myPow(self, x: float, n: int, MOD) -> float:

        sign = True    
        if n < 0 : 
            sign = False
            n = abs(n)

        if n%2== 0 :
            res = self.power(x,n//2, MOD)
            return (res * res)% MOD if sign  else 1/(res * res)%MOD
        else :
            res = self.power(x,n//2, MOD)
            return (res * res * x)%MOD if sign  else 1/(res * res * x)%MOD
    
    def power(self, x, n, MOD) : 

        if n == 0 : 
            return 1
        if n == 1 : 
            return x
        
        if n%2 == 0 : 
            res = self.power(x, n//2, MOD)
            return (res * res)%MOD
        else : 
            res = self.power(x, n//2, MOD)
            return (res * res * x)%MOD
        




# ------------------ custom Power function -----------------
class Solution:
    def myPow(self, x: float, n: int) -> float:

        sign = True    
        if n < 0 : 
            sign = False
            n = abs(n)

        if n%2== 0 :
            res = self.power(x,n//2)
            return res * res if sign  else 1/(res * res)
        else :
            res = self.power(x,n//2)
            return res * res * x if sign  else 1/(res * res * x)
    
    def power(self, x, n) : 

        if n == 0 : 
            return 1
        if n == 1 : 
            return x
        
        if n%2 == 0 : 
            res = self.power(x, n//2)
            return res * res
        else : 
            res = self.power(x, n//2)
            return res * res * x
