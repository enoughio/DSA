class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        n = len(s)

        def check(st, ed) : 

            while st <= ed :
                if s[st] != s[ed] :
                    return False

                st += 1
                ed -= 1
            
            return True

        def rec(k, arr): 

            if k == n:
                ans.append(arr.copy())
                return 

            for i in range(k, n) :
                if check(k, i) : 
                    arr.append(s[k:i+1])
                    rec(i+1, arr )
                    arr.pop()
        

        rec(0, [])
        return ans

