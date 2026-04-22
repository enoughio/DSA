# Definition for a binary tree node.


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        q.append(root)

        if root is None :
            return []

        ans  = []

        while( q ) : 

            rg = len(q) # number of current level element 
            level = [] # store level children

            for i in range(rg) : 
          
                elem = q.popleft()
                level.append(elem.val)
                
                if elem.left : 
                    q.append(elem.left)

                if elem.right : 
                    q.append(elem.right)
                
            ans.append(level)

        return ans
    

# ---- iterative preOrder treversal of tree ---------------

    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        st = [] 

        if root is None  : 
            return []
        
        st.append(root)

        while st : 
            el = st.pop()
            
            if el.right : 
                st.append(el.right)
            
            if el.left : 
                st.append(el.left)

            ans.append(el.val)

        return ans




# ---------- iterative inorder tree treversal -----------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        st = []
        node = root

        while True : 

            if node is not None : 
                st.append(node)
                node = node.left
            else : 
                if not st : 
                    break 

                el = st.pop()
                ans.append(el.val)
                node = el.right

        return ans

