class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        

        self.total = 0 
        self.mini = None
        MOD = (10 ** 9)+7
        n = len(arr)

        for i in range(n) : 
            self.mini = arr[i]

            for j in range(i,n) :
                self.mini = min(arr[j], self.mini)
                self.total = ( self.mini + self.total ) % MOD

        return self.total


# --------------------- sum of subarray minimum ----------------

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        nse = self.nextSmallerEle(arr)
        pse = self.prevSmaller(arr)
        MOD = (10**9)+7
        
        print(nse)
        print(pse)

        total = 0
        
        for i, v in enumerate(arr) : 
            
            pr = pse[i]
            ne = nse[i]

            prevElemCnt = i - pr
            nextElemCnt = ne - i

            total = (total + (prevElemCnt * nextElemCnt *  arr[i]) ) %  MOD
        
        return total

    def prevSmaller(self, arr):
		
        n = len(arr)
        st = []
        pse = [-1]*n

        for i in range(n) : 
            v = arr[i]
            
            while st and st[-1][0] >= v : 
                st.pop()
                
            if st : 
                pse[i] = st[-1][1]
                
            st.append((v, i))

        return pse

    def nextSmallerEle(self, arr):
		# code here
		
        n = len(arr)
        st = []
        nse = [n]*n

        for i in range(n-1,-1,-1) : 
            
            v = arr[i]
            
            while st and st[-1][0] > v : 
                st.pop()
                
            if st : 
                nse[i] = st[-1][1]
                
            st.append((v, i))
            
            
        return nse    



