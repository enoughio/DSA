class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mp = {}
        for i in nums : 
            mp[i] = 1 + mp.get(i, 0)

        arr = []
        for val, cnt in mp.items() : 
            arr.append( [val, cnt ] )
        
        arr.sort( key = lambda x : x[1], reverse= True)    # sort based on 2nd element
        ans = []


        for i in range(k) : 
            ans.append(arr[i][0])

        return ans 
        

class Solution:
    def decodeString(self, s: str) -> str:
        
        
        def generator(reps, st) :
            block = ''
            
            for i in range(reps) :
                block = block + st

            return block



        ans = ""
        reps = 0
        st = ""
        
        for i in range(len(s)) :

            if s[i] > '0' and s[i] <= '9' : 
                reps = int(s[i])
            elif s[i] == '[' : 
                continue 
            elif s[i] == ']' : 
                block = generator(reps, st) 
                ans = ans + block
                st = ''
                reps = 0
            else : 
                st = st + s[i]
            
        return ans
        
