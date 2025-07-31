
# postfix to infix conversion 


class solution : 

    def convert(self, s) : 
        stack = []

        for i in s : 

            if ( i >= 'a' and i <= 'z' ) or ( i >= 'A' and i <= 'Z' ) or ( i >= '0' and i <= '9' ) : 
                stack.append(i)
            
            elif stack : 
                
                t2 = stack[-1]
                stack.pop()
                t1 = stack[-1]
                stack.pop()

                st = f'( {t1} {i} {t2} )'
                stack.append(st)
            
        return stack[-1] if stack else None
    


obj = solution()
print(obj.convert("AB-DE+F*/"))
