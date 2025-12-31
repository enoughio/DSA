class Node :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def build_tree() : 

    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)

    r1 = root.left
    r2 = root.right

    r1.left.left = Node(5)
    r1.left.right = Node(6)

    r2.right.left = Node(7)
    r2.right.right = Node(8)





def print_bt(root : Node) :
    f