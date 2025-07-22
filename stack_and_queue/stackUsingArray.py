
# stack using array
class StackImpl () :  

    def __init__(self, capacity):
        self.top = -1
        self.capacity =  capacity
        self.stack = [0] * capacity


    def topElem(self) :
        if self.top == -1 :
            return None
        return self.stack[self.top]
    
    
    def push(self, n) :
        if( self.top >= self.capacity - 1 ):
            print("Overflow") 
            return None
        
        self.top += 1
        self.stack[self.top] = n
        return n
    
    
    def pop(self) :

        if self.top <= -1 :
            print("Underflow")
            return None
        
        self.top -= 1
        return self.stack[self.top+1]
    

    def size(self) :
        return self.top + 1
    
    def is_full(self) : 
        return self.top == self.capacity -1 

    def is_empty(self) : 
        return self.top == -1
    

s = StackImpl(5)

s.push(10)
s.push(20)
print(f'{s.topElem()}')    # 20
s.push(30)

print(s.pop())     # 30
print(s.size())    # 2

s.push(40)
s.push(50)
s.push(60)
s.push(70)         # Should print "Stack Overflow"
