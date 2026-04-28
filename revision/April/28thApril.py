class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = {}

        for i, v in enumerate(nums) : 
            res = target - v

            if res in mp : 
                return [mp[res], i]
            
            mp[v] = i

        return [-1,-1]

