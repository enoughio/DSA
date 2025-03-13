
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pair = {}
        assigned = {}

        for i in range(len(s)) :
            if( s[i] in pair ):
                if  pair[s[i]] != t[i] :
                    return False
            else:
                if t[i] in assigned:
                    return False
                assigned[t[i]] = True
                pair[s[i]] = t[i]

        return True

    

        




''' 
cpp solution 

class Solution {
public:
    bool isIsomorphic(string s, string t) {

        unordered_map<char, char>mapp;
        unordered_map<char, bool>mapp2;

        for(int i = 0; i < s.size(); i++){

            if(mapp.find(s[i]) != mapp.end()  && mapp[s[i]] != t[i])  //in the mapp
                return false;
            else if (mapp.find(s[i]) == mapp.end() ) {   // not in mapp
                if(mapp2.find(t[i]) != mapp2.end() )
                    return false;
                
                mapp2[t[i]] = true;
                mapp[s[i]] = t[i];
            }
        }
        return true;
    }
};


'''