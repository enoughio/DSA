

/*
//why this code is note working

int aggressiveCows(vector<int> &stalls, int k)
{
    //    Write your code here.
    sort(stalls.begin(), stalls.end());
    int n = stalls.size();
    int maxDis = 0;
    
    for(int mindis = 1; mindis < stalls[n-1]; mindis++){  //search space 1 to maxidstance possible
        int cmindis = stalls[n-1]-stalls[0];
        int cow = stalls[0];  // first cow alwways at 0th position

        for(int i = 1; i < n && k > 0; i++){
            if((stalls[i]-cow) >= mindis){    // if cow can be paced with min distace of mindis
                cmindis = min(stalls[i] - cow, cmindis);  //min distance between cows
                cow = stalls[i];  // new cow at next selected stall
                k--;
            }
        }

        maxDis = max(cmindis, maxDis);  // max of min distance
    }
    return maxDis-1;
}

*/