class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        mp = {}
        ans = [-1]*len(nums1)
        st = []

        for i, v in enumerate(nums1) : 
            mp[v] = i

        for idx in range(len(nums2)-1, -1, -1) : 
            k = nums2[idx]
            while st and st[-1] <= k : 
                st.pop()

            if k in mp.keys() :
                res = -1

                if st : 
                    res = st[-1]
   
                ans[mp[k]] = res

            st.append(k)

        return ans