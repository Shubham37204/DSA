class Solution:
    def nextGreaterElement(self, nums1, nums2):

        nge = {}  #an unordered map of c++
        s = []  
        n=len(nums2)

        for i in range(n-1, -1, -1):   # right → left
            while len(s) > 0 and s[-1] <= nums2[i]:
                s.pop()
            if len(s) == 0: 
                nge[i] = -1
            else:
                nge[i] = s[-1]
            s.append(nums2[i])   # must be inside loop

            ans = []
            for num in nums1:
                ans.append(nge[num])

            return ans
