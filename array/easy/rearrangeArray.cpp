class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {

        int n = nums.size();
        vector<int>ans(n);

        int p = 0, N = 1;
        for(int i = 0; i < n; i++)
        {

            if(nums[i] >= 0 )
            {
                ans[p] = nums[i];
                p = p+2;
            } else {
                ans[N] = nums[i];
                N = N+2;
            }
        }

        return ans;

    }


// python

class Solution:
def rearrangeArray(self, nums: List[int]) -> List[int]:
    
    pos = []
    neg = []

    for i in nums:
        if i > 0:
            pos.append(i)
        else :
            neg.append(i)

    j = 0
    i = 0
    while i < len(nums) and j < len(pos) and j < len(neg):
        nums[i] = pos[j]
        i += 1
        print(i)
        if i <  len(nums) :
            nums[i] = neg[j]
        i += 1
        j += 1


    return nums
