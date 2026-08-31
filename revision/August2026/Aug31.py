class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # n = len(nums)
        cnt1 = 0
        cnt2 = 0

        el1 = float("-inf")
        el2 = float("-inf")
        
        for n in nums : 
            
            if cnt1 == 0 and el2 != n : 
                el1 = n
                cnt1 = 1
            elif cnt2 == 0 and el1 != n :
                el2 = n
                cnt2 = 1
            elif n == el1 : 
                cnt1 += 1
            elif n == el2 : 
                cnt2 += 1
            else : 
                cnt1 -=1
                cnt2 -=1


        mini = len(nums)//3
        cnt1 = 0 
        cnt2 = 0
        for i in nums : 
            if i == el1 : 
                cnt1 += 1
            elif i == el2 : 
                cnt2 += 1

        ans = []

        if cnt1 > mini : 
            ans.append(el1)
        if cnt2 > mini : 
            ans.append(el2)

        return ans 