


/*

//some brute that doesn't work

   string reverseWords(string s) {
        
        string ans = "";
        int l = s.length();
        int cnt = 0;
        cout<<l;

int n = l-1;
for(; n >= 0; n--)

        if( s[n] == ' '){

            if(cnt == 0) continue; // if last character is empty space
             int m = n+1;

             while(cnt >= 0 && m < l){
                ans = ans + s[m];
                m++;
                cnt--;
             }
            //  ans= ans + ' ';

        } else {
            cnt++;
        }

        if(cnt > 0){

            while(cnt > 0){
                if( s[n+1] == ' '){
                    n++;
                    continue;
                }

                ans = ans + s[n+1];
                n++;
                cnt--;
            }

        }

        return ans;
    }
*/