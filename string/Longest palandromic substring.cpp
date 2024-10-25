class Solution {
public:
  bool isPal(int st, int end, string &s) {
    int j = end;
    for (int i = st; i <= (st + end) / 2; i++, j--) {
        if (s[i] != s[j]) return false;
    }
    return true;
}

    string longestPalindrome(string s) {

    int n = s.length();
    int gap = 0;
    string ans = " ";

        while(gap <= n){
            
            int ws = 0;
            int we = gap;
            while(we <= n){
                if(!isPal(ws, we, s)){
                    ws++;
                    we++;
                } else {
                    ans = s.substr(ws, gap+1);
                    break;
                }
            }
            gap++;
        }

        return ans;
    }
};