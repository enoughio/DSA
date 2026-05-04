class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxi = 0
        nse = self.calNse(heights)
        pse = self.calPse(heights)

        for i in range(len(heights)) : 
            res = ((nse[i] - i) + (i - pse[i]) -1 )  * heights[i]


            maxi = max(maxi, res)

        return maxi

    def calNse(self, arr) : 

        st  = []
        n = len(arr)
        nse = [n] * n 

        for i in range(n-1, -1, -1) : 

            while st and arr[st[-1]] >= arr[i] : 
                st.pop()

            if st : 
                nse[i] = st[-1]

            st.append( i ) 

        return nse

    def calPse(self, arr) : 

        st  = []
        n = len(arr)
        pse = [-1] * n 

        for i in range(n) : 

            while st and arr[st[-1]] >= arr[i] : 
                st.pop()

            if st : 
                pse[i] = st[-1]

            st.append(i) 

        return pse
