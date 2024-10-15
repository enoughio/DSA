class Solution {
public:

    long long findTotal(int n, const vector<int>& piles, int h) {
        long long ans = 0;
        for (int i : piles) {
            ans += ceil((double)i / n);
            if(ans > h) break;
        }
        return ans;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        
        auto maxIt = max_element(piles.begin(), piles.end());

        int st = 1;
        int end = *maxIt;
        int ans = *maxIt;
        int mid;

        while(st <= end)
        {
            mid = (end + st)/2;
            int total = findTotal(mid, piles, h);

            if( total <= h ){
                ans = mid;
                end = mid - 1;
            } else {
                st = mid + 1;
            }
        }   

         return ans;

    }
};