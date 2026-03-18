class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        m = len(s)
        n = len(t)

        if m == 0 : return True
        if m == n and n == 0 : return True

        if m > n : return False

        while i < n and j < m : 
            if s[j] == t[i] : 
                i+=1
                j+=1
                if j >= m : 
                    return True
            else : 
                i+=1
                
        print(i, j)
        return False