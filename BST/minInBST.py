class Solution:
    def minValue(self, root):
        # code here
        
        def find(node) : 
            

                
            if node.left is None : 
                return node.data
                
            if node.left : 
                return find(node.left)
            
            
        return find(root)