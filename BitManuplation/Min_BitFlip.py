class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        cnt = 0
        while start > 0 or goal > 0 : 
            st = start & 1
            ed = goal & 1

            if st != ed : 
                cnt += 1
            
            start = start >>  1
            goal = goal >>  1

        return cnt
    

# ==========================

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        num =  start ^ goal
        cnt  = 0
        while num > 0 :
            cnt += num & 1 
            num >>= 1

        return cnt