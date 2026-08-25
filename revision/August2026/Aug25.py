class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [0] * n
        # mul = 1

        for i in range(n) : 

            mul = 1
            for j in range(n)  : 
                if j ==  i : 
                    continue 
                mul =  mul * nums[j]
            
            ans[i] = mul
        
        return ans


# -------------- soled product of array except self -----------


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [0] * n
        post = [0] * n

        mul = 1
        for i in range(n-1, -1, -1) :
            mul = mul * nums[i]
            post[i] = mul
        
        cur = 1
        for i in range(n-1) : 
            till = post[i+1]
            ans[i] = till * cur 
            cur = cur * nums[i]
        
        ans[-1] = cur

        return ans 
        