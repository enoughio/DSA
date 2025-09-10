class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        pk = 0

        if n == 1 : 
            return 0
        elif n == 2 :
            if nums[0] > nums[1] : 
                return 0
            else : 
                return 1
        elif n == 3 : 
            if  nums[0] < nums[1] and nums[1] > nums[2]  :
                return 1 
            elif  nums[0] > nums[1] : 
                return 0
            elif nums[2] > nums[1] : 
                return 2


        if nums[0] > nums[1] : 
            return 0

        for i in range(1, n-1) : 
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]  : 
                return i

        if nums[n-2] < nums[n-1] :
            return n-1
        
        