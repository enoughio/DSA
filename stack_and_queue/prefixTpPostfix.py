


#prefix to postfix 


class Solution : 

    def convert(self, s) : 
        
        stack = []
        
        for i in range(len(s)-1, -1, -1) :
            if ( s[i] >= 'a' and s[i] <= 'z' ) or ( s[i] >= 'A' and s[i] <= 'Z' ) or ( s[i] >= '0' and s[i] <= '9' ) : 
                stack.append(s[i])
            elif stack : 
                t1 = stack[-1]
                stack.pop()
                t2 = stack[-1]
                stack.pop()

                st = f'{t1}{t2}{s[i]}'
                stack.append(st)

        return stack[-1] if stack else None


obj = Solution()
print(obj.convert("/-AB*+DEF"))
