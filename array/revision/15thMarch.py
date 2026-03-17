class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        i = 0
        n = len(s)
        sign = True
        INT_MIN = -(2 ** 31)
        INT_MAX = (2 ** 31)-1

        while i < n and s[i] ==" " :
            i+=1

        if i < n and s[i] == "-" :
            sign = False 
            i+=1
        elif i < n and s[i] == "+" :
            i+=1 

        print(i)
        MOD = (2 ** 31) -1
        while i < n and s[i] >= "0" and s[i] <= "9" :
            res = ord(s[i]) - ord("0")
            ans = ans *10
          
            ans += res
            i+=1

        ans = ans if sign else ans*-1
        ans =  max(INT_MIN, min(INT_MAX, ans))
        return ans
    





    # -------------------------longest palandrom sub---------------

    class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        maxi = 0

        maxl = 0
        maxr = n

        pr = 0
        i = 0

        while i < n :
            l = i
            r = i

            while i +1 < n and s[i] == s[i+1 ] :
                r = i + 1
                i = i + 1

            i = i +1 
        
            while( l >=0 and r < n ) : 
                if s[r] == s[l] :
                    if (r-l)+1 >= maxi : 
                        maxl = l 
                        maxr = r
                        maxi = (r-l)+1
                    r+=1
                    l-=1
                
                else : 
                    break


        return s[maxl : maxr+1]
    
    