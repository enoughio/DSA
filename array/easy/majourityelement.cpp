#include <bits/stdc++.h>
using namespace std;

    int majorityElement(vector<int>& nums) {
            int el, cnt = 0;

            for(int i  = 0; i < nums.size(); i++)
        {
            if(cnt == 0)
            {
                el = nums[i];
                cnt= 1;
            }
            else if (nums[i] == el)
            {
                cnt++;
            } else
                cnt--; 
        }

        return el;
    }













        // unordered_map<int, int> freq;
        // for (int num : nums) {
        //     if (++freq[num] > (nums.size() / 2))
        //         return num;
        // }

        // return 0;
        
    //     map<int, int> mapp;

    //     for(int i = 0; i < nums.size(); i++)
    //     {
    //         mapp[nums[i]]++;
    //     }

    // for (const auto& pair : mapp) {
    //     if (pair.second > (nums.size() /2)) {
    //         return pair.first;
    //     }
    //  }
    //         return mostFrequentElement;