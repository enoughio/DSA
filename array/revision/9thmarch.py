class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = True
        j=1
        i = 0
        n = len(nums)

        while i < n and  j < n :

            if flag : 
                if nums[i] >= nums[j] :
                    while j < n-1 and nums[i] >= nums[j] :
                        j +=1 
                    if nums[i] < nums[j] :
                        nums[i+1], nums[j] = nums[j], nums[i+1]
                    else : 
                        nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j = i + 1

            else :
                if nums[i] <=  nums[j] : 
                    while  j < n-1 and nums[i] <= nums[j] :
                        j += 1
                    if nums[i] > nums[j] :
                        nums[i+1], nums[j] = nums[j], nums[i+1]
                    else : 
                        nums[i], nums[j] = nums[j], nums[i]
                i += 1 
                j = i + 1
            # print(flag)
            flag = not flag 

            
