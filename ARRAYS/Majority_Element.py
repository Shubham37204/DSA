class Solution:
    def majorityElement(self, nums):
        freq=0
        ans=0
        for i in range(len(nums)):
            if freq == 0:
                ans=nums[i]
            if ans == nums[i]:
                freq+=1
            else:
                freq-=1
        return ans

# Create an instance and call the method
solution = Solution()
result = solution.majorityElement([1,2,2,1,1])
print(result)
