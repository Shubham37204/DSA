class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        subset = []

        def Subset_2(a, ans, i, subset):
            if i == len(a):
                subset.append(ans.copy()) 
                return

            ans.append(a[i])
            Subset_2(a, ans, i + 1, subset)

            ans.pop()
            idx = i + 1
            while idx < len(a) and a[idx] == a[i]:
                idx += 1
            Subset_2(a, ans, idx, subset)

        Subset_2(nums, [], 0, subset)
        return subset


# Example usage:
print(Solution().subsetsWithDup([1, 2, 2]))
