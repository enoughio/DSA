class Solution {
public:
    bool rotateString(string s, string goal) {
        int n = s.length();
        

            for(int i = 0; i <= n; i++){   // Starting index for rotation
            
            int flag = 0;
            for (int j = 0; j < n; j++) {  // Rotate string
               
               if(goal[(i + j) % n] != s[j])  // Replace the character at the new position
               { 
                    flag = 1;
                    break;
               }
            }

            if(flag == 0 ) return true;  //validating string

        }
        
        return false;
    }
};