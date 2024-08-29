#include <bits/std++.h>
using namespace std;

class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        
        string r1 = "qwertyuiop";
        string r2 = "asdfghjkl";
        string r3 = "zxcvbnm";

        vector<string> ans;

        for(auto w : words)
        {
           int cnt1 = 0, cnt2 =  0, cnt3 = 0;

           for(auto ch : w )
           {
               if(r1.find(tolower(ch)) != string::npos)
               {
                    cnt1 = 1;
                    break;
               }
           }

           for(auto ch : w )
           {
               if(r2.find(tolower(ch)) != string::npos)
               {
                    cnt2 = 1;
                    break;
               }
           }

           if(cnt1 == 1 && cnt2 == 1)
            continue;

      
           for(auto ch : w )
           {
               if(r3.find(tolower(ch)) != string::npos)
               {
                    cnt3 = 1;
                    break;
               }
           }

            if(cnt1 == 1 && cnt3 == 1 || cnt3 == 1 && cnt2 == 1)
                continue;

            if(cnt1 == 1 || cnt2 == 1 || cnt3 == 1)
                ans.push_back(w);


           cout<<cnt1<<" "<<cnt2<<" "<<cnt3;
           cout<<endl;
            
        }

        return ans;
    }
};
