class Solution:
    def findMedian(self, nums):
        nums.sort()  # Ensure the array is sorted
        n = len(nums)
        mid = n // 2
        
        if n % 2 != 0:
            return nums[mid]
        else:
            # Use mid-1 and mid to calculate the average
            return (nums[mid - 1] + nums[mid]) / 2


# Example usage:
arr = [2, 5, 1, 7]
print(Solution().findMedian(arr))
