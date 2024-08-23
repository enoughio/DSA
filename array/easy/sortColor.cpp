#include <bits/stdc++.h>
using namespace std;


   void sortColors(vector<int>& nums) {
           int n = nums.size();

           int mid = 0, left = 0, right = nums.size()-1;

           while(mid <= right)
           {
                if(nums[mid] == 0)
                {
                    swap(nums[mid], nums[left]);
                    left++;
                    mid++;
                }
                else if(nums[mid] == 1){
                    mid++;
                }
                else {
                    swap(nums[right], nums[mid]);
                    right--;
                }
           }

    }