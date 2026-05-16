# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        self.cnt = 0
        def rec(node) :
            
            if node is None : 
                return
            
            self.cnt +=1
            rec(node.left)
            rec(node.right)

        rec(root)
        return self.cnt
    

    # ------------ optimized one --- 

    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:         

        def findLeftHeight(node) :
            height = 0
            while node : 
                height +=1
                node = node.left
            return height
   
        def findRightHeight(node) :
            height = 0
            while node :  
                height += 1
                node = node.right
            return height


        def rec(node) :
            if node is None : 
                return 0
            
            lh = findLeftHeight(node.left)
            rh = findRightHeight(node.right)
            
            if lh == rh : 
                return (2 << lh) - 1
            
            return 1 + rec(node.left) + rec(node.right)    

        return rec(root)