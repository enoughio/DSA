class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def rec(op, cl, st) : 

            if op == cl and op == n: 
                ans.append(st)
                return 
            
            if op != n : 
                rec(op+1, cl, st+"(" )
            
            if cl < op :
                rec(op, cl+1, st+")" )

        ans = []
        rec(1, 0, "(")
        return ans 