class Solution:
    def checkSubsequenceSum(self, N, arr, K):
        
        return self.rec(0, [], 0, arr, K, N)

    def rec(self, sum, nums, i, arr, k, n):
        
        if( i >= n):
            if(sum == k):
                return True
            return False
        if( sum == k ):   
            return True
        
        if (self.rec(sum, nums, i+1, arr, k, n) == True):
            return True
        nums.append(arr[i])
        sum = sum + arr[i]
        
        ans = self.rec(sum, nums, i+1, arr, k, n)
        if (ans == True):
            return True
        else:
            nums.pop()
            return False
        




s = Solution()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
K = 898234
N = len(arr)
print(s.checkSubsequenceSum(N, arr, K))
