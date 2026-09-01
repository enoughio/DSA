class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        cnt = 0
        prefixSum = 0
        mpp = {}
        mpp[0] = 1

        for i in nums : 
            prefixSum += i
            remove = prefixSum - k

            cnt += mpp.get(remove, 0)
            mpp[prefixSum] = mpp.get(prefixSum, 0) + 1
        
        return cnt
        
