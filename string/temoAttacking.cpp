class Solution {
public:
    // just check if the next attack done is within the affected    duration or not



    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        
        int cnt = 0;
        int n = timeSeries.size();

        for (int i = 0; i+1 < n; i++) {

            if (  (timeSeries[i] + duration - 1) < timeSeries[i + 1]) {
                cnt += duration;    // if the next attack is not in affected range 
                // then add poisone duration to total
            } else {
                cnt += timeSeries[i + 1] - timeSeries[i];
                 // if the next attack is in the affected range 
                // then add the differance in between attack to total
            }
        }
        cnt += duration;

        return cnt;
    }
};