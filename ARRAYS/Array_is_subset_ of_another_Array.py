#2 method
# def isSubset(a, s):
#     return set(a).issubset(set(s))

class Solution:
    def isSubset(self, a, s):
        for i in range(len(a)):
            if a[i] not in s:
                return False
        return True

# Example usage:
nums = [1, 3, 4, 5, 2]
arr = [2, 4, 3, 1, 7, 5, 15]
print(Solution().isSubset(nums, arr))
