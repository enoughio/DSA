class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        for i in range(n) : 
            nums.append(nums[i])
        
        return nums
    

# ---------------------------- 


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=  len(t) : 
            return False 

        s = sorted(list(s))
        t = sorted(list(t))

        for i in range(len(s)) : 
            if s[i] != t[i] : 
                return False 
            
        return True 
    

# ----------------

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        cnt = 300

        for i in range(1, len(strs)) : 
            j = 0
            while ( j < len(strs[0]) and j < len(strs[i]) ) and strs[0][j] == strs[i][j] : 
                j += 1
            
            cnt = min(cnt, j)
        
        return strs[0][0:cnt]