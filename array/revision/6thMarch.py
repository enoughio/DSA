class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        cnt = 0
        n = len(nums)

        for i in range(n) : 
            
            for j in range(n):   
                
                if i == j : 
                    continue
               

                res = nums[i] + nums[j]
                if res == target : 
                    cnt += 1
        
        return cnt


        # ---------------------optimized-----------


        class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        freq = Counter(nums)
        
        ans = 0 
        for k in nums : 
            if target.startswith(k): 
                suffix = target[len(k):]
                ans += freq[suffix]
                if k == suffix: ans -= 1
        return ans 
    

    # ---=-------more optimal---------

    from collections import Counter
from typing import List

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        freq = Counter(nums)
        ans = 0 
        for k, v in freq.items(): 
            if target.startswith(k): 
                suffix = target[len(k):]
                ans += v * freq[suffix]
                if k == suffix: ans -= freq[suffix]
        return ans