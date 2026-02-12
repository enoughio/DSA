# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:


        def fun(node) : 
            if node is None or node.left  is None : 
                return node
            left = fu(node.left) 
            if node.right :
                left.right = node.right
            else : 
                left.right = None

            return left
    
 
        def fu(node) : 
            if node.left : 
                node = node.left
                return fu(node)
            else : 
                return node

        if root is None : 
            return root

        if root.val == key : 
            if root.right : 
                left = root.left
                leftMost = fu(root.right)
                leftMost.left = left
                return root.right
            else : 
                return root.left


            
        node = root 

        while( node ) : 

            if node.val > key : 
                if node.left  and node.left.val == key : 
                    node.left = fun(node.left)
                    break
                else  : 
                    node = node.left 

            else : 
                # print("here")
                if node.right  and node.right.val == key : 
                    node.right = fun(node.right)
                    break
                else : 
                    node = node.right
                
        return root
            

            




    