
# this hvae given me TLE 

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        MOD = ( 10**9 ) + 7
        nums.sort()

        def rec(i, mini, maxi, arr) : 

            if i == n : 
                if len(arr) > 0 and (maxi + mini)  <= target : 
                    print(arr.copy())
                    ans.append(arr.copy())
                return 
            
            arr.append(nums[i])
            rec(i+1,  min( MOD, min(mini, nums[i])), min(MOD, max(maxi, nums[i])), arr )
            arr.pop()
            rec(i+1, mini, maxi, arr )
        
        ans = []
        rec(0, float('inf'), float('-inf'), [])
        return len(ans)



#-----------  optimized ------------


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        MOD = ( 10**9 ) + 7
        nums.sort()
        ans =  0

        r = n-1
        for l, val in enumerate(nums) : 

            if l > 0 and nums[l-1] == nums[l] : 
                ans += int(2** (r-l)) % MOD
                continue

            while r >= l and nums[r] + nums[l] > target : 
                r-=1

            if l <=  r : 
                ans += int(2** (r-l)) % MOD


        return ans % MOD


