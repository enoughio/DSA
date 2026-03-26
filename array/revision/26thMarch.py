class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        ans = []
        n = len(candidates)

        if n == 1 and ( target == candidates[0] ) : 
            return [candidates]

        if candidates[-1] == candidates[0] and target == (n * candidates[0] ): 
            return [candidates]

        def rec(idx, arr, t ) : 
            
            # means we have found a pair
            if t == 0 :
                ans.append(arr) 
                return        

            if t < 0 :
                print("run")
                return

            for i in range(idx, n) : 

                # just take the first occorance and skip duplicates 
                if i > idx and candidates[i] == candidates[i-1] : 
                    continue
                
                # if the current elem is greater then the target
                if candidates[i] > t : 
                    break
                
                rec(i+1, arr+[candidates[i]], t - candidates[i])

        rec(0, [], target)

        return ans

    