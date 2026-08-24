        

def en(s) : 
    n = len(s)

    i = 1
    ch = s[0]
    cnt = 1
    while i < n : 
        if s[i] == ch : 
            cnt +=1
        else : 
            if cnt == 1 : 
                ans = ch + ans 
            else : 
                ans = f"{cnt}[{ch}]" + ans
            ch = s[i]
            cnt = 1
    return ans 


print(en("hello"))



# ------------------- 

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        
        for st in strs : 
            n = len(st)
            encoded = encoded + f"{n}#{st}"
        
        return encoded


    def decode(self, s: str) -> List[str]:
        
        print(s)
        n = len(s)
        i = 0
        ans = []

        while i < n :
            
            cnt = ''
            while s and s[i] != '#' : 
                cnt = cnt + s[i]
                i+=1
            
            i+=1
            cnt = int(cnt)

            block = ""
            for c in range(cnt) : 
                block =  block + s[i]
                i+=1
            
            ans.append(block)

        return ans




