#Infix to Prefix 
# reverse the infix 
# change the brackents
# converted into postfix controlled manner
# the power operatorcan hold the same level of priorty
# other operator can only hold lesser level of priority


class Infix_To_Prefix : 

    def reverse(self, s) : # special reverse function that will also change the brackets
        
        s = list(s)

        i = 0
        j = len(s) - 1

        while ( i <= j ) :

             temp =  s[i]
             s[i] = s[j]
             s[j] = temp
             i +=1
             j -=1

        for i in range(len(s)) :
            if s[i] == '(' : s[i] = ')'
            elif s[i] == ')' :  s[i] = '('

        return ''.join(s)  # Join list into a string

    def priorty(self, i) :
        if i == '^' : return 3
        if i == '*' or i == '/' : return 2
        if i ==  '+' or i == '-' :  return 1
        else : return -1


    def convert(self, s) : 
        
        stack = []
        ans = ''
        s = self.reverse(s)

        for i in s : 

            if ( i >= 'a' and i <= 'z' ) or ( i >= 'A' and i <= 'Z' ) or ( i >= '0' and i <= '9' ) : 
                ans += i
            elif i == '(' :
                stack.append(i)
            elif i == ')' : 
                while stack and stack[-1] != '(' : 
                    ans  += stack[-1]
                    stack.pop()
                if stack : stack.pop()
            else :
                if i == '^' :
                    if stack and self.priorty(stack[-1]) <= self.priorty(i) : 
                        stack.append(i)
                elif stack and self.priorty(stack[-1]) < self.priorty(i) :
                    stack.append(i)
                else : 
                    while stack and self.priorty(stack[-1]) > self.priorty(i) : 
                        ans += stack[-1]
                        stack.pop()
                    stack.append(i)
            
        while stack :
            ans += stack[-1]
            stack.pop()
        
        return ans[::-1]


obj = Infix_To_Prefix()

s = obj.convert('(a+b)*c-d+f')
# s = obj.reverse('(a+b)*c-d+f')
print(s)
