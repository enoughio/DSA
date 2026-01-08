
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None : 
            return ans 
        
        q = deque()
        q.append(root)
        flag = False

        while q : 

            s =  len(q)
            level = [0]*s

            for i in range(s) : 

                node = q.popleft()

                if flag :
                    idx = s - i - 1
                    level[idx] = node.val
                else : 
                    level[i] = node.val
                
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)


  
            ans.append(level)
            flag = not flag 

        return ans

