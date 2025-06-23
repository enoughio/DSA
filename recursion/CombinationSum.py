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








# -------------------------------------------------
class Solution:
    def combinationSum(self, candidates: List[int], t: int) -> List[List[int]]:
        
        ans = []

        def rec(arr, sum, i) :

            if len(candidates) == i : 
                if sum == t :
                    ans.append(arr.copy())

                return
            
            if sum == t :
                ans.append(arr.copy())
                return 
            
            if sum > t : 
                return


            if sum < t:
                if i < len(candidates) :
                    rec(arr + [candidates[i]], i + 1, sum + candidates[i])
                else :
                    return 


            else :
                rec(arr, i + 1, sum)


        rec([], 0, 0)
        return ans

# ===============================================



class Solution:
    def combinationSum(self, candidates: List[int], t: int) -> List[List[int]]:
        
        ans = []
        n = len(candidates) 

        def rec(arr, sum, i) :

            if n <= i : 
                if sum == t :
                    ans.append(arr.copy())
                return
            
            if sum == t :
                ans.append(arr.copy())
                return 
            
            if sum > t : 
                return

            # if candidates[i] + sum  <= t :
            #     rec(arr+[candidates[i]], i, sum + candidates[i])
            # rec(arr, i + 1, sum)
                

            if candidates[i] + sum <= t:
                rec(arr + [candidates[i]], sum + candidates[i], i)  # reuse current
            rec(arr, sum, i+1)  # skip to next
            
            # if candidates[i] + sum  <= t :
            #     arr.append(candidates[i])
            #     rec(arr, sum +  candidates[i], i)
            #     arr.pop()
            # rec(arr, sum, i+1,)


        rec([], 0, 0)
        return ans

