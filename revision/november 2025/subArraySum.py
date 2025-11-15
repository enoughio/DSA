from typing import List
# this only works for non-negative numbers    

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        cnt = 0

        st = 0
        ed = 0
        sum = nums[0]

        while(ed+1 < n and st < n) : 

            ed += 1
            sum += nums[ed]

            while sum > k : 
                sum -= nums[st]
                st+=1

            if st > ed :
                ed = st 
                if st < n :
                    sum = nums[st]
                

            if sum == k :
                cnt +=1 


        while st < n : 
            sum -= nums[st]
            st+=1

            if sum == k : 
                cnt += 1


        return cnt


