class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        mp = {}
        ans = [-1]*len(nums1)
        for i, v in enumerate(nums1) : 
            mp[v] = i
        
        # print(mp)

        for idx, k in enumerate(nums2) : 

            if k in mp.keys() :
                res = -1
                i = idx +1

                while i < len(nums2) :
                    if nums2[i] > k : 
                        res = nums2[i]
                        break
                    i +=1

                ans[mp[k]] = res
            
        
        return ans