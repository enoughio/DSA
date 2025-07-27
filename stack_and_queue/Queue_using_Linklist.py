

class Node () :
    def __init__(self, value):
        self.data = value
        self.next = None


class Queue() : 
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def push(self, val) :

        node = Node(val)
        if self.start == None :
            self.start = node
            self.end = node
        else : 
            self.end = node
        
        self.size += 1
        return
    
    def pop(self) : 

        if self.start == None :  
            print("Queue Underflow")
            return None
    
        rem = self.start
        self.start = self.start.next
        rem.next = None
        data = rem.data

        self.size -= 1
        return data
    
    def Size(self) :
        return self.size()
    
    def top(self) :
        if self.end == None :
            return None
        return self.end.data
    


q = Queue()
q.push(3)
print(q.top())

q.push(4) 
q.push(3)
print(q.pop()) # 3
q.push(33) 
print(q.top()) # 33
q.pop()
q.push(2) 
q.pop()
q.push(1) 
q.pop()
print(q.top())