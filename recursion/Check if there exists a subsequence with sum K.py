
class Solution:
    def checkSubsequenceSum(self, N, arr, K):
        

        def rec(sum, i):
        
            if(i == N):
                if(sum == K):
                    return True
                return False
            
            if sum == K : 
                return True
            
            if( rec(sum + arr[i], i+1 ) == True ):
                return True
            return rec(sum, i+1)
            
        
        return rec(0, 0)



s = Solution()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 8
N = len(arr)
print(s.checkSubsequenceSum(N, arr, K))
# Output: True