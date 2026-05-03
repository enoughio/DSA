
# ----------- more optimized -------------

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        n = len(num)
        
        if k >= n : 
            return "0"

        st = []
        for i in range(n) : 

            while st and k > 0 and int(st[-1]) > int(num[i]) : 
                st.pop()
                k = k-1
            
            if not st and num[i] == "0" : 
                continue
            
            st.append(num[i])
    
        while st and k > 0 : 
            st.pop()
            k = k-1
        
        res = "".join(st)
        if res == "" : 
            return "0"
        return res

      
        

        
