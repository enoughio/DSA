class Solution:
    def isValid(self, s: str) -> bool:
        
        def calOpen(ch) : 

            if ch == ")" :
                return "("
            elif ch == "]" : 
                return "["
            else : 
                return "{"
         
        st = []  # stack
        for ch in s : 
            
            if ch in ["(", "[", "{"] :
                st.append(ch)

            else  :   # closing bracket   
                cl = calOpen(ch)
                
                if st and st[-1] == cl : 
                        st.pop() 
                else : 
                    return False 

                

        if st : return False
        return True
    

    # ------- implemented min Stack -------------

class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        
        p = ()  # val, mini
        if self.st :
            p = ( val, min(val, self.st[-1][1]) )
        else : 
            p = (val, val)

        self.st.append(p)
        print(p)

    def pop(self) -> None:
        p = self.st.pop()
        print(p[0])  

    def top(self) -> int:
        if self.st :
            return self.st[-1][0]
        else : 
            return None
            
    def getMin(self) -> int:
        if self.st : 
            return self.st[-1][1]
        else : 
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()