class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        mp = {}
        mx = 0

        for i in nums : 
            if i % 2 == 0 : 
                cnt = mp.get(i, 0) + 1
                mx = max(cnt, mx)
                mp[i] = cnt

        
        candi = []
        ans = -1
        cnt = 0
        
        for key, val in mp.items() : 
            if val > cnt : 
                ans = key
                cnt = val
            elif val == cnt and key < ans : 
                ans = key
        
        return ans