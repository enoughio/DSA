
from typing import List

def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
    n = len(nums1)
    ans = [-1] * n
    mp = {}

    for idx, i in  enumerate(nums1) : 
        mp[i] = idx

    st = []
    
    for j in range(len(nums2)-1, -1, -1) : 
        i = nums2[j]

        if i in mp : 
            while st and st[-1] < i : 
                st.pop()
            
            if st : 
                ans[mp[i]] = st[-1]
        
        st.append(i)


    return ans