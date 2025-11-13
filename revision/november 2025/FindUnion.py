class Solution:
    def findUnion(self, a, b):
        # code here
        
        i, j = 0, 0
        n, m = len(a), len(b)  # lengths
        
        ans = []
        
        if a[i] < b[j] :
            ans.append(a[i])
            i+=1
        else : 
            ans.append(b[j])
            j+=1
        
        while i < n and j < m : 
            
            if a[i] < b[j] : 
                if(a[i] != ans[-1]): 
                    ans.append(a[i])
                i+=1
            elif a[i] > b[j] : 
                if b[j] != ans[-1] : 
                    ans.append(b[j])
                j+=1
            else : 
                if a[i] != ans[-1] : 
                    ans.append(a[i])
                i+=1
        
        
        while(j < m):
            if ans  and  b[j] == ans[-1] : 
                j+=1    
                continue
            ans.append(b[j])
            j+=1
            
        while(i < n): 
            if ans  and  a[i] == ans[-1] : 
                i+=1
                continue
            ans.append(a[i])
            i+=1
        
        
        return ans