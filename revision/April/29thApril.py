# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: 
        self.maxi = 0

        def DFS(node) : 

            if node is None : 
                return 0
            
            l = DFS(node.left)
            r = DFS(node.right)

            self.maxi = max(self.maxi, l+r)

            return max(l, r) + 1

        DFS(root)
        return  self.maxi

        