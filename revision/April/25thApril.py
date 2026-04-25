class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [-1]*n

        for idx, k in enumerate(nums) : 

            i = 0
            id = idx+1

            while i < n : 

                if nums[id%n] > k : 
                    ans[idx] = nums[id%n]
                    break
                i+=1
                id += 1
            
        return ans
    
    # ----------- optimized solution ----------

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [-1]*n
        st = []

        for i in range(2*n-1, -1, -1) : 
            idx = i%n

            while st and st[-1] <= nums[idx] : 
                st.pop()
            
            if i < n and st : 
                    ans[i] = st[-1]

            st.append(nums[idx])
                
                
        return ans


# --------------- Max Depth of Binary tree ------------ 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None : 
            return 0
            
        return self.DFS(root)

    
    def DFS(self, node) : 

        if node is None : 
            return 0
        
        r = self.DFS(node.left)
        l = self.DFS(node.right)

        return max(l,r) + 1
    
    