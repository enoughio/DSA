//Maximum Nesting Depth of the Parentheses


class Solution {
public:
    int maxDepth(string s) {
        
    int maxi = 0, cnt = 0;

        for(char  ch : s){
            if(ch == '('){
                cnt++;
                maxi = max(cnt, maxi);
            }else if( ch == ')'){
                cnt--;
            }
        }

    return maxi;

    }
};  