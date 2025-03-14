#include <bits/stdc++.h>
using namespace std;

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









class tolution:
    def romanToInt(self, s: str) -> int:
        mp = { 'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100 ,'D': 500, 'M':1000}
        ans = 0
        n = len(s)

        i = 0
        while(i < n):
            if( i+1 < n and s[i] == 'I' and s[i+1] == 'V' ):
                ans = ans + 4
                i+=1
            elif(  i+1 < n and s[i] == 'I' and s[i+1] == 'X' ):
                ans = ans + 9
                i+=1
            elif(  i+1 < n and s[i] == 'X' and s[i+1] == 'L' ):
                ans = ans + 40
                i+=1
            elif(  i+1 < n and s[i] == 'X' and s[i+1] == 'C' ):
                ans = ans + 90
                i+=1
            elif(  i+1 < n and s[i] == 'C' and s[i+1] == 'D' ):
                ans = ans + 400
                i+=1
            elif(  i+1 < n and s[i] == 'C' and s[i+1] == 'M' ):
                ans = ans + 900
                i+=1
            else:
                ans = mp[s[i]]+ans

            i+=1
            

        return ans