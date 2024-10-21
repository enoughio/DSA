class Solution {
public:
    int val(char c) {

        if (c == 'I')
            return 1;
        else if (c == 'V')
            return 5;
        else if (c == 'X')
            return 10;
        else if (c == 'L')
            return 50;
        else if (c == 'C')
            return 100;
        else if (c == 'D')
            return 500;
        else
            return 1000;
    }

    int romanToInt(string s) {

        int ans = 0, i = 0, n = s.length();

        while (i < n) {

            int s1 = val(s[i]);
            if (i + 1 < n) {
                int s2 = val(s[i + 1]);

                if (s2 > s1) {
                    ans += s2 - s1;
                    i++;
                } else {
                    ans += s1;
                }

            } else {
                ans += s1;
            }
            i++;
        }

        return ans;
    }
};