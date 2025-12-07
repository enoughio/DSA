from typing import List


class SolutionNotWorking:
    def sortColors(self, nums: List[int]) -> None:
        
        k, i, j  = -1, -1, -1
        n = len(nums)

        if n == 1 : 
            return

        while k < n and i < n and j < n : 

            print("k : ", k)
            if k == -1 or nums[k] == 2 :
                k+=1
            elif nums[k] == 0 : 
                i += 1
                if i < n and nums[i] == 2 :
                    nums[i] = 0
                    nums[k] = 2
                    print("in : ",nums[k] )
                    k+=1
                elif i < n and nums[i] == 1 : 

                    if j+1 >= n :
                        return
                    
                    j+=1
                    temp = nums[i]
                    nums[i] = nums[k]
                    nums[k] = nums[j]
                    nums[j] = temp
                    k+=1
                    print("here mid")
            elif k < n and nums[k] == 1 : 

                if  j < i and i+1 < n :
                    j = i+1
                elif j+1 < n : 
                    j += 1
                else : 
                    return

                temp = nums[j]
                nums[j] = nums[k]
                nums[k] = temp
                print("here end")
                k+=1


        

# ---------------------------

# final solution 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        def swap(n,m) : 
            nums[n],nums[m] = nums[m],nums[n]

        n = len(nums)

        low = 0
        mid = 0
        high = n-1

        if n == 1 : 
            return

        while mid <= high : 

            if nums[mid] == 0 : 
                swap(mid, low)
                mid += 1
                low += 1
            elif nums[mid] == 1 :
                mid +=1
            else :
                swap(mid,high)
                high-=1
        
        