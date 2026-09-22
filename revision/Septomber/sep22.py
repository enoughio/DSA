class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        p = 1
        lelem = nums[i]
        n = len(nums)

        while ( i  < n ) : 
            if nums[i] != lelem  : 
                lelem = nums[i]
                nums[p] = nums[i] 
                p += 1

            i += 1 

        return p 