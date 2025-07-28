from collections import deque


class Stack :

    def __init__(self):
        self.queue = deque()

    def push(self, val) :
        self.queue.append(val)
        for _ in range( len(self.queue) -1) : 
            self.queue.append(self.queue.popleft())

    def pop(self) : 
        if not self.is_empty() :
            return self.queue.popleft()
        else :
            print("Stack Underflow")
            return None  

    def is_empty(self) : 
        return len(self.queue) == 0

    def Size(self) :
        return len(self.queue)

    def top(self) :
        if not self.is_empty() :
            return self.queue[0]
        else : 
            return None
        
    def Print_st(self) :
        # print("stack top to bottom", list(self.queue))
        print("Stack (top → bottom):")
        for item in self.queue:
            print(item)




st = Stack()

st.push(4)
print(st.top())
st.push(5)
st.push(6)
st.push(7)
print(st.pop())
print()
st.Print_st()