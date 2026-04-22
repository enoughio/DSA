# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def rec(root) : 

            if not root :
                return

            ans.append(root.val)
            rec(root.left)
            rec(root.right)
        
        ans = []
        rec(root)
        return ans


# -----------inorder------------

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def rec(root) : 

            if not root :
                return

            rec(root.left)
            ans.append(root.val)
            rec(root.right)
        
        ans = []
        rec(root)
        return ans


# ---------- postOrder ---------

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def rec(root) : 

            if not root :
                return

            rec(root.left)
            rec(root.right)
            ans.append(root.val)
        
        ans = []
        rec(root)
        return ans
