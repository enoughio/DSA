class Solution:
    def longestSubarray(self, arr, k):  
        maxi = 0
        total_sum = 0
        n = len(arr)
        mapp = {}
        
        for i in range(n):
            total_sum += arr[i]
            
            if total_sum == k:
                maxi = i + 1
            
            if total_sum not in mapp:
                mapp[total_sum] = i
                
            if (total_sum - k) in mapp:
                maxi = max(i - mapp[total_sum - k], maxi)
                
        return maxi


# Runner function to test
def main():
    obj = Solution()
    arr = [1, 2, 4, 5, 3, 0,4,5,3,5,3,5,2,45,2,4,22,214,7,23,54,2,4,2335,3,3,3,5,2,2,3,2]
    k = 20
    print("Longest Subarray Length:", obj.longestSubarray(arr, k))

# Run the function
if __name__ == "__main__":
    main()
