    

def majorityElement(self, nums: List[int]) -> List[int]:
        mp = {}
        n= len(nums)
        x = (n//3)
        ans = set()

        if n <= 2 : 
            return list(set(nums))

        for i in nums : 
            if i in mp : 
                mp[i] += 1
                if mp[i] > x :
                    ans.append(i)
            else : 
                mp[i] = 1

        return list(ans)



class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        el1 = float('inf')
        el2 = float('inf')
        cnt1 = 0
        cnt2 = 0
        n = len(nums)
        
        if n <= 2 : 
            return list(set(nums)) 
        
        for i in nums : 

            if cnt1 == 0 and i != el2 : 
                cnt1 = 1 
                el1 = i
            elif cnt2 == 0 and i != el1 : 
                cnt2 = 1 
                el2 = i
            elif i == el1 : 
                cnt1 += 1
            elif i == el2 : 
                cnt2 += 1
            else : 
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = 0
        cnt2 = 0
        for i in nums : 
            if i == el1 :
                cnt1 += 1
            if i == el2 :
                cnt2 += 1

        x = n // 3
        
        ans = []
        if cnt1 > x :
            ans.append(el1)
        if cnt2 > x :
            ans.append(el2)


        return ans
                



