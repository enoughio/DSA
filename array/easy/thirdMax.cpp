#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int thirdMax(vector<int>& nums) {

        int n = nums.size();
        int max = INT_MAX;

        for(int i = 0; i < n; i++)
        {
            if(nums[i] < max)
                max = nums[i];
        }
        int max2 = max, max3 = max;

        for(int i = 0; i < n; i++)
        {
            if(nums[i] > max)
                max = nums[i];
        }

        for(int i = 0; i < n; i++)
        {
            if(nums[i] < max && nums[i] > max2)
                max2 = nums[i];
        }


        for(int i = 0; i < n; i++)
        {
            if(nums[i] < max2 && nums[i] > max3)
                max3 = nums[i];
        }

          return (max3 != max2 ? max3 : max);
            
    }
};