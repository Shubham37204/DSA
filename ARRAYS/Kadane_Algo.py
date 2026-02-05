class Solution:
    def maxSubArray(self, nums):
        maxVal = nums[0]
        current_sum = 0

        for num in nums:
            current_sum += num
            maxVal = max(maxVal, current_sum)

            if current_sum < 0:
                current_sum = 0

        return maxVal


# Test cases
s = Solution()

print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Expected 6 (subarray [4,-1,2,1])
print(s.maxSubArray([1]))                     # Expected 1
print(s.maxSubArray([5,4,-1,7,8]))            # Expected 23
print(s.maxSubArray([-1,-2,-3,-4]))           # Expected -1 (largest among negatives)
print(s.maxSubArray([2,-1,2,3,4,-5]))         # Expected 10 (subarray [2,-1,2,3,4])