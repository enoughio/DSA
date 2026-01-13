class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        n = len(nums)

        slow, fast = 0,0

        while True  : 
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            if slow == fast : break
        
        slow2 = 0 
        while True : 
            slow =  nums[slow]
            slow2 =  nums[slow2]

            if slow == slow2 : 
                break 
            
        return slow 
        






        # hashtab = {}

        # for i in nums : 
        #     if i in hashtab : return i 
        #     hashtab[i] = 1

        # return nums[n-1]

        # nums.sort()

        # prev = nums[0]
        # for i in range(1, n) : 
        #     if prev == nums[i] :
        #         return nums[i]
        #     prev = nums[i]
        
        return nums[n-1]

        # dig_xor = 0

        # for i in range(1, n) :
        #     dig_xor = i ^ dig_xor

        # nums_xor = 0
        # for i in nums :
        #     nums_xor = nums_xor ^ i

        # return nums_xor ^ dig_xor