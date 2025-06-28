class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = []

        def rec(arr, sum, i): 

            if len(arr) >= k :
                if sum == n : 
                    ans.append(arr)
                return 
            
            if sum > n : 
                return 

            for j in range(i, 10) :
                rec( arr + [j], sum + j, j+1)
                
        rec([], 0, 1)
        return ans
