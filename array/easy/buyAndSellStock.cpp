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