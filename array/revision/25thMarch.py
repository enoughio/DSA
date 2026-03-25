class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        self.rec("", res, 0, 0, n )
        return res


    def rec(self, st, res, op, cl, n) : 
        
        if op <= cl and cl >= n : 
            res.append(st)
            return
        

        if op < n :
            self.rec(st + "(" , res, op+1, cl, n)
        if cl < op :
            self.rec(st + ")", res, op, cl+1, n)


# ----------------


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    
        ans = []
        self.fn([], 0, 0, target, ans, candidates)
        return ans


    def fn(self, arr, i, sum,t, ans, candidates) : 

        if sum == t : 
            ans.append(arr.copy())
            return 
        
        if sum > t :
            return 

        if i >= len(candidates) : 
            return


        self.fn(arr+[candidates[i]], i, sum+candidates[i], t, ans, candidates)
        self.fn(arr, i+1, sum, t, ans, candidates)

