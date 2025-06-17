class Solution:
    def generateBinaryStrings(self, n):
        # Code here
        ans = []
        
        # def rec(arr, i):
        #     if i == n:
        #         ans.append(arr.copy())
        #         # print(arr.copy())
        #         return 
    
    
        #     # arr.append(0)  #left
        #     arr = arr + '0'
        #     rec(arr, i+1)
        #     arr.pop()
            
        #     if(i == 0 or arr[i-1] != 1):
        #         # arr.append(1)
        #         arr = arr = '1'
        #         rec(arr, i+1)
        #         arr.pop()
        
        def rec(s, i):
            if i == n:
                ans.append(s)
                return 
            
            rec(s + '0', i + 1)
            
            if i == 0 or s[-1] != '1':
                rec(s + '1', i + 1)
        
        rec("", 0)
        return ans      