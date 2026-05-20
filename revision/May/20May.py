# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

        def build(mp, i, j, inorder, k, l, preorder ) : 

            if i == j and k == l : 
                return None 
            
            x = preorder[k]
            root = mp[x] 
            left  = build( mp, i, root -1, inorder, k+1, k + (root - i), preorder)
            right  = build( mp, root + 1, j, inorder, k+ (root - i), l , preorder)

            root.left  = left
            root.right = right
        
            return root
        
        
        
        
        
        mp = { }

        n = len(inorder)
        for i in range(n) : 
            mp[inorder[i]] = i
        
        return build(mp, 0, n, inorder, 0, len(preorder), preorder)
        
       