





// Brute

// class Solution {
// public:
//     double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

//         vector<int> ans;
//         //  ans.reserve(nums1.size() + nums2.size());
//          ans.insert(ans.end(), nums1.begin(), nums1.end());
//          ans.insert(ans.end(), nums2.begin(), nums2.end());
//          sort(ans.begin(), ans.end());

//        int n = ans.size();

//         if( n%2 != 0){ // if odd length 
//             return (double)ans[n/2];
//         } else {
//             int mid = n/2;
//             return (ans[mid-1] + ans[mid] )/2.0;
//         }

//         return -1;
//     }
// };