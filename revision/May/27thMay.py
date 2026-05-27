# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def dfs(node, val) : 

            if node is None : return None

            if node.val == val :
                return node
            elif node.val > val : 
                return  dfs(node.left, val)
            elif node.val < val : 
                return dfs(node.right, val)
            
        return dfs(root, val)
