#include<bits/stdc++.h>
using namespace std;


class Solution
{
  public:
    long long int substrCount (string s, int k) {
    	//code here.
    	int n = s.length();
    	
    	int i = 0;
    	int ans = 0;
    	int gap = k;
    	
    	    
    	    
    
    	while(gap < n){
    	    
    	  int ws = 0, we =gap; // create a window
    	  while(we < n) {// moving window till end
    	    
    	        map<char, int>mapp;
    	        int dist = 0;
    	       
    	        for( int j = ws; j <= we; j++){    // count number of distinct character
    	          if (mapp.find(s[j]) == mapp.end()) {
                        dist++;
                        mapp[s[j]] = 1;
                    }

    	        }
                    
                if(dist == k){
                    ans++;
                }	        
    	    // move window
    	   ws++;
    	   we++;
        }
        gap++;  // increase size of window
    }
    
        return ans;
    }
    
};