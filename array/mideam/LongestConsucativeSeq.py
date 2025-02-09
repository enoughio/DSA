
# brute force solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n = len(nums) 
        if(n == 0):
            return 0

        nums.sort()
        cnt = 1
        elem = nums[0] + 1
        maxi = 1
            

        for i in range(1,n):
            # print(i)
            maxi = max(maxi, cnt)
            if(nums[i-1] == nums[i]):
                continue
            elif nums[i] == elem  : 
                elem+=1
                cnt+=1
            else:
                elem = nums[i]
                cnt = 1
                elem+=1

        return  max(maxi, cnt)
    



# optimized solution using set

    # int longestConsecutive(vector<int>& nums) {

    #     unordered_set<int> uset;

    #     if(nums.size() == 0)
    #         return 0;

    #     for(int i : nums){
    #         uset.insert(i);
    #     }

    #     int maxi = 0;

    #     for(int i : uset){

    #         if(uset.find(i-1) == uset.end()){  // if not prevous element
    #                                             // then it is the starting iteration element
    #             int j = i+1;        
    #              int cnt = 1;                   // start couting lengyh = 1, including the current element
    #             while( uset.find(j) != uset.end() ){    
    #                 cnt++;                      // next elent found then incrememt length
    #                 j++;
    #             }

    #             maxi = max(maxi, cnt);          // store max length
    #         } 
    #     }

    #     return maxi;        // returning max length

    # }



# optimized solution using set in python

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uset = set(nums)
        if(len(nums) == 0):
            return 0
        
        maxi = 0

        for i in uset:
            if i-1 not in uset:
                j = i+1
                cnt = 1

                while j in uset:
                    j+=1
                    cnt+=1
                    
                maxi = max(maxi, cnt)

        return maxi
