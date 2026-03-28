class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        def rec(i, arr) : 


            if i > n : 
                # ans.append(arr.copy())
                return 

            ans.append(arr.copy())
            
            
            for j in range(i, n) : 
                
                if j > i and nums[j-1] == nums[j]: 
                    continue

                arr.append(nums[j])
                rec(j+1, arr)
                arr.pop()
            

        ans = []
        rec(0, [])
        return ans


        