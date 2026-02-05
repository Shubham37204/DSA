class Solution:
    def frequencyCount(self, a):
        freq = {}
        for i in a:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        return list(freq.items()) #[(10, 3), (5, 2), (15, 1)]

# Example usage:
arr = [10, 5, 10, 15, 10, 5]
result = Solution().frequencyCount(arr)
for num, count in result:
    print(f"{num} occurs {count} time(s) in the array")
