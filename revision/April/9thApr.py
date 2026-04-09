class Solution:
    def validStrings(self, n: int) -> List[str]:
        

        def rec(i, st) :
            if i == n :
                ans.append(st)
                return

            if i == 0 : 
                rec(i+1, "0")
            elif i > 0 and st[-1] != "0" :
                rec(i+1, st+"0")
            
            rec(i+1, st+"1")


        ans = []
        rec(0, "")
        return ans




