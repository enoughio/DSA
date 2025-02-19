#include <bits/stdc++.h>





    // avg case O(logN)
    // at wotst case O(N)
    bool search(vector<int>& nums, int target) {
        
        int n = nums.size();
        int st = 0;
        int end = n-1;

        while(st <= end)
        {
            int mid = (end + st)/2;
            //breaking conditis is nums[st] == nums[mid] and nums[mid] == nums[end]

            if(target == nums[mid])
                return true;
            if(nums[st] == nums[mid]) st++;   // if found any  break condition then simpl move (avoid)
            else if(nums[mid] == nums[end]) end--;
            
            else if(nums[st] <= nums[mid]) {

                if(target >= nums[st] && target <= nums[mid])
                {
                    end = mid-1;
                }else {
                    st = mid + 1;
                }

            } else {

                if(target >= nums[mid] && target <= nums[end])
                {
                    st = mid+1;
                }else {
                    end = mid - 1;
                }

            }
        }
        return false;

    }

/*
    bool searchRotated(vector<int>&nums, int t){

        int s = 0, n = nums.size(), e = n-1;

        if (n == 1 && nums[n - 1] != t)
            return false;

        while (s <= e) {
            int mid = (s + e) / 2;

            if (nums[mid] == t) {
                return true;
            } else if (nums[mid] < nums[e]) {
                if (t > nums[mid] && t <= nums[e]) {
                    s = mid + 1;
                } else {
                    e = mid - 1;
                }
            } else if (nums[mid] > nums[e]) {
                if (t < nums[mid] && t >= nums[s]) {
                    e = mid - 1;
                } else {
                    s = mid + 1;
                }
            }else if (nums[mid] == nums[e])
                e--;
        }
        return false;



    }


    */