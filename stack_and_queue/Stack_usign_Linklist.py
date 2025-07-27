
class Node () :
    def __init__(self, value):
        self.data = value
        self.next = None


class St () : 
    
    def __init__(self):
      self.top = None
      self.qsize = 0

    def push(self, val) :

        node = Node(val)
        node.next = self.top
        self.top = node

        self.qsize += 1
        
    
    def pop(self) :
        rem = self.top

        if self.top == None : 
            print("Stack underflow")
            return None
        
        self.top = self.top.next
        self.qsize -= 1
        return rem.data
    
    def size(self) : 
        return self.qsize
    

    def Top(self) : 
        if self.top == None :
            return None

        return self.top.data


s = St()

s.push(3)
s.push(4)
print(s.Top())  #4
print(s.pop()) #4
print(s.Top())  #3
s.push(5)
print(s.size()) #2