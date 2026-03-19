class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        cnt1 = 0
        cnt2 = 0
        el1 = -1
        el2 = -1

        for i in nums : 

            if cnt1 == 0 and i != el2 : 
                el1 = i
                cnt1 = 1
            elif cnt2 == 0 and i != el1 : 
                el2 = i
                cnt2 = 1
            elif i == el1 : cnt1+=1
            elif i == el2 : cnt2+=1
            else :
                cnt1-=1
                cnt2-=1

        cnt1 = 0
        cnt2 = 0

        for i in nums : 
            if i == el1 : cnt1 +=1 
            if i == el2 : cnt2 +=1 

        ans = []
        if cnt1 >= floor(len(nums)//3) + 1 : ans.append(el1)
        if cnt2 >= floor(len(nums)//3) + 1 and el2 != el1 : ans.append(el2)
        
        return ans