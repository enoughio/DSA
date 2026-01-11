# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = deque()  # (node, col)
        q.append((root, 0,0)) 
        
        min_col, max_col = 0, 0
        cols = defaultdict(list)


        while q :
            s = len(q)
            
            for _ in range(s) :

                node, col, row = q.popleft()
                min_col, max_col = min(min_col, col), max(max_col, col)

                cols[col].append((row, node.val))
                
                
                if node.left :
                     q.append((node.left, col -1, row+1))
                if node.right :
                     q.append((node.right, col +1, row+1))

        ans = []
        for c in range(min_col, max_col + 1) :

            Ucol = cols[c]
            Ucol.sort( key=lambda x : (x[0], x[1]) )

            col = []
            for _, val in Ucol :
                col.append(val)

            ans.append(col)

        return ans
