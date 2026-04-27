# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def DFS(node) : 
            
            if node is None : 
                return (True, 0)

            l = DFS(node.left) 
            if l[0] == False : 
                return (False, 0 )
            r = DFS(node.right)
            if r[0] == False : 
                return (False, 0 )
            
            if abs(l[1] - r[1]) > 1 : 
                return (False, max(l[1], r[1]) + 1 ) 

            res = (l[0] and r[0], max(l[1], r[1]) + 1 )
            return res 

      
        res = DFS(root)
        return res[0]