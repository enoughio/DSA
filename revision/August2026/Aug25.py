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

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        rows = len(matrix)
        n = rows

        cnt = 0

        for cnt in range(n) : 

            row = set()
            col = set()

            for i in range(rows) : 
                row.add(matrix[cnt][i])
            
            for i in range(rows) : 
                col.add(matrix[i][cnt])
            
            if len(row) < n or len(col) < n : 
                return False 
 
        return True
        
