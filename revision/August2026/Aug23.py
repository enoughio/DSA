class Solution:
    def decodeString(self, s: str) -> str:
        
        def generator(reps, st) :
            block = ''
            
            for i in range(reps) :
                block = block + st

            return block

        ans = ""
        stk = []
        i = 0

        while i < len(s) : 

            if s[i] == ']' : 

                st = ''
                while stk and stk[-1] != '[' : 
                    el = stk.pop()
                    st = el + st 
                
                rep = ''
                while stk and stk[-1].isdigit() : 
                    dig = stk.pop()
                    rep = dig + rep

                if rep  == '' : 
                    rep = '0'
                rep = int(rep)
                block = generator(rep, st)

                for c in block : 
                    stk.append(c)
                
            else : 
                stk.append(s[i])
            
            i+=1

        n = len(stk)
        for i in range(n-1, -1, -1) : 
            ans = stk.pop() + ans
        
        return ans 
    


# --------------------- final Solution --------------

class Solution:
    def decodeString(self, s: str) -> str:
        
        def generator(reps, st) :
            block = ''
            
            for i in range(reps) :
                block = block + st

            return block

        ans = ""
        stk = []
        i = 0

        while i < len(s) : 

            if s[i] == ']' : 

                st = ''
                while stk and stk[-1] != '[' : 
                    el = stk.pop()
                    st = el + st 
                
                stk.pop()
                
                rep = ''
                while stk and stk[-1].isdigit() : 
                    dig = stk.pop()
                    rep = dig + rep

                if rep  == '' : 
                    rep = '0'
                rep = int(rep)
                block = generator(rep, st)

                for c in block : 
                    stk.append(c)
                
            else : 
                stk.append(s[i])
            
            i+=1

        n = len(stk)
        for i in range(n-1, -1, -1) : 
            ans = stk.pop() + ans
        
        return ans 