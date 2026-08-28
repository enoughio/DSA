class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sm = float('inf')
        mx = float('-inf')

        if len(nums) == 0 : 
            return 0
        elif len(nums) == 1 : 
            return 1


        for i in nums : 
            sm = min(sm, i)
            mx = max(mx, i)
       
        mp = {}
        for i in nums : 
            mp[i] = 1
        

        cnt = 0
        maxi = 0
        next = sm

        while next != mx + 1 : 
            if next in mp : 
                cnt += 1
                next = next + 1
            else : 
                maxi = max(maxi, cnt)
                while next not in mp and next < mx: 
                    next +=1
                cnt = 0
                    
        return max(maxi, cnt)


# ------------------------ sovled longest consucative subsequence -----------
