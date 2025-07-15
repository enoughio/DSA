
class Solution:
    def findXOR(self, l, r):
        # Code here
        def finder(n): 
            if n % 4 == 1 : return 1
            if n % 4 == 2 : return n+1
            if n % 4 == 3 : return 0
            if n % 4 == 0 : return n
                
        return finder(l-1) ^ finder(r)