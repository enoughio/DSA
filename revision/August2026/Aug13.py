class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        el = None
        cnt = 0

        for i in range( len(nums) ) : 
            
            if cnt == 0 : 
                cnt = 1
                el = nums[i]
                continue
            
            if el == nums[i] : 
                cnt += 1
            else :  
                cnt -= 1


        return el