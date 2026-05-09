# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        def search(node, p , q) : 
            
            if node is None : 
                return None

            if node.val == q  or node.val == p : 
                return node

            l = search(node.left, p, q)
            r = search(node.right, p, q)

            if r is None and l is None : 
                return None
            
            if r and not l :  
                return r 

            if not r and  l :
                return l 

            if r and l : 
                return node  

        
        return search(root, p.val, q.val)
  
        
        