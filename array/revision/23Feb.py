class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 
        j = 0

        n = len(nums)

        while j < n : 
            
            if j < i : 
                j+=1
                continue 
            
            if nums[i] != 0 : 
                i+=1 
            
            if nums[j] == 0 :
                j+=1
            
            if j < n and i < n and j > i and nums[i] == 0 and nums[j] != 0 : 
                nums[i], nums[j] = nums[j], nums[i]
            


# ---------------------------
    def singleNumber(self, nums: List[int]) -> int:
        
        xor = nums[0]

        for i in range(1,len(nums)) : 
            xor = xor ^ nums[i]
        
        return xor