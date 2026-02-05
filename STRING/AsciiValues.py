class Solution(object):
    def asciiValues(self, s):
        result = []
        for ch in s:
            ascii_val = ord(ch)
            result.append(ascii_val)
        return result

#return [ord(ch) for ch in s]

#eg2 if ord is not allowed
# class Solution(object):
#     def asciiValues(self, s):
#         result = []
#         byte_data = bytearray(s, 'utf-8')  # convert string to byte array
#         for b in byte_data:
#             result.append(b)
#         return result

# Example
sol = Solution()
print(sol.asciiValues("ABC"))   # Output: [65, 66, 67]
print(sol.asciiValues("hello")) # Output: [104, 101, 108, 108, 111]
