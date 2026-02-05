class Solution:
    def rotateArray(self, nums, k):
        n = len(nums)
        k = k % n  # In case k > n

        def reverse_section(array, start, end):
            while start < end:
                array[start], array[end] = array[end], array[start]
                start += 1
                end -= 1

        # Step 1: Reverse first k elements
        reverse_section(nums, 0, k - 1)

        # Step 2: Reverse the rest
        reverse_section(nums, k, n - 1)

        # Step 3: Reverse the whole array
        reverse_section(nums, 0, n - 1)

        return nums


# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7]
print(Solution().rotateArray(arr, 3))


# class Solution:
#     def rotateArray(self, nums, k, direction="left"):
#         n = len(nums)
#         k = k % n  # In case k > n

#         def reverse_section(array, start, end):
#             while start < end:
#                 array[start], array[end] = array[end], array[start]
#                 start += 1
#                 end -= 1

#         if direction == "left":
#             # Left Rotation
#             reverse_section(nums, 0, k - 1)    # Step 1: Reverse first k
#             reverse_section(nums, k, n - 1)    # Step 2: Reverse rest
#             reverse_section(nums, 0, n - 1)    # Step 3: Reverse whole
#         else:
#             # Right Rotation
#             reverse_section(nums, 0, n - 1)    # Step 1: Reverse whole
#             reverse_section(nums, 0, k - 1)    # Step 2: Reverse first k
#             reverse_section(nums, k, n - 1)    # Step 3: Reverse rest

#         return nums


# # Example usage:
# arr1 = [1, 2, 3, 4, 5, 6, 7]
# arr2 = [1, 2, 3, 4, 5, 6, 7]

# print("Left Rotation:", Solution().rotateArray(arr1, 3, "left"))   # [4, 5, 6, 7, 1, 2, 3]
# print("Right Rotation:", Solution().rotateArray(arr2, 3, "right")) # [5, 6, 7, 1, 2, 3, 4]
