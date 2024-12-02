class Solution {
public:
    vector<string> letterCombinations(string digits) { 
        
        int n = stoi(digits); 
        
        }
};

vector<string> fun(int n, vector<string> ans) {

    vector<string> data = {"abc", "def",  "ghi", "jkl",
                           "mno", "pqrs", "tuv", "wxyz"};

    if (n == 0)
        return ans;

    int digit = n % 10;
    n = n / 10;

    vector<string> Nans;
    if (ans.size() == 0) {
        for (char c : data[digit]) {
            Nans.push_back(c);
        }
        ans = fun(n, Nans);
    } else {
        for (char ch : data[digit]) {
            for (string s : ans) {
                s += ch;
                Nans.push_back(s);
            }
        }
        fun(n, Nans);
    }

    return ans;
}