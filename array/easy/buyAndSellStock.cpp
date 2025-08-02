#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int buy = 0;  //   these only stores indexes
        int sell = 0;
        int cBuy = 0;
        int maxProfit = 0;
    
    for(int i = 1; i < prices.size(); i++)
    {
        maxProfit = prices[sell] - prices[buy];

        if(prices[i] < prices[buy])
        {
            cBuy = i;
        }

        if(prices[sell] - prices[cBuy] > maxProfit ){
            buy = cBuy;
            sell = cBuy;
        }

        else if ( prices[i] > prices[buy] && i > buy )
        {
            if(prices[i] > prices[sell])
                sell = i;
        }
    }
            buy = cBuy;
            return prices[sell] - prices[buy];
    }
};





// non working brute 

// class Solution {
// public:
//     int maxProfit(vector<int>& prices) {
        
//         int buy = 0;  //   these only stores indexes
//         int sell = 0;
//         int cBuy = 0;
//         int maxProfit = 0;
    
//     for(int i = 1; i < prices.size(); i++)
//     {
//         maxProfit = prices[sell] - prices[buy];

//         if(prices[i] < prices[buy])
//         {
//             cBuy = i;
//         }

//         if(prices[sell] - prices[cBuy] > maxProfit ){
//             buy = cBuy;
//             sell = cBuy;
//         }

//         else if ( prices[i] > prices[buy] && i > buy )
//         {
//             if(prices[i] > prices[sell])
//                 sell = i;
//         }
//     }
//             buy = cBuy;
//             return prices[sell] - prices[buy];
//     }
// };






/// inital brute 
        // int minimum = prices[0];
        // int maxPr = 0;

        // for(int i = 1; i < prices.size(); i++)
        // {
        //     int cost = prices[0] - minimum;
        //     maxPr = max(maxPr, prices[i]);
        //     minimum = min(prices[i], minimum);

        // }
          
        //   return maxPr-minimum;




// TLE
        // int n = nums.size();
        // int maxi = 0;

        // for( int i = 0; i < n; i++){
        //     for(int j = i+1; j < n; j++){
        //         if(nums[j] > nums[i]){
        //             maxi = max(nums[j] - nums[i], maxi);
        //         }
        //     }
        // }

        // return maxi;




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        mini = prices[0]

        for i in range( len(prices) ) : 
            prof =  prices[i] - mini

            if prof > maxP and prof > 0 : 
                maxP = prof

            if prices[i] < mini : 
                mini = prices[i]
            
        return maxP
        

// two pointer approach
// Best Time to Buy and Sell Stock
//  def maxProfit(self, prices: List[int]) -> int:
//         high=prices[0]
//         low=prices[0]
//         profit=0
//         for price in prices:
//             if (price>low):
//                 high=price
//                 profit=max(profit,high-low)
//             else:  
//                 low = price
//             high =  price 
            
//         return profit