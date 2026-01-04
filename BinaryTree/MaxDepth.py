# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def fn(root, cnt) : 

            if root is None : 
                return cnt

            cnt +=1
            l = fn(root.left, cnt)
            r = fn(root.right, cnt)

            return max(l, r)

        return fn(root, 0)
