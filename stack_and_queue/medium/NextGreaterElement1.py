class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n = len(nums2)
        m = len(nums1)

        ans = [-1] * m

        map = { }
        for idx, i in enumerate(nums1) :
            map[i] = idx

        stack = []
        for i in range(n) :
            
            while stack and nums2[i] > stack[-1] :
                top = stack[-1]
                idx = map[top] 
                ans[idx] = nums2[i]
                stack.pop()


            if nums2[i] in map : 
                stack.append(nums2[i])
            
        return ans 