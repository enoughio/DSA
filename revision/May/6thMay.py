'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def boundaryTraversal(self, root):
        # code here 
    
        ls = []
        def left(node) : 
            
            if node is None : return
            
            if node.left : 
                
                ls.append(node.data)
                left(node.left)
                
            else : 
                
                ls.append(node.data)
                left(node.right)
            
            
        
        rs = []
        def right(node) : 
            
            if node is None : return
        
            if node.right : 
                
                rs.append(node.data)
                right(node.right)
            
            else :
                
                rs.append(node.data)
                right(node.left)
            
            return 
            
        bt = []
        def bottom(node) : 
            
            
            if node is None : 
                return
            
            if node.left is None and node.right is None : 
                bt.append(node.data)
                return 
            
            bottom(node.left)
            bottom(node.right)
            
            return
    
        
        ans = []
        
        if root : 
            ans.append(root.data)
            
        if root.left : 
            left(root.left)
        if root.right : 
            right(root.right)
        if root.left is not None or root.right is not None : 
            bottom(root)
        
        if rs : 
            rs.pop()
        if ls : 
            ls.pop()
            
        
        for i in ls : 
            ans.append(i)
        
        for j in bt : 
            ans.append(j)
        
        rs.reverse()
        for k in rs : 
            ans.append(k)
        
        return ans
            


# --------------vertical order treversal -------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        self.mp = {}
        self.maxl = 0 
        self.maxR = 0 

        def rec(node, row, col) : 

            if node is None : 
                return 

            if col not in self.mp : 
                self.mp[col] = []

            self.mp[col].append(node.val)
        
            rec(node.left, row+1, col-1)
            self.maxl = min(self.maxl, col)

            rec(node.right, row+1, col+1)
            self.maxR = max(self.maxR, col)
        

        ans = []
        rec(root, 0, 0)

        # print(self.maxl)
        # print(self.maxR)

        for i in range(self.maxl, self.maxR+1, 1) : 

            if i in self.mp : 
                self.mp[i].sort()
                ans.append(self.mp[i])

                
        return ans 


