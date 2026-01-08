'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of nodes in the Binary Tree.
'''

# Binary tree node class for reference.
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# Functions to traverse on each part.
def traverseBoundary(root):
    # Write your code here.
    
    lt = []
    st = []
    In = []

    def left(node) : 

        if node is None : return
        if not node.left and not node.right : 
          
            return 

        lt.append(node.data)
        if node.left : 
            left(node.left)
        else : 
            left(node.right) 

    def right(node) : 

        if node is None : return 
        if not node.left and not node.right : 
      
            return 
        
        st.append(node.data)
        if node.right :
            right(node.right) 
        else :
            right(node.left)
            
    def Inorder(node) :
        
        if node is None : return
        if not node.left and not node.right : 
            In.append(node.data)
            return 
        
        Inorder(node.left)
        Inorder(node.right)

    ans = []
    ans.append(root.data)
    if root.left : 
        left(root.left)
    if root.right : 
        right(root.right)
    
    Inorder(root)

    
    for i in lt : 
        ans.append(i)
    for k in range(s) :
        ans.append(In[k])

    while st : 
        elem = st.pop()
        ans.append(elem)
    
    return ans


