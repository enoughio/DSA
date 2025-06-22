

class Solution:
    def generateParenthesis(self, n: int):
        
        ans = []
        st = '('
        open = 1
        close = 0
        self.rec(ans, st, open, close, n)
        return ans

    def rec(self, ans, st, open, close, n):
        if len(st) >= n*2:
            if( open  == close ):
                ans.append(st)
            return

        if(open < n):
            self.rec(ans, st + '(', open + 1, close, n)

        if( open > close):
            self.rec(ans, st + ')', open, close + 1, n)

        return
        

## caller fuction

s = Solution()
print(s.generateParenthesis(8)) # ["((()))","(()())","(())()","()(())","()()()"]


# ==========================

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def rec(st, open, close):
            
            if  len(st) == n*2 :
                ans.append(st)
                return

            if open != n :
                rec( st + '(', open + 1, close)
            
            if(open > close):
                rec(st + ")", open, close + 1)
            
        rec("", 0, 0)
        return ans
 

#  +====================