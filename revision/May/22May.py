# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

        def build(mp, inorder, i, j, preorder, p, q ) : 

            if i > j or p > q:
                return None
            
            if j < i  or p > q  : 
                return None
            
            rootVal = preorder[p]
            rootIdx = mp[rootVal]

            root = TreeNode(rootVal)

            left  = build( mp, inorder, i, rootIdx-1, preorder, p+1, p+(rootIdx-i))
            right  = build( mp, inorder, rootIdx+1, len(inorder)-1, preorder, p+(rootIdx-i)+1, q )

            root.left  = left
            root.right = right
        
            return root
        
                
        mp = { }

        n = len(inorder)
        for i in range(n) : 
            mp[inorder[i]] = i
        
        return build(mp, inorder, 0, n-1, preorder, 0, n-1)
        
       