class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def devide(nums, l , r) : 
            if ( l >= r ) : 
                return nums
             
            m = (l+r)//2

            devide(nums, l, m ) 
            devide(nums, m+1, r )

            merge(nums, l, m, m+1, r)  
            return nums
            

        def merge(nums,  l1, r1, l2, r2 ) : 
            # print("Here")
            i, j, k = 0, 0, l1
            n = len(nums)
            arr1 = nums[l1:r1+1]
            arr2 = nums[l2:r2+1]

            while i < len(arr1) and j < len(arr2) : 

                if arr1[i] < arr2[j] : 
                    nums[k] = arr1[i]
                    i+=1
                else : 
                    nums[k] = arr2[j]
                    j+=1
                k+=1

            while i < len(arr1) : 
                print("here")
                nums[k] = arr1[i] 
                k+=1
                i+=1

            while j < len(arr2)  : 
                nums[k] = arr2[j] 
                k+=1
                j+=1
            
            return nums

        return devide(nums, 0, len(nums)-1) 
