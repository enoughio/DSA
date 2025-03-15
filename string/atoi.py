class Solution:
    def myAtoi(self, s: str) -> int:
        
        flag = False
        st = 0
        ed = 0
        ans = 0
        n = len(s)

        if(n == 0):
            return ans

        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648

        while( st < n and s[st] == ' ' ):
            st+=1

        if( st <  n and s[st] == '-' ):
            flag = True
            st+=1
        elif( st < n and  s[st] == '+' ):
            st+=1

        while( st < n and s[st] == '0' ):
            st+=1
        
        ed = st
        while( ed < n and s[ed] >= '0' and s[ed] <= '9' ):
            ed+=1
        
        ed-=1
        p = 1
        while( ed < n and ed >= st):

            if(ans + (int(s[ed]) * p)) > INT_MAX :
                if(flag):
                    return INT_MIN
                return INT_MAX

            ans += int(s[ed]) * p
            p = p*10
            ed-=1
        
        if(flag):
            return ans*-1
        return ans
