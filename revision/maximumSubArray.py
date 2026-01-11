class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sum, maxSum = 0, float('-inf')

        for num in nums : 
            sum  = sum + num
            maxSum = max(maxSum, sum)

            if sum < 0  : 
                sum = 0

        return maxSum