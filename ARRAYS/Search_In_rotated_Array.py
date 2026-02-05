class Solution:
    def search(self, arr, target):
        start, end = 0, len(arr) - 1

        while start <= end:
            mid = (start + end) // 2   # Correct mid calculation

            if arr[mid] == target:
                return mid

            # If left half is sorted
            if arr[start] <= arr[mid]:
                if arr[start] <= target <= arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # Else right half is sorted
            else:
                if arr[mid] <= target <= arr[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1

a = [4, 5, 6, 7, 0, 1, 2]
print(Solution().search(a, 0))  # Output: 4
print(Solution().search(a, 3))  # Output: -1
