class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        ans = ''
        n = len(num)
        st = []

        if n == k : 
            return '0'

        for c in num : 
            while k > 0 and  st and st[-1] > c : 
                st.pop()
                k-=1            
            st.append(c)


        while k != 0 and st : 
            st.pop()
            k-=1

        if not st : 
            return '0' 

        # while st : 
        #     ans = st[-1] + ans
        #     st.pop()
        
        i = 0
        while len(st) > i and st[i] == "0" :
            i += 1
        st = st[i:]

        if len(st) == 0 : 
            return '0'
        return ''.join(st)




