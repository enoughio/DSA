
from typing import List


class Solution:
    def sumSubarrayMins(self, a: List[int]) -> int:
        
        n = len(a)
        ans = 0

        mod = ( 10 ** 9 ) + 7
        pse = [-1] * n
        nse = [n]* n

        st = []
        for i in range(n) :    # Previous smaller or equal Element
            if st and st[-1][0] < a[i] : 
                pse[i] = st[-1][1]
            else :
                while st and st[-1][0] > a[i] :   # only poping the elem that 
                    st.pop()                      # that are greater then arr[i]
                if st : 
                    pse[i] = st[-1][1]             #store equal or smaller elem 

            st.append((a[i], i))

        st2 = []
        for i in range(n-1, -1, -1) :    # next smaller Element
            if st2 and st2[-1][0] < a[i] : 
                nse[i] = st2[-1][1]
            else :
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




# =======================
# for greater element
    def sumOfSubArrayMax(self, a: List[int]) -> int:

        st1 = []
        st2 = []

        ans = 0
        