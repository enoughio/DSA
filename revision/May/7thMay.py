# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        self.mp = {  }
        self.maxl = 0 
        self.maxR = 0 

        def rec(node, row, col) : 

            if node is None : 
                return 

            if col not in self.mp : 
                self.mp[col] = []

            self.mp[col].append((node.val, row)) 
        
            rec(node.left, row+1, col-1)
            self.maxl = min(self.maxl, col)

            rec(node.right, row+1, col+1)
            self.maxR = max(self.maxR, col)
        
        ans = []
        rec(root, 0, 0)


        for i in range(self.maxl, self.maxR+1, 1) : 

            if i in self.mp : 
                self.mp[i].sort( key=lambda x : (x[1], x[0]) )

                res = []
                for i, j in self.mp[i] : 
                    res.append(i) 
                
                ans.append(res)
                
        return ans 


# ----------------------- binary tree right side view -------------- 

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        if root is None : 
            return []

        q = deque()
        q.append(root)

        elems = []

        while q : 

            level = []
            for i in range( len(q) ) : 
                
                node = q.popleft()
                level.append(node.val)  
                
                if node.left  : 
                    q.append(node.left)

                if node.right :
                    q.append(node.right)

            elems.append(level)

        ans = []
        for i in elems : 
            ans.append(i[-1])
        
        return ans
    

