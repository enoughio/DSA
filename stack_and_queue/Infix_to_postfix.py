#infix to postfix

class InfTopost : 

    def __init__(self):
        self.ans = ''
        self.stack  = []

    def priorty(self, i) :
        if i == '^' : return 3
        if i == '*' or i == '/' : return 2
        if i ==  '+' or i == '-' :  return 1
        else : return -1

    def converter(self, s) : 
        
        for i in s : 

            if ( i >= 'a' and i <= 'z' ) or ( i >= 'A' and i <= 'Z' ) or ( i >= '0' and i <= '9' ) : 
                self.ans += i
            elif ( i == '(' ) : 
                self.stack.append(i)
            elif i == ')' :
                while ( self.stack  and self.stack[-1] != '(' ) : 
                    self.ans += self.stack[-1]
                    self.stack.pop()

                if self.stack :  self.stack.pop()

            elif  self.stack and self.priorty(self.stack[-1]) < self.priorty(i) : 
                self.stack.append(i)
            else : 
                while self.stack and  self.priorty(self.stack[-1]) >= self.priorty(i) :
                    self.ans += self.stack[-1]
                    self.stack.pop()
                self.stack.append(i)

        while len(self.stack) != 0 : 
            self.ans += self.stack.pop()
            
        return self.ans 

obj = InfTopost()
print(obj.converter('a+b*(c^d-e)'))