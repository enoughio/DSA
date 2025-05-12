class Solution:
    def subsets(self, nums):
        
        ans  = []
        arr = []
        i = 0

        self.rec(ans, arr, i, nums)
        print(len(ans))
        return ans

    def rec(self, ans, arr,i , nums):

        if i >= len(nums):
            ans.append(arr[:])
            return
        
        self.rec( ans, arr, i+1, nums)
        arr.append(nums[i])
        self.rec( ans, arr, i+1, nums)
        arr.pop()



s = Solution()
nums = [1,2,3]
print(s.subsets(nums))
