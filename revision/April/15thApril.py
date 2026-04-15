class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        def rec(idx, arr, total ) : 

            
            if total == target : 
                print(arr)
                ans.append(arr.copy())
                return 

            if idx >= n :     # if we reached maximum index
                return 
        
            if total > target : # if the sum ovflows then stop 
                return
            
            arr.append(candidates[idx])
            rec(idx, arr, total+candidates[idx] )  # reuse the same index
            arr.pop()
            
            rec(idx+1, arr , total )  


        n = len(candidates)
        ans = []
        rec(0,[],0)
        return ans

