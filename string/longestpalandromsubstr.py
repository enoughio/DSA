class Solution:
    def longestPalindrome(self, s: str) -> str:
  
        i = 0 
        n = len(s)

        res = s[0]
        reslen = 0
            
        while i < n:
            st = i
            ed = i+1
            while  st >= 0 and ed < n and s[st] == s[ed] : 
                if(ed - st +1) > reslen:
                    res = s[st:ed+1]
                    reslen = ed - st + 1
                st -= 1
                ed +=1

            st = i
            ed = i
            while st >= 0 and ed < n and s[st] == s[ed] : 
                if(ed -st +1) > reslen:
                    res = s[st:ed+1]
                    reslen = ed - st + 1
                st -= 1
                ed +=1

            i+=1        



        
        return res 



