class Solution {
public:
    int search(vector<int>& nums, int t) {

        int s = 0;
        int e = nums.size() - 1;
        int mid = s + (e - s) / 2;

        while (s <= e) {
            if (nums[mid] == t)
                return mid;

            if (nums[mid] >= nums[s]) {
                if (t >= nums[s] && t < nums[mid]) {
                    e = mid - 1;
                } else {
                    s = mid + 1;
                }
            } else {
                if (t > nums[mid] && t <= nums[e]) {
                    s = mid + 1;
                } else {
                    e = mid - 1;
                }
            }

            mid = s + (e - s) / 2;
        }

        return -1;
    }
};