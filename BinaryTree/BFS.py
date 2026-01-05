        # my attempt

# import dqueu from queue

# def bfs(root) :

#         ans = []
#         if root == None : return ans

#         q = dqueue()
#         q.append(root)

#         while(len(q) != 0) :
                
#             s = len(q)
#             level = []
#             for i in range(s) :
#                     p = q.popleft()
#                     level.append(p.val)
#                     if p.left !=  None :
#                             q.appen(p.left)
#                     if p.right !=  None :
#                             q.appen(p.right)
            
            
#             ans.append(level)

#         return ans



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        if root is None : return ans

        q = deque()
        q.append(root)

        while( len(q) != 0 ) :
            
            s = len(q)
            level = []

            for _ in range(s) : 

                elem  = q.popleft()
                level.append(elem.val) 

                if elem.left != None : 
                    q.append(elem.left)

                if elem.right != None :
                    q.append(elem.right)

            ans.append(level)

        return ans