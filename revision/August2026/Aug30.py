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

    # ------- brute force ---------


    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = set()
        mp = {}
        
        for i in nums : 
            cnt = mp.get(i, 0) + 1 
            mp[i] = cnt

            if cnt > (n//3)  : 
                ans.add(i)
        return list(ans) 


# ---------------- majourity elem 1 ------
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        cnt = 0
        el = None 

        for i in nums : 

            if cnt == 0 : 
                el = i
                cnt = 1
            elif i == el : 
                cnt +=1
            else : 
                cnt -=1
        
        return el




