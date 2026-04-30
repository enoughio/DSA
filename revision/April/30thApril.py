class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        # pt = 0
        # pge = [-1]*n
        # for i, v in enumerate(height) : 

        #     if pt > v : 
        #         pge[i] = pt
        #     else : 
        #         pt = v
        #         pge[i] = -1
        
        gt = 0
        nge = [-1]*n
        for i in range(n-1, -1, -1) : 

            if gt > height[i] : 
                nge[i] = gt
            else : 
                gt = height[i]
                nge[i] = -1
        
        print(nge)
        # print(pge)
        

        pt = 0
        ans = 0
        i = 0
        for e in height : 

            if pt > e and nge[i] != -1 : 
                ans += min(nge[i], pt) - e
            elif pt <= e : 
                pt = e
            
            i+=1

        return ans
            