#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void recursion(vector<int>& nums,vector<vector<int>> & ans, int index)
    {
        if(index >= nums.size())
        {
            ans.push_back(nums);
            return;
        }

        for(int i = index; i < nums.size(); i++)
        {
            swap(nums[index], nums[i]);
            recursion(nums, ans, index+1);
            swap(nums[i], nums[index]);
        }

    }

    vector<vector<int>> permute(vector<int>& nums) {
        
        vector<vector<int>> ans;
        int index = 0;
        recursion( nums, ans, index);
        return ans;
    }
};