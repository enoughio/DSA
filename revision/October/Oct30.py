class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        n = len(s)
        m = len(t)

        if m != n : return False 

        freq = {}
        fqSum = 0

        for i in s  : 
            freq[i] = freq.get(i, 0) + 1
            fqSum +=1
        for i in t : 

            if i in freq and freq[i] != 0 : 
                freq[i]  = freq.get(i, 0) - 1
                fqSum -= 1  
            else : 
                return False    
        
        if fqSum == 0: 
            return True
        else : 
            return False