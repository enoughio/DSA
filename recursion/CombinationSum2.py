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













# ===================================
# TLE solution  

class Solution:
    def combinationSum2(self, candidates: List[int], t: int) -> List[List[int]]:
        
        ans = set()
        n = len(candidates) 

        def rec(arr, sum, i) :

            if n <= i : 
                if sum == t :
                    arr.sort()
                    tup = tuple(arr)
                    ans.add(tup)
                return
            
            if sum == t :
                arr.sort()
                tup = tuple(arr)
                ans.add(tup)
                return 
            
            if sum > t : 
                return                

            if candidates[i] + sum <= t:
                rec(arr + [candidates[i]], sum + candidates[i], i+1)  # reuse current
            rec(arr, sum, i+1)  # skip to next
            


        rec([], 0, 0)
        return list(ans)


# =========================================



class Solution:
    def combinationSum2(self, candidates: List[int], t: int) -> List[List[int]]:
        
        ans = []
        n = len(candidates) 
        candidates.sort()

        
        if(candidates[0] == candidates[-1] and t > candidates[0]*len(candidates)) :
            return []

        def rec(arr, sum, i) :

            if n <= i : 
                if sum == 0 :
                    ans.append(arr)
                return
            
            if sum == 0 :
                ans.append(arr)
                return
            
            for j in range(i, n):

                if( j > i and candidates[j] == candidates[j-1] ):
                    continue

                if candidates[i] > sum :
                    break

                rec(arr + [candidates[j]], sum - candidates[j], j+1)  # take the current 

            # rec(arr, sum, i+1)  # skip to next

        rec([], t, 0)
        return ans
