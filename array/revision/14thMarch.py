


# -------------- Brute Force ------------

class Solution:
    def romanToInt(self, s: str) -> int:
        
        def val(c) : 
            if c == "I" :
                return 1
            elif c == 'V' : 
                return 5
            elif c == 'X' : 
                return 10
            if c == 'L' :
                return 50
            if c == "C" : 
                return 100
            if c == "D" : 
                return 500
            if c == "M" : 
                return 1000
        
        i = 0 
        num = 0
        n = len(s)
        
        while i < n : 

            if i + 1 < n and s[i] == "I" and s[i+1] == 'V' :
                num += 4
                i+=1
            elif i + 1 < n and s[i] == "I" and s[i+1] == 'X' :
                num += 9
                i+=1
            elif i + 1 < n and s[i] == "X" and s[i+1] == 'L' :
                num += 40
                i+=1
            elif i + 1 < n and s[i] == "X" and s[i+1] == 'C' :
                num += 90
                i+=1
            elif i + 1 < n and s[i] == "C" and s[i+1] == 'D' :
                num += 400
                i+=1
            elif i + 1 < n and s[i] == "C" and s[i+1] == 'M' :
                num += 900
                i+=1
            else : 
                num += val(s[i])
            
            i+=1
            
        return num




# ------------------- Much better solution -----------------


class Solution:
    def romanToInt(self, s: str) -> int:
        
        val = {
            "I" : 1 ,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        total = 0
        pre_value = 0
        
        for i in reversed(s):
            value = val.get(i, 0)

            if value < pre_value:
                total -= value
            else:
                total += value

            pre_value = value

        return total


