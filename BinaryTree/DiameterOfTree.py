class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxi = [0]
        def fn( node) :
            
            if node is None : 
                return (0, 0)

            left = fn(node.left)
            right = fn(node.right)

            myHeight = left[0]+right[0]
            maxi[0] = max(maxi[0], myHeight, left[1], right[1])
            return ( 1+max(left[0], right[0]), maxi[0])

        fn(root)
        return maxi[0]


        # ------------- simplefied ------------

        