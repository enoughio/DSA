#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int sum = 0;
        int maxSum = nums[0];

        for(int i = 0; i < nums.size(); i++)
        {
            sum += nums[i];

            if(sum > maxSum)
                maxSum = sum;

            if(sum < 0)
                sum = 0;
            
        }

        return maxSum;
    }
};

// using Kadane's Algo

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadans algorithum 

        sum =  0
        maxi = float('-inf')

        for i in nums :

            sum += i

            if sum > maxi : 
                maxi  = sum 
            
            if sum < 0 :
                sum =  0

        return maxi




   // sassta soln

        // int maxSum = nums[0];
        // int n = nums.size();

        // for(int i = 0; i < n; i++)
        // {
        //     int sum = 0;
        //     for(int j = i; j < n; j++)
        //     {   
        //         sum += nums[j];
        //     }
        //         maxSum = max(sum, maxSum);
        // }

        // return maxSum;