class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        sm = prices[0]
        pr  = 0

        for cur in prices:

            diff = cur - sm
            
            sm = min(sm, cur)
            pr = max(diff, pr)

        
        return pr