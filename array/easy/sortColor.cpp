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


/* python */

        def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        lis = [0]*3 

        for i in nums:
            lis[i] += 1

        j = 0
        for i in range(3):
            while(lis[i] > 0):
                nums[j] = i
                lis[i] -= 1
                j += 1   