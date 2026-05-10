# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        q = deque()
        q.append(root)
        
        maxi = 1

        while q :
            n = len(q)
            level = []

            for i in range(n) : 

                node = q.popleft()


                l = new Node(float("-inf"))
                if node.left : 
                    l = node.left
                
                r = new Node(float("-inf"))
                if node.right : 
                    r = node.right

                if level and l is none : 
                    level.append(l)
                elif l is not None :
                    level.append(l)

                if level and r is none : 
                    level.append(r)
                if r is not none : 
                    level.append(r)
                
            while level and level[-1].val == float("-inf") : 
                level.pop()  

            maxi = max( len(level), maxi )
