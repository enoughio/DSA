        int s = 0, n = nums.size(), e = n-1;

        if (n == 1 && nums[n - 1] != t)
            return false;

        while (s <= e) {
            int mid = (s + e) / 2;

            if (nums[mid] == t) {
                return true;
            } else if (nums[mid] < nums[e]) {
                if (t > nums[mid] && t <= nums[e]) {
                    s = mid + 1;
                } else {
                    e = mid - 1;
                }
            } else if (nums[mid] > nums[e]) {
                if (t < nums[mid] && t >= nums[s]) {
                    e = mid - 1;
                } else {
                    s = mid + 1;
                }
            }else if (nums[mid] == nums[e])
                e--;
        }
        return false;