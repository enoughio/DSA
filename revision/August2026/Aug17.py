class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def devide(nums, l , r) : 
            if ( l >= r ) : 
                return nums
             
            m = (l+r)//2

            devide(nums, l, m ) 
            devide(nums, m+1, r )

            return merge(nums, l, m, m+1, r)  
            

        def merge(nums,  l1, r1, l2, r2 ) : 
            print("Here")
            i, j, k = l1, l2, l1
            n = len(nums)
            # arr = [0] * n

            while i <= r1 and j <= r2 : 

                if nums[i] < nums[j] : 
                    nums[k] = nums[i]
                    i+=1
                else : 
                    nums[k] = nums[j]
                    j+=1
                k+=1

            while i <= r1 and k < n: 
                print("here")
                nums[k] = nums[i] 
                k+=1
                i+=1

            while j <= r2 and k < n : 
                nums[k] = nums[j] 
                k+=1
                j+=1
            
            return nums

        return devide(nums, 0, len(nums)-1) 


            