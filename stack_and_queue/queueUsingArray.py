#queue implementiaion using array
class QueueImpl() : 

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [0] * capacity
        self.qSize = 0
        self.start = -1
        self.end = -1

    def push(self, n) : 

        if (self.end + 1) % self.capacity == self.start:
            print("Queue Overflow")
            return

        if self.start == -1 : 
            self.start  += 1
            self.end = self.start 
        else : 
            self.end = ( self.end + 1 ) % self.capacity

        self.queue[self.end] = n
        self.qSize += 1
        return
    
    
    def pop(self) :

        if (self.start == -1) : 
            print('stack underFlow')
            return
        
        popped_value = self.queue[self.start]
        
        if self.end == self.start : 
            self.start = - 1
            self.end =  - 1
        else :
            self.start = (self.start + 1 ) % self.capacity

        self.qSize -= 1 
        return popped_value


    def size(self): 
        return self.qSize
    

    def front(self):
        if self.start == -1:
            return None
        return self.queue[self.start]



q = QueueImpl(4)

q.push(4)
q.push(3)
print('Size is:', q.size())  # 2
q.pop()
q.push(2)
print('Size is:', q.size())  # 2
print('Front element is:', q.front())  # 3

