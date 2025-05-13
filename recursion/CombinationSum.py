class Solution:
    def combinationSum(self, candidates, K: int):
        ans = []    

        def rec(i, r, ds):
            if(r == 0):
                ans.append(ds.copy())
                return

            if r < 0: 
                return
            
            if i >= len(candidates) :
                if r == 0 :
                    ans.append(ds.copy())
                return

            if candidates[i] <= r :
                ds.append(candidates[i])
                rec(i, r - candidates[i], ds)
                ds.pop()
            rec(i+1, r , ds)

        rec(0, K, [])
        return ans



s = Solution()
candidates = [8, 7, 4, 3]
K = 11
print(s.combinationSum(candidates, K))
# Output: [[2, 2, 3], [7]]