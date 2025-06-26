class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        nums.sort()
        
        def rec(arr, i):

            if i == len(nums) : 
                tup = tuple(arr)
                ans.add(tup)
                return 
            
            rec(arr + [nums[i]] , i+1)
            rec(arr, i+1)


        rec([], 0)
        return list(ans)
    

# =============================
# optimized

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()
        n = len(nums)
        
        def rec(arr, i):

            # if i == 0 : 
            #     ans.append([])

            if i == n : 
                ans.append(arr)
                return 

            ans.append(arr)
            
            for j in range(i, n) :

                if j > i and nums[j] == nums[j-1] :
                    continue 

                rec(arr + [nums[j]] , j+1)


        rec([], 0)
        return list(ans)
    
