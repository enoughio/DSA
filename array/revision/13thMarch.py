
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


# ----------------------revers string----------


class Solution:
    def reverseWords(self, s: str) -> str:
        
        n = len(s)
        st = 0 
        ed = n-1
        ans = ""

        # trim front space 
        while s[st] == " " :
            st+=1
            
        # trim back space 
        while s[ed] == " " :
            ed-=1
         

        while st <= ed :

            temp = ""
            while st <= ed and s[st] != " " :
                temp += s[st]
                st+=1

            if ans != "" : 
                ans = temp+ " " + ans
            else : 
                ans = temp + ans 


            
            # remove extra space 
            while st <ed and s[st] == " " :
                st+=1

        return ans
