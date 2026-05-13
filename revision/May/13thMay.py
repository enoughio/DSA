# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def search(t, node) :

            if node is None : 
                return None
            
            if node == t : 
                return node

            l = search(t, node.left)
            r = search(t, node.right)
            
            if l is not None : 
                return l
            
            return r
        


        def find(i, node) : 

            if node is None : 
                return 

            if i > k : return 

            if i == k : 
                ans.append(node.val)
                return 
            
            print(i)
            
            find(i+1, node.left)
            find(i+1, node.right)


        ans = []
        node = search(target, root)
        find(0, node)

        return ans