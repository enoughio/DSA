class Solution:
    def maxLength(self, arr):
        # code here
        
        mp = {}
        sum = 0
        maxi = 0
        
        for idx, i in enumerate(arr) :
            
            sum += i
            
            if sum == 0 :
                maxi = idx + 1
            else :
                if sum in mp : 
                    maxi = max(maxi, idx - mp[sum])
                else : 
                    mp[sum] = idx
                    
        
        return maxi