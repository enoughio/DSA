class Solution {
    public:
        string removeOuterParentheses(string s) {
            
            int open = 0;
            int close = 0;
            string ans = "";
    
            for(char ch : s){
                if(ch == '('){
                    open++;
    
                    if(open == 1)
                        continue;
                    ans += "(";
                } else {
                    close++;
    
                    if(open == close){
                        open = 0;
                        close = 0;
                        continue;
                    }
    
                    ans += ')';
    
                }
            }
    
            return ans;
    
        }
    };