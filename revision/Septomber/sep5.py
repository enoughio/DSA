class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def convert(s) : 
            st = []

            for i in s : 
                if i.isalnum() : 
                    st.append(i.lower())
            return st

        
        def compare(st) : 
            
            n = len(st)

            i = 0
            j = n-1

            while i < j :
                if st[i] != st[j] : 
                    return False

                i+=1
                j-=1

            return True
        
        st = convert(s)
        if 0 == len(st) : 
            return True
        return compare(st)