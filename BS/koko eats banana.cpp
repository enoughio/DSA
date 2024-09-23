class Solution {
public:
    long long findTotal(int n, vector<int>& piles){
        long long ans = 0;

        for(int i : piles){
            ans += ceil(i/n);
        }
        cout<<ans<<" ";
        return ans;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        
        auto maxIt = max_element(piles.begin(), piles.end());

        int st = 0; 
        int end = *maxIt;
        int ans = *maxIt;
        int mid;

        while(st <= end)
        {
            mid = (end + st)/2;
            int total = findTotal(mid, piles);

            if( total <= h ){
                ans = mid;
                end = mid - 1;
            } else {
                st = mid + 1;
            }
        }   

        // cout<<"::"<<mid<<" : mid";

         return ans;

    }
};