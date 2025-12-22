class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n) :
            if i > 0 and nums[i] == nums[i-1] : 
                continue
            
            sum = nums[i]
            l1 = 0

            for j in range(i+1, n) :
                
                if l1 > 0 and nums[j] == nums[j-1] : 
                    continue
                l1+=1

                sum += nums[j]

                k = j+1
                l = n-1

                while k < l :
                    temp = sum + nums[k] + nums[l] 
                    
                    if temp < target :
                        k+=1 
                        while k < l and nums[k] == nums[k-1] : 
                            k+=1
                    elif temp > target : 
                        l-=1
                        while l > k and nums[l] == nums[l+1] : 
                            l -= 1
                    else : 
                        arr = [nums[i], nums[j], nums[k], nums[l]]
                        ans.append(arr)
                        k+=1 
                        l-=1
                        while k < l and nums[k] == nums[k-1] : 
                            k+=1
                        while l > k and nums[l] == nums[l+1] : 
                            l-=1


                sum -= nums[j]        
            sum -= nums[i]


        return ans