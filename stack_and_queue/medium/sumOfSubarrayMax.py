

class Solution : 
    def sumOfSubArrayMax(self, a ) -> int : 
        
        ans = 0
        n =  len(a)
        mod = ( 10 ** 9 ) + 7

        st1 = []
        nge = [n]*n
        # next greater element  
        for i in range(n-1, -1, -1)  :

            while st1 and st1[-1][0] <= a[i] : 
                st1.pop()
            
            if st1 : 
                nge[i] = st1[-1][1]
                
            st1.append((a[i], i))

        
        st2 = []
        pge = [-1]*n
        # Previous Greater Element
        for i in range(n) : 

            while st2 and st2[-1][0] < a[i] : 
                st2.pop()
            
            if st2 : 
                pge[i] = st2[-1][1]
                
            st2.append((a[i], i))




        for idx, i in enumerate(a) : 

            ng =  nge[idx] - idx
            pg =  idx - pge[idx]

            ans = ans + (((ng * pg)%mod)* i) % mod 

        return ans
    


arr = [3,1,2,5]
s = Solution()
print(s.sumOfSubArrayMax(arr))
