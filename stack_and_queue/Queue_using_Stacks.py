class MyQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []
        

    def push(self, x: int) -> None:
        size = len(self.st1)
        prevItem = []
        for _ in range(len(self.st1)) :
            prevItem.append(self.st1.pop())
        self.st1.append(x)
        
        for i in range(len(prevItem) -1 , -1, -1) : 
            self.st1.append(prevItem[i])

    def pop(self) -> int:
        val = self.st1.pop()
        return val
        

    def peek(self) -> int:
        if not self.empty() : 
            return self.st1[-1]
        else : 
            print('Stack Underflow')
            return None


    def empty(self) -> bool:
        return len(self.st1) == 0  


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(7)
print(obj.pop())
obj.push(4)
print( "peek is :", obj.peek())
print(obj.empty())