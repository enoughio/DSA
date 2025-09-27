
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        nge = [-1] * n
        pge = [-1] * n    


        st = []
        #Previous greater elment
        for i in range(n) : 
            if st and st[-1] > height[i] : 
                pge[i] = st[-1]
            else : 
                if st : st.pop()
                pge[i] = -1
                st.append(height[i])


        st2 = []
        #next greater elment
        for i in range(n-1, -1, -1) : 
            if st2 and st2[-1] > height[i] : 
                nge[i] = st2[-1]
            else : 
                if st2 : st2.pop()
                nge[i] = -1
                st2.append(height[i])

        ans = 0 
        print(nge)

        for i in range(n) : 
            if nge[i] > 0 and pge[i] > 0 : 
                cap = min(nge[i], pge[i])
                ans += cap - height[i]
        
        return ans
