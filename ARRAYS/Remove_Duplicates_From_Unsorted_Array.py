class Solution:
    def removeDuplicate(self, nums):
        temp = []
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp.append(nums[i])
        return temp


# Example usage:
arr = [4, 3, 9, 2, 4, 1, 10, 89, 34]
print(Solution().removeDuplicate(arr))
