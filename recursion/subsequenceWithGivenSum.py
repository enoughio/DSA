class Solution:
    def checkSubsequenceSum(self, N, arr, K):
        
        return self.rec(0, [], 0, arr, K, N)

    def rec(self, sum, nums, i, arr, k, n):
        
        if( i >= n):
            if(sum == k):
                print(nums)
                return True
            return False
        if( sum == k ):   
            print(nums)
            return True
        
        if (self.rec(sum, nums, i+1, arr, k, n) == True):
            return True
        nums.append(arr[i])
        sum = sum + arr[i]
        
        if (self.rec(sum, nums, i+1, arr, k, n) == True):
            return True
        else:
            nums.pop()
            return False

s = Solution()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
K = 3
N = len(arr)
print(s.checkSubsequenceSum(N, arr, K))
