
# ---------find union of two array----------------

class Solution:
    def findUnion(self, a, b):
        # code here 
               
        i = 0
        j = 0
        
        n = len(a)
        m = len(b)
        
        ans = []
        
        if a[i] < b[j] :
            ans.append(a[i])
            i+=1
        elif a[i] > b[j] : 
            ans.append(b[j])
            j+=1
        else : 
            ans.append(a[i])
            i+=1
            j+=1
            
        while i < n and j < m :
            if a[i] < b[j] : 
                if ans and ans[-1] != a[i] : 
                    ans.append(a[i])
                i+=1
            elif a[i] > b[j] :
                if ans and ans[-1] != b[j] : 
                    ans.append(b[j])
                j+=1
            else : 
                if ans and ans[-1] != b[j] : 
                    ans.append(b[j])
                j+=1
                i+=1
        
        while j < m : 
            if ans and ans[-1] != b[j] : 
                ans.append(b[j])
            j+=1
        
        while i < n :
            if ans and ans[-1] != a[i] : 
                ans.append(a[i])
            i+=1
            
        return ans 
    
# -----------------better approch-----------------------
class Solution:
    def findUnion(self, a, b):
        # code here 
               
        i = 0
        j = 0
        
        n = len(a)
        m = len(b)
        
        ans = []
        

            
        while i < n and j < m :
            
            if i > 0 and a[i-1] == a[i] : 
                i+=1
                continue
            
            if j > 0 and b[j-1] == b[j] :
                j+=1
                continue
            
            
            if a[i] < b[j] :
                ans.append(a[i])
                i+=1
            elif a[i] > b[j] :
                ans.append(b[j])
                j+=1
            else :
                ans.append(b[j])
                j+=1
                i+=1
        
        while j < m :
                
            if j > 0 and b[j-1] == b[j] :
                j+=1
                continue
            
            ans.append(b[j])
            j+=1
        
        while i < n :
            
            if i > 0 and a[i-1] == a[i] : 
                i+=1
                continue
            
            ans.append(a[i])
            i+=1
            
        return ans 
                
            
                
# ---------------------------------------------------------------
