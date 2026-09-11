class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        n= len(s)

        def compare(s, re) : 
            n = len(s)
            i = 0
            j = n-1

            while i < j and i < n and j > -1   :
                
                if i == re : 
                    i+=1
                if s[i] != s[j]  : 
                    return False
                i+=1
                j-=1
            
            return True

        def compare2(s, re) : 
            n = len(s)
            i = 0
            j = n-1

            while i < j and i < n and j > -1   :
                
                if j == re : 
                    j-=1
                if   i < n and j > -1 and s[i] != s[j] : 
                    return False
                i+=1
                j-=1
            
            return True
        
        n = len(s)
        i = 0
        j = n-1
        flag = True

        while i < j and i < n and j > -1   :
            
            if s[i] != s[j] and flag == True : 
                
                res1 = compare(s, i)
                res2 = compare2(s, j)
                if res1 == True : 
                    return True
                elif res2 == True : 
                    return True
                else : return False

                flag = False

            i+=1
            j-=1
        
        return True

