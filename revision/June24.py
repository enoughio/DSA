class Solution:
    def check(self, nums: List[int]) -> bool:
        arr = []
        n  = len(nums)
        
        br = 0

        for i in range(n) : 
            if i > 0 and nums[i-1] > nums[i] : 
                br = i
                break
        
        for i in range(br, n) : 
            arr.append(nums[i]) 
        
        for i in range(0, br) : 
            arr.append(nums[i]) 
        

        for i in range(len(arr)) :
            if i > 0 and arr[i-1] > arr[i] :
                return False

        return True 
