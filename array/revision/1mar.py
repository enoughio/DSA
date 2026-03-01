class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        cnt = 0
        mapp = {}
        mapp[0] = 1
        prefixSum = 0

        for i in nums : 

            prefixSum += i
            prefix = prefixSum - k

            cnt += mapp.get(prefix, 0)
            mapp[prefixSum] = 1 + mapp.get(prefixSum, 0)

        return cnt 