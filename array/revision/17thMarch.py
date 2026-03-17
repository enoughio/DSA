class Solution:
    def beautySum(self, s: str) -> int:

        n = len(s)
        ans = 0
        data = { }

        for i in range(n) : 

            for j in range(i,n) : 
                ans += self.cal( s[i:j+1])
            
        return ans
        
        
    def cal(self, s) : 
        freq = { }

        for i in s :
            freq[i] = freq.get(i, 0) + 1
        
        # print(freq)

        mf = 0
        lf = 600

        for k, v in freq.items() : 
            mf = max(v, mf)
            lf = min(lf, v)

        return mf - lf  
    



    # -------------------------------not understand  it well-----------------------------


class xSolution:
    def beautySum(self, s: str) -> int:

        n = len(s)
        ans = 0

        for i in range(n) : 
            freq = { }

            for j in range(i,n) : 
                
                freq[s[j]] = freq.get(s[j], 0) + 1
        

                lf = 6000
                mf = 0
                for k, v in freq.items() : 
                    mf = max(v, mf)
                    lf = min(lf, v)

                ans += mf - lf

        return ans

