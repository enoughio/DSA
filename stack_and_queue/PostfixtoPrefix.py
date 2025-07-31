#postfix to prefix


class Solution : 

    def convert(self, s) : 
        
        stack = []
        
        for i in s :
            if ( i >= 'a' and i <= 'z' ) or ( i >= 'A' and i <= 'Z' ) or ( i >= '0' and i <= '9' ) : 
                stack.append(i)
            elif stack : 
                t1 = stack[-1]
                stack.pop()
                t2 = stack[-1]
                stack.pop()

                st = f'{i}{t2}{t1}'
                stack.append(st)

        return stack[-1] if stack else None


obj = Solution()
print(obj.convert("AB-DE+F*/"))
