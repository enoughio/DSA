class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {

        vector<int>mis (1001, 0);
        int n = 1, cnt = 0;
        int s = arr.size();

        int i = 0;

        while(i < s){
            if(arr[i] == n){
                n++;
                i++;
            } else {
                cnt++;
                mis[cnt] = n;
                n++;
            }
        }


        for(int i = cnt+1; i < 1001; i++){
            mis[i] = n;
            n++;
        }

 
        return mis[k];

        
    }
};