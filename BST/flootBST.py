'''
# Node Class:
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def floor(self, root, val):
        # code here
           
        def fun(node) : 
            
            nonlocal ans
            
            if node is None : 
                return 
            
            if node.data == val : 
                ans = node.data
                return
            elif node.data < val : 
                ans = node.data 
                fun(node.right)
            else : 
                fun(node.left)
            
        if root is None : 
            return None
            
        ans = -1
        fun(root)
        return ans
        