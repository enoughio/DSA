class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        
        // sort array in assending order
        // pick the pair from right side 
        // find min of pair 
        // make a running sum of min of pair
        // return sum since array is sorted the pair that we get is of max value and
        // the sum of their mininim is also maximized by itsel

        int n = nums.size();
        sort(nums.begin(), nums.end());
        int sumMax = 0;

        for(int i = n-1, j = i-1; j >= 0 && i >= 1; j -= 2,  i -= 2){
            sumMax += min(nums[i] , nums[j]);
        }

        return sumMax;
    }
};