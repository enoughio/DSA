# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if root is None : return ""

        q = deque()
        q.append(root)
        ans = []

        while q : 
            n = len(q)
            
            for _ in range(n) : 
                el = q.popleft()

                if el : 
                    ans.append(el.val)
                else : 
                    ans.append("#")

                if el and el.left :  
                    q.append(el.left)
                elif el :  
                    q.append(None)

                if el and el.right :  
                    q.append(el.right)
                elif el :  
                    q.append(None)
                
            # while ans and ans[-1] is None : 
            #     ans.pop()

        res = ",".join(map(str, ans))
        print(ans)
        return res



    def deserialize(self, st):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        n = len(st)
        token = st.split(',')

        if n == 0: 
            return None

        q = deque()
        i = 1

        root = TreeNode(token[0])
        q.append(root)

        while i < n and q : 

            m = len(q)

            for _ in range(m) : 
                node = q.popleft()
     
                if i >= n : break
                if token[i] == "," : i+= 1 

                if token[i] != "," and token[i] != "#" :      
                    left = TreeNode(int(token[i]))
                    node.left = left
                    q.append(left)
                    i+=1
                elif token[i] == "#" : 
                    node.left = None
                    i+=1
            
                if i >= n : break
                if  token[i] == "," : i+= 1 

                if token[i] != "#" and token[i] != ",":      
                    right = TreeNode(int(token[i]))
                    node.right = right
                    q.append(right)
                    i+=1
                elif token[i] == "#" : 
                    node.right = None 
                    i+=1
                

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# -------------- 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if root is None : return ""

        q = deque()
        q.append(root)
        ans = []

        while q : 
            n = len(q)
            
            for _ in range(n) : 
                el = q.popleft()

                if el : 
                    ans.append(el.val)
                else : 
                    ans.append("#")

                if el and el.left :  
                    q.append(el.left)
                elif el :  
                    q.append(None)

                if el and el.right :  
                    q.append(el.right)
                elif el :  
                    q.append(None)
                
            # while ans and ans[-1] is None : 
            #     ans.pop()

        res = ",".join(map(str, ans))
        return res



    def deserialize(self, st):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if len(st) == 0 : return None

        token = st.split(',')
        n = len(token)
        print(token)

        if n == 0: 
            return None

        q = deque()
        i = 1

        root = TreeNode(token[0])
        q.append(root)

        while i < n and q : 

            m = len(q)

            for _ in range(m) : 
                node = q.popleft()
     
                if i >= n : break
                if token[i] != "#" :      
                    left = TreeNode(int(token[i]))
                    node.left = left
                    q.append(left)
                i+=1
        
            
                if i >= n : break
                if token[i] != "#" :      
                    right = TreeNode(int(token[i]))
                    node.right = right
                    q.append(right)
                i+=1
    
                

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))