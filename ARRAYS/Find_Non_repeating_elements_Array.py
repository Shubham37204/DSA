# class Solution:
#     def nonRepeating(self, a):
#         temp = []  # List to store non-repeating elements
#         for i in range(len(a)):
#             if a.count(a[i]) == 1:  # Check if the element occurs only once
#                 temp.append(a[i])
#         return temp


# # Example usage:
# nums = [1, 2, -1, 1, 3, 1]
# print(Solution().nonRepeating(nums))

class Solution:
    def nonRepeating(self, arr):
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        result = []
        for num in arr:
            if freq[num] == 1:
                result.append(num)
        return result

nums = [1, 2, -1, 1, 3, 1]
print(Solution().nonRepeating(nums))  # Output: [2, -1, 3]
