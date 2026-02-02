# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def find(node, val) : 
            if not node : 
                return None

            if node.val == val : 
                return node
            elif node.val < val : 
                return find(node.right, val)
            else  : 
                return find(node.left, val)

            return None
        
        # ans  = []
        # def cal(node, ans) : 
        #     if not node : 
        #         return 

        #     ans.append(node.val)
        #     cal(node.left, ans) 
        #     cal(node.right, ans) 

        return find(root, val)
        # cal(node,ans)

        return ans