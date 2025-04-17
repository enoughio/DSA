class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = self.normalize(s)
        return self.rec(0, len(s)-1, s)

    
    def normalize(self, s):
        t = ""
        for i in s:
            if i.isalnum():
                t += i.lower()
        return t


    def rec(self, st, ed, s):
        
        if(st >= ed):
            return True
        
        if(s[st] != s[ed]):
            return False
        else :
           return self.rec(st+1, ed-1, s)
        

## optimized version

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.checkPal(s,0, len(s)-1)
        
    def checkPal(self, s, st, ed):

        if(st >= ed):
            return True
        
        if( True != s[st].isalnum() ):
            return self.checkPal(s, st+1, ed)

        if ( True !=  s[ed].isalnum() ):
            return self.checkPal(s, st, ed-1 )
        
        if(s[st].lower() != s[ed].lower()):
            return False
        else: 
            return self.checkPal(s, st+1, ed-1)


# Example usage:

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal"))  # Output: True

        