# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def treverse(node, mini, maxi ) : 

            if not node :
                return True
            
            if  node.val > mini and node.val < maxi : 
                l = treverse(node.left, mini, node.val)
                r = treverse(node.right, node.val, maxi)

                return l and r 
                
                if not l or not r : 
                    return False
                else : 
                    return True

            else : 
                return False

        
        res = treverse(root, float("-inf"), float('inf'))
        return res