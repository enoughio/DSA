class Solution:
    def check(self, nums: List[int]) -> bool:
        
        i,j = 0, 0
        n = len(nums)

        while(i < n and  j < 2*n): 

            idx = j%n
            if nums[idx - 1] > nums[idx] : 
                i = j

            if ( j-i+1 == n ): 
                return True
            
            j+=1
        

        return False