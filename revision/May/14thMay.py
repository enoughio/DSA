# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        def getParents(root) : 

            parents =  {}
            q = deque()

            killer = root

            q.append(root)

            while q : 
                n = len(q) 

                for _ in range(n) : 

                    elem = q.popleft()
                    if elem.val == start : 
                        killer = elem

                    if elem.left : 
                        parents[elem.left] =  elem
                        q.append(elem.left)
                    
                    if elem.right : 
                        parents[elem.right] =  elem
                        q.append(elem.right)

            return (parents, killer)

        
        def infect(start, parentof) :
            
            infected = {}
            q = deque()
            minutes = 0

            q.append(start)

            while q : 
                n  = len(q) 

                for _ in range(n) :
                    
                    el = q.popleft()
                    infected[el] = True

                    if el in parentof and parentof[el] not in infected : 
                        q.append(parentof[el])

                    if el.left and el.left not in infected : 
                        q.append(el.left)

                    if el.right and el.right not in infected : 
                        q.append(el.right)
                
                minutes += 1 


            return minutes-1


        data = getParents(root)
        return infect(data[1], data[0])
    

    # ---------------- solved infected binary tree ---------------


    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:        

        def getParents(root) : 

            q = deque()
            q.append(root)
            parentof = {}

            while q : 

                n = len(q)

                for _ in range(n) : 

                    el = q.popleft()

                    if el.left : 
                        parentof[el.left] = el 
                        q.append(el.left)
                    
                    if el.right : 
                        parentof[el.right] = el 
                        q.append(el.right)

            return parentof

        
        def treverse(k, target, parentof) : 

            q = deque()
            ans = []
            visited = { }
            
            d = 0

            q.append(target)

            while d < k : 

                n = len(q)

                for _ in range(n) : 

                    el = q.popleft()
                    visited[el] = True

                    if el in parentof and parentof[el] not in visited : 
                        q.append(parentof[el])
                    
                    if el.left and el.left not in visited : 
                        q.append(el.left)
                    
                    if el.right and el.right not in visited :
                        q.append(el.right)

                d = d+1
                
            while q : 
                elem = q.popleft()
                ans.append(elem.val)
            
            return ans 

        
        if root.left is None  and root.right is None : 
            return []  

        parents = getParents(root)
        print("hter")
        return treverse(k, target, parents)


# -------------- solved all nodes distance k in binary tree ------------- 







