#include<bits/stdc++.h>
using namespace std;

    int singleNonDuplicate(vector<int>& nums) {

        int n = nums.size();
        int st = 0, end = n-1;
        int mid = 0;

        while(st <= end)
        {
            mid = (end + st)/2;
            if(mid+1 >= n || mid -1 < 0) {
                break;
            }

            if(nums[mid] != nums[mid+1] && nums[mid] != nums[mid-1]){
                return nums[mid];
            }

            if(nums[mid] == nums[mid+1])
            {
                if((mid+2)%2 == 0){
                    st = mid +2;
                } else {
                    end = mid -1;
                }
            } else {

                if((mid+1)%2 == 0){
                    st = mid + 1;
                } else {
                    end = mid -2;
                }
            }

        }
            cout<<"here";
            return nums[mid];
    }
