class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [-1]*n

        for idx, k in enumerate(nums) : 

            i = 0
            id = idx+1

            while i < n : 

                if nums[id%n] > k : 
                    ans[idx] = nums[id%n]
                    break
                i+=1
                id += 1
            
        return ans
    
    