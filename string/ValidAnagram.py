class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)):
            return False

        m1 = {}
        
        for i in s :
            if(i in m1):
                m1[i]+=1
            else:
                m1[i] = 1
        
        for i in t:
            if i in m1 and m1[i] > 0:
                m1[i]-=1
            else: 
                return False

        return True
    


#  print(m1[ ord(i) - ord('a') ])

#  more optimized solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)):
            return False

        m1 = [0]*26
        
        for i in s :
            m1[ ord(i) - ord('a') ] += 1
           
        for i in t:
            if m1[ ord(i) - ord('a') ] > 0:
                m1[ ord(i) - ord('a') ]-=1
            else: 
                return False

        return True