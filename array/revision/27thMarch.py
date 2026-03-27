    class Solution:
        def combinationSum3(self, k: int, n: int) -> List[List[int]]:
            
        
            def fn (dig, i, arr, r ) :  

                if r == 0 and dig != k : 
                    return

                if dig >= k and r == 0 : 
                    ans.append(arr.copy())
                    return

                if i >= 10 :
                    return

                fn(dig+1, i+1, arr+[i], r-i)
                fn(dig, i+1, arr, r)
            
            ans = []
            fn(0, 1, [], n)

            return ans
        




    # ------------subsets---------

    class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)

        def fun(i, arr) :

            ans.append(arr.copy())

            for j in range(i, n) :
                arr.append(nums[j ])
                fun(j+1, arr)
                arr.pop()


        ans = []
        fun(0, [])
        return ans