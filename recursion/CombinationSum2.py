class Solution:
    def combinationSum2(self, candidates, K: int):
        

        # def rec(arr, i, sum):
        #     if(i == len(candidates)):
        #         if(sum == 0):
        #             arr.sort()
        #             ans.append(arr.copy())
        #         return
            
        #     if(sum == 0):
        #         arr.sort()
        #         ans.append(arr.copy())
        #         return
        
        #     rec(arr, i+1, sum)
        #     if candidates[i] <= sum :
        #         arr.append(candidates[i])
        #         sum = sum - candidates[i]
        #         rec(arr, i+1, sum )
        #         arr.pop()
        
        # ans = []
        # rec([], 0, target)
        # return ans

        def rec(i, r, ds):

            if(r == 0):
                st = ds.copy()
                st.sort()
                st = tuple(st)
                ans.add(st)
                return

            if r < 0: 
                return
            
            if i >= len(candidates) :
                if r == 0 :
                    st = ds.copy()
                    st.sort()
                    st = tuple(st)
                    ans.add(st)
                return

            if candidates[i] <= r :
                ds.append(candidates[i])
                rec(i+1, r - candidates[i], ds)
                ds.pop()
            rec(i+1, r , ds)

        ans = set()
        rec(0, K, [])
        res = list(ans)
        return res


s = Solution()
arr = [10, 1, 2, 7, 6, 1, 5, 2, 3, 4, 5, 6, 7, 8, 9]        
K = 8
N = len(arr)
print(s.combinationSum2(arr, K))
