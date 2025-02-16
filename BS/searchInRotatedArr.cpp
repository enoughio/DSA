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



class Solution {
public:
    int removeDuplicates(vector<int>& nums) {

        int i = 0;
        
        for(int j = 1; j< nums.size(); j++)
        {    if(nums[i] != nums[j])
            {
                i++;
                nums[i] = nums[j];
            }
        }
            return i+1;
    }
};




// in python
class Solution:
    def search(self, nums: List[int], t: int) -> int:
        s = 0
        e = len(nums)-1


        while( s <= e):
            mid = (s+e)//2
            
            if(nums[mid] == t):
                return mid
            
            if nums[mid] <= nums[e] :
                if t >= nums[mid] and t <= nums[e] :
                    s = mid + 1
                else:
                    e = mid - 1
            else : 
                if t >= nums[s] and t <= nums[mid] :
                    e = mid - 1
                else :
                    s = mid + 1
        
        return -1








//     int removeDuplicates(vector<int>& nums) {
//         int i=0;
//         for(int j=1;j<nums.size();j++)
//         {
//             if(nums[i] != nums[j])
//             {
//                 i++;
//                 nums[i] = nums[j];
//             }
//         }
//         return i+1;
        
//     }
// };