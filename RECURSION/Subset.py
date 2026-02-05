class Solution:
    def subsets(self, nums):
        subset = []

        def Subset(a, ans, i):
            # When we reach the end of the array
            if i == len(a):
                subset.append(ans.copy())
                return

            ans.append(a[i])
            Subset(a, ans, i + 1)
            ans.pop()
            Subset(a, ans, i + 1)

        Subset(nums, [], 0)
        return subset


# Example usage:
print(Solution().subsets([1, 2, 3]))
