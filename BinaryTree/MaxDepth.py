# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def fn(root, cnt) : 

            if root is None : 
                return cnt

            cnt +=1
            l = fn(root.left, cnt)
            r = fn(root.right, cnt)

            return max(l, r)

        return fn(root, 0)


# ------------ using BFS ---------

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        level = 0

        if root is None : return level
        q = deque()
        q.append(root)

        while(q) :

            s = len(q)

            for _ in range(s) :
                e = q.popleft()
                
                if e.left :
                    q.append(e.left)
                if e.right : 
                    q.append(e.right)
                
            level += 1

        return level




