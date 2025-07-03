class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt  = 0

        for i in range( len(nums) ) :
            sum = 0 
            for j in range( i, len(nums) ) : 
                sum = sum + nums[j]

                if sum == k : 
                    cnt =  cnt + 1
                
        return cnt 



        # ======================================



        class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        map = { 0 : 1 }

        sum =  0
        cnt = 0

        for i in range(len(nums)) : 

            sum =  sum + nums[i]
            if( ( sum - k ) in map  ) : 
                cnt =  cnt + map[sum-k]
            
            map[sum] = map.get(sum, 0) + 1

        return cnt