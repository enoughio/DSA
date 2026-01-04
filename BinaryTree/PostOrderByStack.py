
# ---------------- two stack 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans =[]
        if root == None : return ans

        st = []
        st2 = []

        st.append(root)

        while len(st) != 0 :
            elem = st.pop()
            st2.append(elem.val)
            if elem.left  : st.append(elem.left ) 
            if elem.right : st.append(elem.right ) 
            
        while len(st2) != 0 :
            e = st2.pop()
            ans.append(e)

        return ans
        

# --------------- 