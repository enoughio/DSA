












# ------------------------------------------------------------------------------

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        x = k
        mx = 0
        i, j = 0, 0
        st = 0

        while  j < n : 

            if nums[j] ==  0 : 
                x-= 1
            
            if x < 0 : 
                while( nums[i] != 0) :
                    i+=1 
                i+=1
                x +=1

            mx = max(mx, j-i+1)
            j+=1

        return mx




