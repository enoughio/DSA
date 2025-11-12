class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)

        nums.reverse()
        k = k%n
        
        st = 0
        ed = k-1
        while(ed > st ) :
            nums[st], nums[ed] = nums[ed], nums[st]
            st+=1
            ed-=1
         
        st = k
        ed = n-1
        x = k+n-1

        while(ed > st): 
            nums[st], nums[ed] = nums[ed], nums[st]
            st+=1
            ed-=1
        

