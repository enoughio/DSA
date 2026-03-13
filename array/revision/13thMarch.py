
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
    

        cnt = 0
        ans = []


        for p in s :

            if p is '(' :
                cnt +=1
            else : 
                cnt -=1

            if cnt > 1 and p == '(' :
                ans.append(p)
            elif cnt >= 1 and p == ')' :
                ans.append(p)

        return ''.join(ans)


