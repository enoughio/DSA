# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        pos = root

        def fun(node) :

            nonlocal val
            nonlocal pos

            if node is None : 
                return 
            
            if node.val > val : 
                pos = node
                fun(node.left)
            else : 
                pos = node
                fun(node.right)


        if root is None : 
            return TreeNode(val)

        fun(root)

        if  val > pos.val  : 
            pos.right =  TreeNode(val)
        else : 
            pos.left =  TreeNode(val)

        return root
