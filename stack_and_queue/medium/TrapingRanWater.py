class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        total = 0

        # # prefixMax
        # prefixMax = []
        # prefixMax.append(height[0])
        # for j in range(1,n) :
        #     prefixMax.append(max(prefixMax[-1], height[j]))

        # sufixMax
        sufixMax = [0]*n
        sufixMax[-1] = height[-1]
        for j in range(n-2,-1,-1) :
            sufixMax[j] =  max( sufixMax[j+1], height[j] )

        l_max = height[0]
        for i in range(n) : 
            cur = height[i]

            if l_max > cur and sufixMax[i] > cur : 
                total = total + min(l_max, sufixMax[i]) - cur
            
            l_max = max(l_max, height[i])

        return total
    

    