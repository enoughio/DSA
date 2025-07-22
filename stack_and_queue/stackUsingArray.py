
# stack using array
class StackImpl () :  

    def __init__(self):
        self.top = -1
        self.stack = []


    def topElem(self) :
        if self.top == -1 :
            return -1
        return self.stack[self.top]
    
    
    def push(self, n) : 
        self.top += 1
        self.stack.append(n)
        return self.stack[self.top]
    
    
    def pop(self) :
        if self.top == -1 :
            return None
        self.top -= 1
        return self.stack[self.top+1]
    

    def size(self) :
        return self.top + 1
    

s = StackImpl()
s.push(10)
s.push(20)
print(s.topElem())  # 20
print(s.pop())         # 20
print(s.topElem())  # 20
print(s.size())        # 1


s2 = StackImpl()
print(f'this is s2 {s2.topElem()}')