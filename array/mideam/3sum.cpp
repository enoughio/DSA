#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        int n = nums.size();
        set<vector<int>>st;

        for(int i = 0; i < n-1; i++)
        {
            set<int> hashset;
            for(int j = i+1; j < n; j++)
            {
                  int third = -(nums[i] + nums[j]);

                if(hashset.find(third) != hashset.end()) 
                {
                    vector<int>sub = {third, nums[j], nums[i]};
                    sort(sub.begin(), sub.end());
                    st.insert(sub);
                }

                hashset.insert(nums[j]);    
            }
        }
        
        vector<vector<int>>ans = {st.begin(), st.end()};
        return ans;
    }
};

// TLE
    //  int n = nums.size();
    //     set<vector<int>>st;

    //     for(int i = 0; i < n-1; i++)
    //     {
    //         set<int> hashset;
    //         for(int j = i+1; j < n; j++)
    //         {
    //               int third = -(nums[i] + nums[j]);

    //             if(hashset.find(third) != hashset.end()) 
    //             {
    //                 vector<int>sub = {third, nums[j], nums[i]};
    //                 sort(sub.begin(), sub.end());
    //                 st.insert(sub);
    //             }

    //             hashset.insert(nums[j]);    
    //         }
    //     }
        
    //     vector<vector<int>>ans = {st.begin(), st.end()};
    //     return ans;

//TLE
    //     for(int i = 0; i < n; i++)
    //     {
    //         mapp[nums[i]]  = i;
    //     }

    //     for(int i = 0; i < n-2; i++)
    //     {
    //         for(int j = i+1; j < n-1; j++)
    //         {
    //             for(int k = j+1; k < n; k++)
    //             {
                    
    //                 if(nums[i] + nums[j] + nums[k] == 0) 
    //                 {
    //                     vector<int>sub = {nums[i], nums[j], nums[k]};
    //                     sort(sub.begin(), sub.end());
    //                     st.insert(sub);
    //                 }
    //             }
    //         }
    //     }
        
    //     vector<vector<int>>ans = {st.begin(), st.end()};
    //     return ans;
    // }










    class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>>ans;

        for(int i = 0; i < n; i++)
        {
            if(i > 0 && nums[i] == nums[i - 1]) continue;

            int j = i+1;
            int k = n-1;

            while(j < k)
            {
                if(nums[i] + nums[j] + nums[k] == 0)
                {
                   vector<int>temp = {nums[i], nums[j], nums[k]};
                   ans.push_back(temp);
                   j++;
                   k--;
                   while(j < k && nums[j] == nums[j-1]) j++;
                   while(k > j && nums[k] == nums[k+1]) k--;

                }
                else if (nums[i] + nums[j] + nums[k] > 0)
                {
                    k--;
                } else 
                    j++;
                
            }
        }

        return ans;

    }
};


// TLE
        // int n = nums.size();
        // set<vector<int>>st;

        // for(int i = 0; i < n-1; i++)
        // {
        //     set<int> hashset;
        //     for(int j = i+1; j < n; j++)
        //     {
        //         int third = -(nums[i] + nums[j]);

        //         if(hashset.find(third) != hashset.end()) 
        //         {
        //             vector<int>sub = {third, nums[j], nums[i]};
        //             sort(sub.begin(), sub.end());
        //             st.insert(sub);
        //         }
                
        //         hashset.insert(nums[j]);
        //     }
        // }
        
        // vector<vector<int>>ans = {st.begin(), st.end()};
        // return ans;

// TLE
    //  int n = nums.size();
    //     set<vector<int>>st;

    //     for(int i = 0; i < n-1; i++)
    //     {
    //         set<int> hashset;
    //         for(int j = i+1; j < n; j++)
    //         {
    //               int third = -(nums[i] + nums[j]);

    //             if(hashset.find(third) != hashset.end()) 
    //             {
    //                 vector<int>sub = {third, nums[j], nums[i]};
    //                 sort(sub.begin(), sub.end());
    //                 st.insert(sub);
    //             }

    //             hashset.insert(nums[j]);    
    //         }
    //     }
        
    //     vector<vector<int>>ans = {st.begin(), st.end()};
    //     return ans;

//TLE
    //     for(int i = 0; i < n; i++)
    //     {
    //         mapp[nums[i]]  = i;
    //     }

    //     for(int i = 0; i < n-2; i++)
    //     {
    //         for(int j = i+1; j < n-1; j++)
    //         {
    //             for(int k = j+1; k < n; k++)
    //             {
                    
    //                 if(nums[i] + nums[j] + nums[k] == 0) 
    //                 {
    //                     vector<int>sub = {nums[i], nums[j], nums[k]};
    //                     sort(sub.begin(), sub.end());
    //                     st.insert(sub);
    //                 }
    //             }
    //         }
    //     }
        
    //     vector<vector<int>>ans = {st.begin(), st.end()};
    //     return ans;
    // }