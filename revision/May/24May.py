# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        
        def build(mp, inorder, i, j, postorder, p, q ) : 

            if i > j or p > q:
                return None
            
            if j < i  or p > q  : 
                return None
            
            rootVal = postorder[q]
            rootIdx = mp[rootVal]

            root = TreeNode(rootVal) 

            left = build(mp, inorder, i, rootIdx-1, postorder, p, q - (j-rootIdx)-1 )
            right = build(mp, inorder, rootIdx+1, j, postorder, q-(j-rootIdx), q-1 )

            root.left = left
            root.right = right

            return root
        
        
        mp = { }

        n = len(inorder)
        for i in range(n) : 
            mp[inorder[i]] = i
        
        return build(mp, inorder, 0, n-1, postorder, 0, n-1)
        