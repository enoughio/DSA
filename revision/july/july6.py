class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=  len(t) : 
            return False 
        
        ms = {}
        mt = {}

        for i in s :
            ms[i] = ms.get(i, 0) + 1
        
        for i in t :
            mt[i] = mt.get(i, 0) + 1

        for i in ms.keys() : 
            if i not in mt :
                return False 
            elif mt[i] != ms[i] : 
                return False 
            
        return True 
    

    # -------------------------


    
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for i in nums : 
            if i in seen : 
                return True 
            seen[i] = i 

        return False
    

    # --------------------------


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i in range(len(nums)) :
            res = target - nums[i]
            if res in mp : 
                return [ i, mp[res]]
            mp[nums[i]] = i
        
        return [0, 0]
    

