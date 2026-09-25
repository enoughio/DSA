class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:

        mp = {}

        for i in range(len(nums)) : 
            rem = k - nums[i]
            if rem in mp : 
                return [ i, mp[rem] ]
             
            mp[nums[i]] = i

        return [-1, -1]

# ---------------

class Solution:
    def twoSum(self, nums: list[int], k: int) -> list[int]:
        mp = {}

        for i in range( len(nums)) : 
            rem = k - nums[i]
            if rem in mp : 
                return [ mp[rem]+1, i+1 ]
             
            mp[nums[i]] = i

        return [-1, -1]