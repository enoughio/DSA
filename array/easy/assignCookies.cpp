#include <bits/stdc++.h>
using namespace std;


class Solution {
public:w
    int findContentChildren(vector<int>& g, vector<int>& s) {
        
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        int i = 0;
        for(int j = 0; i < g.size() && j < s.size(); j++)
        {
            if(g[i] <= s[j])
            {
                i++;
            }
        }

        return i;
    }
};

// 40ms idk why ?


// brute
    //  while(i < g.size() && j < s.size())
    //     {
    //         if(g[i] <= s[j])
    //         {
    //             cnt++;
    //             i++;
    //             j++;
    //         } else {
    //             j++;
    //         }
    //     }



//     static const bool Booster = [](){
//     std::ios_base::sync_with_stdio(false);
//     std::cout.tie(nullptr);
//     std::cin.tie(nullptr);
//     return true;
// }();