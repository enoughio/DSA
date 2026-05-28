
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
            
            
            def findRight(node, parent) : 

                if node.right is None : 
                    return node
    
                return findRight(node.right)

            
            def helper(node) : 

                if node.left is None : 
                    return node.right
                elif node.right is None : 
                    return node.left

                lastRight = findRight(node.left)
                lastRight.right = node.right

                return node.left
        
                


            if node is None : 
                return None
            
            if root.val == key : 
                return helper(root)
            
            while node != None : 
                
                if node.val <= key : 
                    if node.val == key : 
                        return helper(node)
                    else :  
                        node = node.left
                else :  
                    node = node.left
                    
            
