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

            st.append(num[i])
    
        while k > 0 : 
            st.pop()
            k = k-1
        
        res = ""
        while st :
            # res = res + int(st.pop()) 
            res = st.pop() + res
        
        i = 0
        while i < len(res) and res[i] == '0' : 
            i += 1

        ste = ""
        for j in range(i, len(res)) : 
            ste = ste + res[j]

        if not ste : 
            return "0"
        return ste
        
