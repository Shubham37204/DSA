class Solution:
    def rearrangeArray(self, arr):
        n = len(arr)
        # Step 1: Sort the array
        arr.sort()
        # Step 2: Find the middle index
        mid = n // 2
        # Step 3: Reverse the second half
        i = mid
        j = n - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr

# Example usage:
arr = [8, 7, 1, 6, 5, 9]
print(Solution().rearrangeArray(arr))
