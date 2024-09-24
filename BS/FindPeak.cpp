#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {

        int n = nums.size();
        int st = 1;
        int end = n-2, mid = 0;
        // edge cases
        if(n == 1 || nums[0] > nums[1])
            return 0;
        if(nums[n-1] > nums[n-2])
            return n-1;

        while(st <= end)
        {
            mid = (end + st)/2;

            if(mid+1 >=  n || mid -1 < 0)
                break;

            if(nums[mid] > nums[mid+1] && nums[mid] > nums[mid-1] )
                return mid;
            if(nums[mid] > nums[mid+1]  ){
                end = mid - 1;
            }
            else{
                st = mid + 1;
            } 

        }
        return mid;

    }
};
 

// make
 void main() 
 {
    vector<int> x = {2,3,4,5,6,7};
    Solution s;

    cout<< s.findPeakElement(x);

    // return 1;
 }