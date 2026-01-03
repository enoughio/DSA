# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []        
        def dfs(root) : 

            if root == None : 
                return
            
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ans





# ------------------


class Solution:

    def dfs(self, root, ans) : 

        if root == None : 
            return
        
        ans.append(root.val)
        self.dfs(root.left, ans)
        self.dfs(root.right, ans)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []        
        self.dfs(root, ans)

        return ans

