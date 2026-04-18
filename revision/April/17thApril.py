class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        def rec(i, arr, t) : 

            if i >= n : 
                if t == 0 : 
                    ans.append(arr.copy())
                return 
            
            if t < 0 : 
                return 

            arr.append(candidates[i])
            rec(i+1, arr, t - candidates[i])
            arr.pop()

            while i+1 < n and candidates[i] == candidates[i+1] :
                i+=1

            rec(i+1, arr, t)


        n = len(candidates)
        ans = []

        rec(0, [], target)
        return ans

        # --------------------subset 1 ----------------

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def rec(i, arr): 

            if i == n : 
                ans.append(arr.copy())
                return 
            
            rec(i+1, arr + [nums[i]])
            rec(i+1, arr)
        
        ans = []
        n = len(nums)
        rec(0, [])
        return ans

# ---------------- subset 2 ----------------

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def rec(i, arr) : 

            if i == n :
                ans.append(arr.copy())
                return 
            
            rec(i+1, arr + [nums[i]])
            while i+1 < n and nums[i] == nums[i+1] : i+=1
            rec(i+1, arr )
        
        ans = []
        n = len(nums)
        rec(0, [])
        return ans


