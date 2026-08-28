class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        el = prices[-1]
        cnt = 0

        for i in range(n-1, -1, -1) : 
            if prices[i] < el : 
                cnt += (el - prices[i]) 
                el = prices[i]
            else : 
                el = prices[i]
        
        return cnt