# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        q = deque()
        q.append((root, 0))
        
        max_width = 1

        while q :
            n = len(q)
            f_idx = float('inf')
            l_idx = float('-inf')

            for _ in range(n) : 

                elem = q.popleft()
                l_idx = max(l_idx, elem[1])
                f_idx = min(f_idx, elem[1])

                
                if elem[0].left : 
                    idx = ( (2 * (elem[1]-1) ) + 1 )
                    q.append((elem[0].left, idx))
                
                if elem[0].right : 
                    idx = ( (2 * (elem[1]-1) ) + 2 )
                    q.append((elem[0].right, idx))
                                    
            width = (l_idx -  f_idx) +1
            max_width = max(max_width, width )
    

        return max_width
    

    # ----- solved one question ----
    
    class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        
        l = root.left.val
        r = root.right.val

        if r+l == root.val : 
            return True
        return False
        

        # ------  


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
                return [True, -1] 
            
            l = rec(node.left)
            if  l[0] == False  : 
                return [False, 0] 
            
            r = rec(node.right)
            if  r[0] == False  : 
                return [False, 0]
            
            
            if ( l[1] == -1 and r[1] == -1 ) : 
                return [True, node.data]
            
            if( l[1] != -1 and r[1] == -1 ) or r[1] != -1 and l[1] == -1 : 
                return [False, -1]
            
            if ( (l[1] + r[1]) != node.data  ) : return [False, -1]
            
            return [True, node.data]
                
                
        rs = rec(root)
        return rec[0]
