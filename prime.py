class Solution:
    def isPrime(self, n):
        # code here
        
        if n == 1 : 
            return False
        
        m = math.ceil(math.sqrt(n)) 
        for i in range(2, m+1) :
            
            if n%i == 0 : 
                return False
                
        return True