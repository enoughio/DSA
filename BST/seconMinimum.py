class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
         
        res = [float('inf')]

        def treverse(node) :

            if node is None :
                return 
            
            if root.val < node.val < res[0] :
                res[0] = node.val
            treverse(node.left)
            treverse(node.right)

        treverse(root)
        return res[0] if res[0] != float('inf') else  -1