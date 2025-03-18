#include <bits/stdc++.h>
using namespace std;
    bool isPal(int ws, int we, string s){
        while(ws < we){
            if(s[ws] != s[we]){
                return false;
            }
            ws++;
            we--;
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




