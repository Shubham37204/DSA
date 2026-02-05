class Solution:
    def repeatingElement(self, a):
        a.sort()  # Sort the array so duplicates come together
        temp = []  # List to store repeating elements
        
        for i in range(1, len(a)):
            if a[i] == a[i - 1] and a[i] not in temp:
                temp.append(a[i])
        
        return temp  # Return the full list of duplicates


# Example usage:
arr = [1, 1, 2, 3, 4, 4, 5, 2]
print(Solution().repeatingElement(arr))


# class Solution:
#     def repeatingElement(self, a):
#         freq = {}
#         temp = []
#         for num in a:
#             if num in freq:
#                 freq[num] += 1
#             else:
#                 freq[num] = 1
        
#         for num in freq:
#             if freq[num] > 1:
#                 temp.append(num)
        
#         return temp

# # Example usage:
# arr = [1, 1, 2, 3, 4, 4, 5, 2]
# print(Solution().repeatingElement(arr))  # [1, 2, 4]
