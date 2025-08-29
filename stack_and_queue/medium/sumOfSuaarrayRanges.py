class Solution:
    def sumSubarrayMins(self, a: List[int]) -> int:
        
        n = len(a)
        ans = 0

        mod = ( 10 ** 9 ) + 7
        pse = [-1] * n
        nse = [n]* n

        st = []
        for i in range(n) :    # Previous smaller or equal Element

            while st and st[-1][0] > a[i] :   # only poping the elem that 
                st.pop()                      # that are greater then arr[i]
            
            if st : 
                pse[i] = st[-1][1]             #store equal or smaller elem 

            st.append((a[i], i))



        st2 = []
        for i in range(n-1, -1, -1) :    # next smaller Element
    
            while st2 and st2[-1][0] >= a[i] :
                st2.pop()
            
            if st2: 
                nse[i] = st2[-1][1]   # only store smaller element

            st2.append((a[i], i))


        for i in range(n) : 

            p = i - pse[i]
            n = nse[i] - i

            ans = (ans + ((p*n)%mod)*a[i])%mod
            
        
        return ans


    
    def sumOfSubArrayMax(self, a) -> int: 
        ans = 0
        n = len(a)
        mod = 10**9 + 7

        nge = [n] * n   # next greater index
        pge = [-1] * n  # previous greater index

        st1 = []
        for i in range(n-1, -1, -1):
            while st1 and st1[-1][0] <= a[i]:
                st1.pop()
            if st1:
                nge[i] = st1[-1][1]
            st1.append((a[i], i))

        st2 = []
        for i in range(n):
            while st2 and st2[-1][0] < a[i]:
                st2.pop()
            if st2:
                pge[i] = st2[-1][1]
            st2.append((a[i], i))

        for idx, val in enumerate(a):
            ng = nge[idx] - idx
            pg = idx - pge[idx]
            ans = (ans + (ng * pg * val) % mod) % mod 

        return ans



    def subArrayRanges(self, nums: List[int]) -> int:
        mini =  self.sumSubarrayMins(nums)
        maxi =  self.sumOfSubArrayMax(nums)

        return maxi - mini