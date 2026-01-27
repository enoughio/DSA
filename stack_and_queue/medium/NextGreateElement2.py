#=======================
#Brure force solution
# #


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [-1] *n
        cnt = 0
        
        for i in range(n) : 
            idx = i + 1
            while  idx < i + n :
                c = idx % n
                if nums[c] > nums[i] :
                    ans[i] = nums[c]
                    break
                idx += 1

        return ans 
    
#===================================



class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [0] * n

        for i in range((2*n) - 1, -1 , -1) : 
            
            if stack and stack[-1] > nums[i % n] : 
                ans[i%n] = stack[-1]
            elif stack : 
                while stack and stack[-1] <= nums[i % n] : 
                    stack.pop()
                if stack :
                    ans[i%n] = stack[-1]
                    
            if len(stack) == 0 : 
                ans[i%n] = -1
    
            stack.append(nums[i%n])

        e = 0
        maxi = nums[0]
        for i, num in enumerate(nums) :
            if num > maxi :
                e = i
                maxi = nums[i]

        ans[e] = -1
        return ans 




# ------------------------------------------revision---------------
            
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [-1]*n

        for idx, elem in enumerate(nums) : 
            
            for j in range(idx, idx + n) : 
                i = j%n
                if nums[i] > elem : 
                    ans[idx] = nums[i]
                    break

        return ans 