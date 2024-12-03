class Solution {
public:
    int hIndex(vector<int>& citations) {

        int h = 0;
        int n = citations.size();

        while (h < n) {
            int nh = h + 1;
            int cnt = 0;
            int p = 0;
            while (p < n) {

                if (citations[p] >= nh) {
                    cnt++;
                    if (cnt >= nh)
                        break;
                }
                p++;
            }
            
            if (cnt >= nh)
                h = nh;
            else
                return h;
        }

        return h;
    }
};