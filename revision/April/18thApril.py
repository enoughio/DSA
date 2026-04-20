class Solution:
    def combinationSum3(self, limit: int, target: int) -> List[List[int]]:


        def rec(i, arr, rem) : 

            
            if len(arr)  == limit : 
                if rem == 0 :
                    ans.append(arr.copy()) 
                return

            if rem <= 0 : 
                return 

            if len(arr) > limit : 
                return 

            if i >= 10 :
                return 

            if i > rem : 
                return

            rec(i+1, arr + [i], rem - i)
            rec(i+1, arr, rem)

        ans = []
        rec(1, [], target)
        return ans
