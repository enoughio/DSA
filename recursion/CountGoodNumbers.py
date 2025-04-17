class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = pow(10,9) + 7
        
        if n == 1 :
            return 5

        if n%2 == 0:
            even = n//2
            odd = n//2
        else : 
            even = 1 + (n//2)
            odd = n//2
        
        digit = self.rec(5, even, MOD) * self.rec(4, odd, MOD)

        return digit

    def rec(self, x, n, MOD):
        if(n == 0):
            return 1
        if(n == 1):
            return x
        
        if(n%2 == 0):
            return (self.rec((x * x)% MOD, n//2,  MOD))%MOD
            # return res * res
        else : 
            return  (self.rec((x * x)% MOD , n//2,  MOD) * x)% MOD
            # return res * res * x
        

#hero-----------------
        if n == 1:
            return 5

        even = (n + 1) // 2  # positions: 0, 2, 4... can hold 5 values
        odd = n // 2         # positions: 1, 3, 5... can hold 4 values

        digit = (self.rec(5, even, MOD) * self.rec(4, odd, MOD)) % MOD

        return digit
#---------------------------


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = pow(10,9) + 7
        
        if n == 1 :
            return 5

        if n%2 == 0:
            even = n//2
            odd = n//2
        else : 
            even = 1 + (n//2)
            odd = n//2
        
        digit = (self.rec(5, even, MOD) * self.rec(4, odd, MOD)) % MOD    #changed this one

        return digit

    def rec(self, x, n, MOD):
        if(n == 0):
            return 1
        if(n == 1):
            return x
        
        if(n%2 == 0):
            return (self.rec((x * x)% MOD, n//2,  MOD))%MOD
            # return res * res
        else : 
            return  (self.rec((x * x)% MOD , n//2,  MOD) * x)% MOD
            # return res * res * x
        



class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = pow(10,9) + 7
        
        if n == 1:
            return 5

        even = (n + 1) // 2  # positions: 0, 2, 4... can hold 5 values
        odd = n // 2         # positions: 1, 3, 5... can hold 4 values

        digit = (self.rec(5, even, MOD) * self.rec(4, odd, MOD)) % MOD

        return digit

    def rec(self, x, n, MOD):
        if(n == 0):
            return 1
        if(n == 1):
            return x
        
        if(n%2 == 0):
            return (self.rec((x * x)% MOD, n//2,  MOD))%MOD
            # return res * res
        else : 
            return  (self.rec((x * x)% MOD , n//2,  MOD) * x)% MOD
            # return res * res * x
        