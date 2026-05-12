'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        # code here
        
        def rec(node) : 
            
            if node is None : 
                return 1
            
            if not node.left and not node.right : 
                return 1
            
            left = 0 if not node.left else node.left.data 
            right = 0 if not node.right else node.right.data 
                
            isSum = 1 if ( left + right ) == node.data  else 0
        
            return isSum * rec(node.left) * rec(node.right)
            
        
        return  rec(root)