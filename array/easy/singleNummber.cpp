// 136. Single Number
// Solved
// Easy
// Topics
// Companies
// Hint
// Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

// You must implement a solution with a linear runtime complexity and use only constant extra space.

 

// Example 1:

// Input: nums = [2,2,1]
// Output: 1
// Example 2:

#include <bits/stdc++.h>
using namespace std;

int singleNumber(vector<int>& nums);

    int singleNumber(vector<int>& nums) {
        
        int sum = nums[0];
        for(int i = 1;  i < nums.size(); i++)
        {
            sum = sum^nums[i];
        }

        return sum;
 
    }



    
int main() {
	// your code goes here
    int t;
    cin>>t;
    
    vector<int>v;
    
    while(t--)
        {
            int n; 
            cin>>n;
            
            for(int i = 0; i < v.size(); i++)
                cout<<v[i];
            cout<<endl;
        }
    
}
