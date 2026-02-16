# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # if cnt == k : 
        #     return node
        
        ans = root.val

        def find(node, k) :
            
            nonlocal ans, cnt
            if node is None : 
                return

            find(node.left, k)
            cnt+=1
            if cnt == k :
                ans = node.val
                return 

            find(node.right, k)
        cnt = 0
        find(root, k)
        return ans  

