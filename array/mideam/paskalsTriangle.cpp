#include "bits/stdc++.h"
using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>>ans;

        for(int row = 0; row < numRows; row++)
        {   
            vector<int>current;
            current.push_back(1);
            for(int col = 1; col <= row; col++)
            {
                current.push_back( current[col-1] * ( row - col + 1 )/col );
            }
            ans.push_back(current);
        }
        return ans;
    }
};


// module Solution

        // for(int j = 0; j < numRows; j++)
        // {
        //    vector<int> nums(j+1, 1);

        //     for(int i = 1; i < j; i++)
        //     {
        //         nums[i] = ans[j-1][i] + ans[j-1][i-1];
        //     }
        //     ans.push_back(nums);
        // }
        //     return ans;