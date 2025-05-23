class Solution {
public:
    int calSum(int L, vector<int>& nums, int n, int k){
        int sum = 0;
        int maxSum = 0;
        int i = 0;

        for(i = 0; i < n; i++){

            if(sum + nums[i] <= L){
                sum += nums[i];
            } else {
                k--;
                maxSum = max(maxSum, sum);
                sum = nums[i];
              
                if( k == 1) break;

            }
        }

        
            for(int j = i; j < n; j++){
                sum += nums[i];
            } 

            k--;
            maxSum = max(maxSum, sum);
            
            return (k == 0 ? maxSum : -1);

    }

    int splitArray(vector<int>& nums, int k) {
        
        int sum;
        for(int i : nums){
            sum += i;
        }
        int n = nums.size();
        int maxi = sum;
        int me = *max_element(nums.begin(), nums.end());

        for(int L = me; L < sum; L++){

            int  sumMax = calSum(L, nums, n , k);

            if(sumMax != -1){
                maxi = min(maxi, sumMax);
            } else {
                return maxi;
            }
        }

        return -1;
    }
};











// TLE
class Solution {
public:
    bool calSplit(vector<int>&nums, int k, int l){

        int sum = 0;
        for(int i : nums){
            if(sum + i <= l){
                sum += i;
            } else {
                sum = i;
                k--;
                if(k == 0) return true;  // L split array into more then k parts
            }
        }

        return false;  //L splits array in it is equal or less parts
    }

    int splitArray(vector<int>& nums, int k) {
        

        if(k > nums.size()) return -1;

        int max = *max_element(nums.begin(), nums.end());
        int sum = 0;
        
        for(int i : nums)
            sum += i;
        
        //  Return the minimized largest sum of the split. 
        //  means feed it in assending order and once it satisfy the constrain return it
        // for lesser value it will split array into more parts 
      //-----  // for right value it will split array into exactly k parts
        // for higher value it will split lesser parts
        for(int i = max; i <= sum; i++)
        {
            
            if(calSplit(nums, k, i) == true){
                continue;
            } else {
                return i;
            }

        }

    return -1;

    }
};









class Solution {
    public:
        int check(vector<int>& nums, int s, int k) {
    
            int maxi = nums[0];
            int barrier = 1;
            int st = 0;
            int i = 0;
            int sum = 0;
    
            while (i < nums.size()) {
    
                if (sum + nums[i] < s) {
    
                    barrier++;
                    maxi = max(sum, maxi);
                    st = i;
                } else {
                    sum += nums[i];
                }
                
                if (barrier >= k) {
                    return maxi;
                }
    
                i++;
            }
    
            return max(sum, maxi);
    
        }
    
        int splitArray(vector<int>& nums, int k) {
    
    
            int sum = 0;
    
            for( int i : nums){
                sum+= i;
            }
            
            int miniSub = nums[0];
    
            for(int s = nums[0]; s < sum; s++){
                int cm = check(nums, s, k);
                miniSub = max(miniSub, cm);
            }
    
            return miniSub;
        }
    };




    class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        mAr = 0

        for i in range(n):
            height = heights[i]

            rmax = i + 1
            while rmax < n and heights[rmax] >= height:
                rmax += 1
            
            lmax = i
            while lmax >= 0 and heights[lmax] >= height:
                lmax -= 1
            
            rmax -= 1
            lmax += 1
            mAr = max(mAr, height * (rmax - lmax + 1))
        return mAr