# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # if cnt == k : 
        #     return root
        
        cnt = 0
        ans = root.val

        def find(node) :
            
            nonlocal ans, cnt
            if node is None : 
                return

            find(node.left)
            cnt+=1
            if cnt == k :
                ans = node.val
                return 

            find(node.right)


        find(root)
        return ans  


            
