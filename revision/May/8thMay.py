# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        def search(node, t, ans) : 
            
            if node is None : 
                return (False, ans) 

            ans.append(node)

            if node.val == t : 
                return (True, ans)
            
            l = search(node.left, t, ans ) 
            if l[0] is True : 
                return (True, ans)

            r = search(node.right, t, ans )
            
            if r[0] is True  : 
                return (True, ans)
            
            
            ans.pop()
            return (False, ans)  
            
        
        a1 = []
        s = search(root, p.val, a1)
  
        a2 = []
        s2 = search(root, q.val, a2)
      

        n = len(a1)
        m = len(a2)
        i , j  = 0, 0
        ans = a1[0]

        while i < n and j < m : 
            if a1[i].val == a2[j].val : 
                ans = a1[i]

            i += 1
            j += 1

        return ans
    