#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        int ind = -1;

        for(int i = n-2; i >= 0; i-- )
        {
            if(nums[i+1] > nums[i] )
            {
                ind = i;
                break;
            }
        }

        if(ind == -1)
        {
            reverse(nums.begin(), nums.end());
            return;
        }

        for(int i = n-1; i > ind; i--)
        {
            if(nums[i] > nums[ind])
            {
                swap(nums[i], nums[ind]);
                break;
            }
        }

        reverse(nums.begin()+1+ind,nums.end());
    }
};



class Solution {
    public:
        void nextPermutation(vector<int>& nums) {
            
            int n = nums.size();
            int indx = -1;
    
            // find the longest prifix breakpoint
            for( int i = n-2; i >= 0; i--){
    
                if(nums[i] < nums[i+1])
                    indx = i;
                    break;
            }
    
            // if not next permutation
            if(indx == -1){
                reverse(nums.begin(), nums.end());
                return;
            }
    
            // cout<<nums[indx];
            // find the smallest elem in the suffix 
            for(int i = n-1; i > indx; i--){
    
                if(nums[i] > nums[indx]){   // swap it 
                    swap(nums[i], nums[indx]);
                    break;
                }
            }
            
            cout<<indx;
    
            // reverse the array after breakpoint
            // int f = indx + 1;
            // int b = n-1;
    
            reverse(nums.begin()+indx+1, nums.end());
            
            // while( f < b){
            //     swap(nums[f], nums[b]);
            //     f++;
            //     b--;
            // }
    
    
        }
    };