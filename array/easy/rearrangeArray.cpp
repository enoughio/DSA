class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {

        int n = nums.size();
        vector<int>ans(n);

        int p = 0, N = 1;
        for(int i = 0; i < n; i++)
        {

            if(nums[i] >= 0 )
            {
                ans[p] = nums[i];
                p = p+2;
            } else {
                ans[N] = nums[i];
                N = N+2;
            }
        }

        return ans;

    }