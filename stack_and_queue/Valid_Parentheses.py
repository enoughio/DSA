class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        open = ['(', '[', '{']


        for item in s :
            if item in open : 
                stack.append(item)
            elif len(stack) > 0 and  stack[-1] == '(' and  item == ')' :
                stack.pop()
            elif len(stack) > 0 and stack[-1] == '[' and  item == ']' :
                stack.pop()
            elif len(stack) > 0 and stack[-1] == '{' and  item == '}' :
                stack.pop()
            else :
                return False

        if len(stack) > 0 : 
            return False

        return True