class Solution {
public:
    int countPairs(vector<int>& nums, int target) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        
        int st = 0;
        int end  = n-1;
        int mid;
        int cnt = 0;

        while(st < end){

            if(( nums[st]+nums[end] ) < target) {
                cnt= cnt + end - st;
                st++;
            } else {
                end--;
            }
        }

        return cnt;
    }
};



    // brute

        // int n = nums.size();
        // int cnt = 0;
        // for(int i = 0; i < n; i++){

            
        //     for(int j = i+1; j < n; j++){

        //         if((nums[i] + nums[j]) < target ) cnt++;
        //     }
        // }
        // return cnt;