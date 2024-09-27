class Solution {
public:

    long long calSum(vector<int>& nums, int div){
            double sum = 0;
            for(int i = 0; i < nums.size(); i++){
                sum += ceil(nums[i]/(double) div );
            }
            return sum;
    }


    int smallestDivisor(vector<int>& nums, int threshold) {

        int max = *max_element(nums.begin(), nums.end());  // find max
    

          // search space
        int st = 1;  // 1 
        int end = max; // max element
        int ans = max;

        while(st <= end){
            int mid = (end + st )/2;
            long long sum = calSum(nums, mid);  // calculate sum of division

            if(sum <= threshold){   // if sum is less then threshold
                ans  = mid;         // store current ans and 
                end = mid - 1;   // thrn look for smaller
            }
            else    
                st = mid + 1;

        }        
            return ans;        
    }
};






//TLE

// public:

//     long long calSum(vector<int>& nums, int div){
//             double sum = 0;

//             for(int i = 0; i < nums.size(); i++){
//                 // (nums[i] < div ? sum++ : 
//                 sum += ceil(nums[i]/(double) div );
//             }
//             return sum;
//     }


//     int smallestDivisor(vector<int>& nums, int threshold) {

//         int max = *max_element(nums.begin(), nums.end());
    
//         for(int div = 1;  div <= max; div++){

//             long long sum = calSum(nums, div);

//             if(sum <= threshold)
//                 return div;
//         }        
//             return max;        
//     }
// };