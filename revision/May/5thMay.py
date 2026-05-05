# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None and q is None : 
            return True
        
        if p and not q :
            return False 
        
        if q and not p : 
            return False 
        
        if q.val != p.val : 
            return False 
        
        l = self.isSameTree(q.left, p.left)
        r = self.isSameTree(q.right, p.right)

        return (l and r)