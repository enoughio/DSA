class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        #  find the first zero valued index
        while i < len(nums)  :
            if nums[i] == 0 :
                break
            i = i + 1
        
        if i ==  len( nums ) :   # return the same array if no  zero is found 
            return nums

            #  '  i ' pointer  act as the indecator to where to place the next non zero integer 
        for j in range(i, len(nums) ) :             
            
            if i == j :
                continue

            if nums[j] != 0 :            # if we have a zero value before  any non zero integer the swap the value, 
                                            # so that we have zero toward last
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp         
                i = i + 1                   # move the i poibnter to next index as there 
                j = j + 1
