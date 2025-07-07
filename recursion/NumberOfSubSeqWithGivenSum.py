class Solution:
    def numSubseq(self, nums: List[int], t: int) -> int:

        def rec(arr, m, mx, i):

            if i == len(nums) : 
                sum = m + mx 
                if sum <= t : 
                    ans.append(arr)
                return

            rec(arr + [nums[i]], min(m, nums[i]), max(mx, nums[i]), i+1)
            rec(arr, m, mx, i+1)
                 
        ans = []
        rec([], float('inf'), float('-inf'), 0)
        return len(ans)
    


    # =========================BRUTE========================


class Solution:
    def numSubseq(self, nums: List[int], t: int) -> int:

        nums.sort()
        res = 0
        mod = ( 10 ** 9 ) + 7

        right = len(nums) - 1
        for i,left in enumerate(nums ) : 

            while i <= right and ( left +  nums[right] ) > t :
                right -= 1
            
            if i <= right : 
                res +=  ( 2**( right - i) )
                res %= mod

        return res
