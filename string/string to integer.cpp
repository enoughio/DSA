/*
    int myAtoi(string s) {
        int n = s.length();
        int i = 0;
        int SF = 1;
        long long ans = 0;

        while (s[i] == ' ')
            i++;

        if (s[i] == '-') {
            SF = -1;
            i++;
        } else if (s[i] == '+') {
            SF = 1;
            i++;
        }


        while (i < n && 0 <= s[i] - '0' && s[i] - '0' <= 9) {

            
            if (ans > INT_MAX / 10 ||
                (ans == INT_MAX / 10 && s[i] - '0') > INT_MAX % 10) {
                return ans = (SF == 1 ? INT_MAX : INT_MIN);
            }
            ans = ans * 10 + s[i] - '0';
            i++;
        }

         if(ans > INT_MAX && SF == 1) return INT_MAX;
        if(ans < INT_MIN && SF == -1) return INT_MIN;

        return ans * SF;
    }
};

*/









/*
// forward count but not wirking
class Solution {
public:
    int myAtoi(string s) {

        int n = s.length();
        long long ans = 0;
        int RF = 0;
        int SF = 0;
        int set = 0;

        for (int i = 0; i < n; i++) {

            if (s[i] >= '0' && s[i] <= '9') // is a integer
            {   
                ans = ans*10 + (s[i] - '0');
                set = 1;
                if(RF == 1){
                    return ans;
                }

            } else if (s[i] == '+' && set == 0  || s[i] == '-' && set == 0 ) { // it's an sign
                SF = 1;

            } else if(s[i] == ' ' && ans == 0 ){
                continue;
            } else { // not an interger
                return ans;
                RF = 1;  // set null flag  for cases like('543-232')
            }
        }
        
            if (SF == 1)
                ans *= -1;

        return ans;

    }
};

*/



// brute Tle

// {

//         int n = s.length();
//         long long ans = 0;
//         long long pow = 1;
//         int SF = 0; // sign flag
//         int RF = 0; // reset flag

//         for (int i = n - 1; i >= 0; i--) {

//             if (s[i] >= 48 && s[i] <= 57) // is a integer
//             {

//                 if (RF == 1) // if we have to reset the integer to 0
//                 {
//                     ans = 0;
//                     RF = 0;
//                     SF = 0;
//                 }
//                 ans += (s[i] - 48) * pow;
//                 pow *= 10;

//             } else if (s[i] == 45 || s[i] == 44 || s[i] == ' ' ) { // it's an sign
//                 SF = 1;
//                 RF = 1;  // set null flag  for cases like('543-232')
//                 pow = 1; // 10^ to 0 (used for conversion to int)

//             } else { // not an interger

//                 ans = 0;
//                 RF = 1;  // set null flag  for cases like('543-232')
//                 pow = 1; // 10^ to 0 (used for conversion to int)
//             }
//         }

//         if (SF == 1)
//             ans *= -1;


//         return (int) ans;
//     }







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