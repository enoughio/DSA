''' class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,node, val):
        # code here
        
        def fun(node) : 
            
            nonlocal ans
            
            if node is None : 
                return 
            
            if node.data == val : 
                ans = node.data
                return
            elif node.data > val : 
                ans = node.data 
                fun(node.left)
            else : 
                fun(node.right)
            
        if root is None : 
            return None
            
        ans = -1
        fun(root)
        return ans
        