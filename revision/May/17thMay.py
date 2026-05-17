# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        self.parent = None
        def search(node) : 

            if node is None : 
                return self.parent

            self.parent = node
            if node.val > val : 
                rec(node.left)
            else :
                rec(node.left)
                 
            return self.parent
        
        parent = search(root)
        if parent.val > val : 
            parent.left = TreeNode(val)
        else : 
            parent.right = TreeNode(val)

        return root



# -----------------  fixed 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        self.parent = None
        def search(node) : 

            if node is None : 
                return self.parent

            self.parent = node
            if node.val > val : 
                search(node.left)
            else :
                search(node.right)
                 
            return self.parent
        

        if root is None : 
            return TreeNode(val)

        parent = search(root)
        if parent.val > val : 
            parent.left = TreeNode(val)
        else : 
            parent.right = TreeNode(val)

        return root
