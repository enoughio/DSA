

class Solution {
public:
    pair<int, int> findMinMax(vector<int>& arr, int n) {
        if (n == 0)
            return {-1, -1}; // Handle the empty array case

        int minElement = arr[0];
        int maxElement = arr[0];

        for (int i = 1; i < n; i++) {
            if (arr[i] < minElement) {
                minElement = arr[i];
            }
            if (arr[i] > maxElement) {
                maxElement = arr[i];
            }
        }
        return {minElement, maxElement}; // Return a pair containing min and max
    }

    int boukuetMade(vector<int>& bloomDay, long long day, int flower_require,
                    int size) {

        long long cnt = 0; // adjecency flag
        long long NB = 0;  // no of bouque made

        for (int j = 0; j < size; j++) { // for array treversal

            if (day >=
                bloomDay[j]) // if that flower is bloomed on that perticular day
            {
                cnt++; // for counting consucative
            } else { // if we have enough consucative flowers to make a bouquet

                NB += (cnt / flower_require);
                cnt = 0; // if it is not consucative
            }
        }

        NB += (cnt / flower_require); // for last consucative sequence

        return NB; // returns no of bouquer made
    }

    int minDays(vector<int>& bloomDay, int m, int k) {

        int n = bloomDay.size();
        pair<int, int> p = findMinMax(bloomDay, n);

        // Ensure n < m * k without causing overflow
        if (m > 0 && n / m < k) {
            // Handle the case where m * k would cause overflow
            return -1;
        }

        long long ans = p.second;
        int st = p.first; // ans space
        int end = p.second;

        while (st <= end) {

            long long mid = (end + st) / 2;
            int bouquet = boukuetMade(bloomDay, mid, k, n);

            if (bouquet >= m) {
                ans = mid;     // store current ans
                end = mid - 1; // look for minimum
            } else {
                st = mid + 1; // go with larger value (day)
            }
        }

        return ans;
    }
};