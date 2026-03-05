
# find no of subarry with sum k 

arr = [2,3,4,1,1,4,1,3,4,3,2]
k = 6

def noOfSubarray(arr, k) : 
     
    i = 0 
    j = 0 
    cnt = 0 

    sum = 0

    while (j < len(arr)) : 

        if sum < 0 : 
            sum = 0 

        while sum > k :  
            sum -= arr[i] 
            i+=1 

        sum += arr[j] 
        j+=1 

        if sum == k : 
            cnt+=1 
    
    return cnt 

# -----------------------

# ----------Two Sum--------------

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = {}

        for i in range(len(nums)) : 

            rem = target - nums[i]

            if rem in mp : 
                return [i, mp[rem]]

            mp[nums[i]] = i

        return [0,1]  



