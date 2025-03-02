/*

bool isValid(vector<int>& stalls, int k, int dis, int n){
    int last = stalls[0];
    int cow = 1;

    for(int i = 1; i < n; i++){
        if((stalls[i] - last) >= dis){
            last = stalls[i];
            cow++;
        }
    }

    if(cow >= k) return true;
    return false;
}

int aggressiveCows(vector<int> &stalls, int k)
{
    //    Write your code here.
    sort(stalls.begin(), stalls.end());
    int n = stalls.size();
    
    for(int mindis = 1; mindis <= stalls[n-1]; mindis++){  //search space 1 to maxidstance possible

        if(isValid(stalls, k, mindis, n) == true){
            continue;
        } else {
            return mindis-1;
        }

    }
    return -1;
}

*/







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



bool chaeck(vector<int> &stalls, int dis, int cows, int n){
    int cnt = 1;
    int prev = stalls[0];

    for(int i = 1; i < n; i++){
       int diff = stalls[i] - prev;

        if( diff >= dis){
            cnt++;
            prev = stalls[i];
        } 
        
        if( cnt >= cows)
            return true;

    }


    return false;
}


int aggressiveCows(vector<int> &stalls, int k)
{
//    Write your code here.
sort(stalls.begin(), stalls.end());
int ans = 0;
int n = stalls.size();

// for( int dis = 1; dis < ; dis++){
int dis = 1;
while(true){


    if(chaeck(stalls, dis, k, n)){
        ans = dis;
    }else{
        return ans;
    }

    dis++;

}

    return ans;

}





int check(vector<int>&nums, int m, int s, int aSum){

    int sum = nums[0];
    int br = 1;
    int i = 1;

    while( i < nums.size()){

        if(sum + nums[i] <= s){
            sum += nums[i];       
        }else{
            br++;
            sum = nums[i];
        }

        if(br == m){
            return true;
        }
        i++;
    }

    return false;
}


int findPages(vector<int>& arr, int n, int m) {
    // Write your code here.

    int aSum = 0;
    int maxElem = arr[0];

    if(m > n)
    return -1;

    for (int num : arr) {
        aSum += num;
        if (num > maxElem) {
            maxElem = num;
        }
    }

    if(m == n )
        return  maxElem;

    int ans = maxElem;
    for(int i = maxElem; i <= aSum; i++){

        if( check(arr, m, i, aSum)){
            ans = i;
        }else{
            return i-1;
        }
      
    }

     return ans;   
    
}