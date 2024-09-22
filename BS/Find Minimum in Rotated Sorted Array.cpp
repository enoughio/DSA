#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {

        int s = 0, e = nums.size() - 1;

        while(s < e)
        {
            // if(nums[mid] < nums[0] && nums[mid] < nums[])
            int mid = s + ( e - s)/2;

            if( nums[mid] >= nums[0] )
                s = mid + 1;
            else 
                e = mid;

            
        }

        return min(nums[s],nums[0]);
    }
};