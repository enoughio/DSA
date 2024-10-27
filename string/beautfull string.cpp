class Solution {
public:
    int beautySum(string s) {

        int n = s.size();

        int sum = 0;

        for (int i = 0; i < n; i++) {
            map<char, int> mapp;
            int mini = 600;
            for (int j = i; j < n; j++) {

                mapp[s[j]]++;
                // mini = min(mini, mapp[s[j]]);   // why this not work
                // ???????????
                maxi = max(maxi, mapp[s[j]]);
                mini = INT_MAX;
                for (const auto& entry : mapp) {
                    mini = min(mini, entry.second);
                }

                sum += maxi - mini;
            }
        }

        return sum;
    }
};