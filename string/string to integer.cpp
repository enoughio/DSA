class Solution {
public:
    int myAtoi(string s) {

        int n = s.length();
        long long ans = 0;
        long long pow = 1;
        int SF = 0; // sign flag
        int RF = 0; // reset flag

        for (int i = 0; i < n; i++) {

            if (s[i] >= 48 && s[i] <= 57) // is a integer
            {

                if (RF == 1) // if we have to reset the integer to 0
                {
                    ans = 0;
                    RF = 0;
                    SF = 0;
                }
                ans = (s[i] - 48) + ans*pow;
                pow *= 10;

            } else if (s[i] == 45 || s[i] == 44 || s[i] == ' ' ) { // it's an sign
                SF = 1;
                RF = 1;  // set null flag  for cases like('543-232')
                pow = 1; // 10^ to 0 (used for conversion to int)

            } else { // not an interger

                ans = 0;
                RF = 1;  // set null flag  for cases like('543-232')
                pow = 1; // 10^ to 0 (used for conversion to int)
            }
        }

        if (SF == 1)
            ans *= -1;

        return ans;
    }
};